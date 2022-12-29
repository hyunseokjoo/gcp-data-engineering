먼저 [Kafka 구축](../kafka/README.md) 이 끝난 다음 진행해 주세요. 구축이 되었다면, DataProc에서 Spark Cluster를 만들어 주세요. Kafka broker에 연결하여 Spark Streaming을 이용하여 GCS에 적재 합니다.

- Master node에 ssh 접속합니다.
  ```bash
  ssh streamify-spark
  ```

- git의 내용을 받아줍니다.
  ```bash
  git clone https://github.com/hyunseokjoo/gcp-data-engineering.git && \
  cd gcp-data-engineering/spark_streaming
  ```

- 환경 설정
  - Kafka 주소와 GCS bucket을 환경에 등록해 줍니다.
    ```bash
    export KAFKA_ADDRESS={your_compute_instance_external_ip}
    export GCP_GCS_BUCKET={your_bucket_name}
    ```

- Spark Streaming 실행
  ```bash
  spark-submit \
  --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2 \
  stream_all_events.py
  ```

- 알맞게 설정과 실행이 되었다면 Bucket에 parquet파일로 내려질 것 입니다.

- 읽는 토픽은 아래와 같습니다.
  - listen_events
  - page_view_events
  - auth_events