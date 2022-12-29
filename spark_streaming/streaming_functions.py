from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, month, hour, dayofmonth, col, year, udf

# 사용자 정의 함수 디코딩
@udf
def string_decode(s, encoding='utf-8'):
    if s:
        return (s.encode('latin1')        
                .decode('unicode-escape') 
                .encode('latin1')         
                .decode(encoding)         
                .strip('\"'))

    else:
        return s

# spark session 만드는 함수 
def create_or_get_spark_session(app_name, master="yarn"):
    spark = (SparkSession
             .builder
             .appName(app_name)
             .master(master=master)
             .getOrCreate())

    return spark

# kafka stream을 읽는 함수
def create_kafka_read_stream(spark, kafka_address, kafka_port, topic, starting_offset="earliest"):
    read_stream = (spark
                   .readStream
                   .format("kafka")                                                         # format으로 정의 기본 kafka, rabbitmq 등 사용 가능 
                   .option("kafka.bootstrap.servers", f"{kafka_address}:{kafka_port}")      # kafka 서버 설정
                   .option("failOnDataLoss", False)                                         # 데이터 손실 여부 - 기본 손실하지 않도록 설정됨
                   .option("startingOffsets", starting_offset)                              # StartingPoint - earliest = 처음부터, latest = 최신 오프셋만
                   .option("subscribe", topic)                                              # 읽을 토픽 지정
                   .load())

    return read_stream


def process_stream(stream, stream_schema, topic):
    # value.data 형식으로 데이터가 전달되어 data에 있는 값을 select하여 테이블화 하는 로직
    stream = (stream
              .selectExpr("CAST(value AS STRING)")
              .select(
                  from_json(col("value"), stream_schema).alias(
                      "data")
              )
              .select("data.*")
              )

    # 년, 월, 일, 시 추가
    stream = (stream
              .withColumn("ts", (col("ts")/1000).cast("timestamp"))
              .withColumn("year", year(col("ts")))
              .withColumn("month", month(col("ts")))
              .withColumn("hour", hour(col("ts")))
              .withColumn("day", dayofmonth(col("ts")))
              )

    # string 인코딩
    if topic in ["listen_events", "page_view_events"]:
        stream = (stream
                .withColumn("song", string_decode("song"))
                .withColumn("artist", string_decode("artist")) 
                )

    return stream

# Stream 쓰기 함수
def create_file_write_stream(stream, storage_path, checkpoint_path, trigger="120 seconds", output_mode="append", file_format="parquet"):
    write_stream = (stream
                    .writeStream
                    .format(file_format)                            # file_format 지정 - 기본 parquet로 설정함
                    .partitionBy("month", "day", "hour")            # 월, 일, 시로 Partitioning
                    .option("path", storage_path)                   # storage_path 지정
                    .option("checkpointLocation", checkpoint_path)  # checkpoint 관리 장소 지정
                    .trigger(processingTime=trigger)                # 트리거 전략 - 기본 2분으로 설정함
                    .outputMode(output_mode))                       # outputmode - 기본 append mode - 나머지는 둘 중 선택 가능 complete mode, update mode

    return write_stream