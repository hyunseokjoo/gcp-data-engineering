CREATE TABLE {{ GCP_PROJECT_ID }}.{{ BIGQUERY_DATASET_TARGET }}.auth_events 
 ( 
  ts TIMESTAMP,
  level STRING,
  city STRING,
  state STRING,
  userAgent STRING,
  lon FLOAT64,
  lat FLOAT64,
  userId INTEGER,
  lastName STRING,
  firstName STRING,
  gender STRING,
  registration INTEGER,
  success BOOLEA
 );       
