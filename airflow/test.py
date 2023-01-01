import os
from pathlib import Path

EVENTS = ['listen_events', 'page_view_events', 'auth_events'] 

GCP_PROJECT_ID = 'your_project_id'
GCP_GCS_BUCKET = 'your_bucket_id'
BIGQUERY_DATASET = 'staging'
EXECUTION_DATETIME_STR = '{{ logical_date.strftime("%m%d%H") }}'

TABLE_MAP = { f"{event.upper()}_TABLE" : event for event in EVENTS}
EXTERNAL_MAP = { f"external_{event.upper()}" : event for event in EVENTS}

MACRO_VARS = {"GCP_PROJECT_ID":GCP_PROJECT_ID, 
              "BIGQUERY_DATASET": BIGQUERY_DATASET, 
              "EXECUTION_DATETIME_STR": EXECUTION_DATETIME_STR
              }

MACRO_VARS.update(TABLE_MAP)
MACRO_VARS.update(EXTERNAL_MAP)


print(MACRO_VARS)


p = Path(os.getcwd() , 'sql', 'external_listen_events.sql')
fd = open(p , 'r')
sqlFile = fd.read()
fd.close()

print(p)
print(sqlFile)
