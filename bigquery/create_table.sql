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

CREATE TABLE {{ GCP_PROJECT_ID }}.{{ BIGQUERY_DATASET_TARGET }}.page_view_events 
 ( 
  ts TIMESTAMP,
  page STRING,
  auth STRING,
  method STRING,
  status INTEGER,
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
  artist STRING,
  song STRING,
  duration FLOAT6
 );