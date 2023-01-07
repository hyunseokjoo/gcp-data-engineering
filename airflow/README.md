## Setup Composer

GCP환경에서 Composer를 올려서 사용할 예정 이전에 bigquery에 테이블이 생성 되어있어야 합니다.

- Composer에 파일을 올리기 전에 streamify_dag.py의 project id, bucket id 를 변경해줍니다.
- 또한, dag의 start_date을 자신에게 GCS의 폴더 시간에 맞게 변경해줍니다.
- Composer의 UI에서 Airflow DAG폴더를 클릭하여 GCS접속하고 해당 GCS Bucket에 Sql폴더와 Streamify_dag.py를 업로드 해준다
- Airflow 웹 접속을 클릭하여 DAG확인해 준다.