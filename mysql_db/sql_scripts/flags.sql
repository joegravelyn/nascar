CREATE TABLE flags
(
      race_id           int
   ,  series_id         int
   ,  lap_number        int
   ,  flag_state        int
   ,  elapsed_time      decimal(10, 4)
   ,  comment           varchar(500)
   ,  beneficiary       int
   ,  time_of_day       decimal(10, 4)
   ,  time_of_day_os    timestamp
)
;