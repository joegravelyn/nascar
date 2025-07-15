CREATE TABLE lap_times_laps
(
      year              int
   ,  race_id           int
   ,  series_id         int
   ,  car_number        int
   ,  driver_full_name  varchar(200)
   ,  mfr               varchar(50)
   ,  finish_pos        int
   ,  driver_id         int
   ,  lap_number        int
   ,  lap_time          decimal(10,3)
   ,  lap_speed         decimal(10, 3)
   ,  running_pos       int
)
;