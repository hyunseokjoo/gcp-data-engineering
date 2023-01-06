import os
from pathlib import Path
from datetime import datetime
from airflow import DAG
from airflow.providers.google.cloud.operators.bigquery import (BigQueryCreateExternalTableOperator, 
                                                               BigQueryInsertJobOperator,
                                                               BigQueryDeleteTableOperator)


EVENTS = ['listen_events', 'page_view_events', 'auth_events'] 


GCP_PROJECT_ID = {your_project_id}
GCP_GCS_BUCKET = {your_bucket_id}

BIGQUERY_DATASET_STAGING = 'staging'
BIGQUERY_DATASET_TARGET = 'target'

EXECUTION_MONTH = '{{ execution_date.strftime("%-m") }}'
EXECUTION_DAY = '{{ execution_date.strftime("%-d") }}'
EXECUTION_HOUR = '{{ execution_date.strftime("%-H") }}'
EXECUTION_DATETIME_STR = '{{ execution_date.strftime("%m%d%H") }}'

TABLE_MAP = { f"{event.upper()}_TABLE" : event for event in EVENTS}

MACRO_VARS = {
    "GCP_PROJECT_ID" : GCP_PROJECT_ID, 
    "GCP_GCS_BUCKET" : GCP_GCS_BUCKET, 
    "BIGQUERY_DATASET_STAGING" : BIGQUERY_DATASET_STAGING, 
    "BIGQUERY_DATASET_TARGET" : BIGQUERY_DATASET_TARGET, 
    "EXECUTION_DATETIME_STR": EXECUTION_DATETIME_STR
}

MACRO_VARS.update(TABLE_MAP)

default_args = {
    'owner' : 'airflow'
}

with DAG(
    dag_id = f'streamify_dag_test',
    default_args = default_args,
    description = f'Hourly data pipeline to generate dims and facts for streamify',
    schedule_interval="5 * * * *", # 매 시간 : 5분 마다 dag실행
    start_date=datetime(2022,12,31,9),
    catchup=True,
    max_active_runs=1,
    user_defined_macros=MACRO_VARS,
    tags=['streamify']
) as dag:
    

    for event in EVENTS:
        
        staging_table_name = event  
        merge_query = f'merge_{event}'
        external_table_name = f'{staging_table_name}'
        events_data_path = f'{staging_table_name}/month={EXECUTION_MONTH}/day={EXECUTION_DAY}/hour={EXECUTION_HOUR}'
        
        create_external_table_task = BigQueryCreateExternalTableOperator(
            task_id = f'{event}_create_external_table',
            table_resource = {
                'tableReference': {
                'projectId': '{{ GCP_PROJECT_ID }}',
                'datasetId': '{{ BIGQUERY_DATASET_STAGING }}',
                'tableId': f'{external_table_name}',
                },
                'externalDataConfiguration': {
                    'sourceFormat': 'PARQUET',
                    'sourceUris': [f'gs://{ GCP_GCS_BUCKET }/{events_data_path}/*'],
                },
            }
        )

        execute_insert_query_task = BigQueryInsertJobOperator(
            task_id = f'{event}_execute_insert_query',
            configuration = {
                'query': {
                    'query': f'sql/insert_{event}.sql',
                    'useLegacySql': False
                },
                'timeoutMs' : 300000,
                'defaultDataset' : {
                    'projectId': '{{ GCP_PROJECT_ID }}',
                    'datasetId': '{{ BIGQUERY_DATASET_TARGET }}'
                    }
                }
        )

        delete_external_table_task = BigQueryDeleteTableOperator(
            task_id = f'{event}_delete_external_table',
            deletion_dataset_table = f'{ GCP_PROJECT_ID }.{ BIGQUERY_DATASET_STAGING }.{external_table_name}',
            ignore_if_missing = True
        )           
        
        create_external_table_task >> \
        execute_insert_query_task >> \
        delete_external_table_task
