## Setup Composer

GCP환경에서 Composer를 올려서 사용할 예정 이전에 bigquery에 테이블이 생성 되어있어야 합니다.

- Composer에 파일을 올리기 전에 streamify_dag.py의 project id, bucket id 를 변경해 준다.
- 또한, dag의 start_date를 변경해 준다.
- Composer에서 올라온 Airflow DAG폴더를 클릭하여 GCS접속 
- 해당 GCS Bucket에 Sql폴더와 Streamify_dag.py를 업로드 해준다
- Airflow 웹 접속을 클릭하여 DAG확인