CREATE TABLE schedule
(
      start_time        datetime
   ,  end_time          datetime
   ,  event_name        varchar(200)
   ,  race_id           int
   ,  track_id          int
   ,  track_name        varchar(200)
   ,  race_name         varchar(200)
   ,  series_id         int
   ,  run_type          int
   ,  start_time_utc    datetime
   ,  end_time_utc      datetime
)
;