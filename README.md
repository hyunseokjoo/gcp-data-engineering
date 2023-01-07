# Introduction
GCP Data 분석 플랫폼을 구축해보는 Toy Project입니다.

## Architecture
![Architecture](./images/architecture.png)

- Toy Project에서는 위같은 아키텍쳐를 가집니다. 위의 환경을 기반으로 데이터 플랫폼을 구축 하볼 예정입니다.
    ### 구축과정
    1. [Kafka 구축](./kafka/README.md)
    2. [Spark Streaming 구축](./spark_streaming/README.md)
    3. [Bigquery 구축](./bigquery/README.md)
    4. [Airflow 구축](./airflow/README.md)
        

#### Scenario
    1. Eventsim & Kafka 구축 
    2. DataProc안에 Spark Streaming 실행하여 Kafka to GCS 데이터 이관
    3. Composer(Airflow)를 이용하여 및 GCS to Bigquery 데이터 적재 
    4. DataStudio와 연결하여 데이터 시각화

#### Result
![Architecture](./images/bi.png)


#### 툴 및 기술
- Stream Data - [**Eventsim**](https://github.com/Interana/eventsim)
- Cloud - [**Google Cloud Platform**](https://cloud.google.com)
- Containerization - [**Docker**](https://www.docker.com), [**Docker Compose**](https://docs.docker.com/compose/)
- Stream Processing - [**Kafka**](https://kafka.apache.org), [**Spark Streaming**](https://spark.apache.org/docs/latest/streaming-programming-guide.html)
- Orchestration - [**Airflow**](https://airflow.apache.org)
- Data Lake - [**Google Cloud Storage**](https://cloud.google.com/storage)
- Data Warehouse - [**BigQuery**](https://cloud.google.com/bigquery)
- Data Visualization - [**Data Studio**](https://datastudio.google.com/overview)
- Language - [**Python**](https://www.python.org)