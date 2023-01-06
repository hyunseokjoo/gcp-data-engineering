insert into {{ GCP_PROJECT_ID }}.{{ BIGQUERY_DATASET_TARGET }}.auth_events(
 ts, level, city, state, userAgent, lon, lat, userId,
 lastName, firstName, gender, registration, success )
 selecT  ts, level, city, state, userAgent, lon, lat, userId,
 lastName, firstName, gender, registration, success 
 from {{ GCP_PROJECT_ID }}.{{ BIGQUERY_DATASET_STAGING }}.auth_events;