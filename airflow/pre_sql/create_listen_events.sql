 CREATE TABLE {{ GCP_PROJECT_ID }}.{{ BIGQUERY_DATASET_TARGET }}.listen_events 
 ( 
  artist STRING,
  song STRING,
  duration FLOAT64,
  ts TIMESTAMP,
  auth STRING,
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
  registration INTEGER
 );       
