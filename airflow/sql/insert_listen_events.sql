insert into {{ GCP_PROJECT_ID }}.{{ BIGQUERY_DATASET_TARGET }}.listen_events(
 artist, song, duration, ts,  auth, 
 level, city, state, userAgent, lon, lat, 
 userId, lastName, firstName, gender, registration  )
 selecT artist, song, duration, ts,  auth, 
 level, city, state, userAgent, lon, lat, 
 userId, lastName, firstName, gender, registration 
 from {{ GCP_PROJECT_ID }}.{{ BIGQUERY_DATASET_STAGING }}.listen_events;