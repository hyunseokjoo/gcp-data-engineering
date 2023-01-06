insert into {{ GCP_PROJECT_ID }}.{{ BIGQUERY_DATASET_TARGET }}.page_view_events(
 ts, page, auth, method, status, level, 
 city, state, userAgent, lon, lat, userId, lastName, 
 firstName, gender, registration, artist, song, duration)
 selecT ts, page, auth, method, status, level, 
 city, state, userAgent, lon, lat, userId,lastName, 
 firstName, gender, registration, artist, song, duration
 from {{ GCP_PROJECT_ID }}.{{ BIGQUERY_DATASET_STAGING }}.page_view_events;