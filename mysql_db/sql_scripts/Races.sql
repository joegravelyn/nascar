CREATE TABLE races
(
      race_id              int            not null
   ,  master_race_id       int            not null
   ,  series_id            int            not null
   ,  season               int            not null
   ,  race_name            varchar(200)   not null
   ,  track_id             int            not null
   ,  track_name           varchar(200)   not null
   ,  scheduled_date       datetime       not null
   ,  scheduled_distance   decimal(5, 2)  not null
   ,  scheduled_laps       int            not null
   ,  race_type_id         int            not null
   ,  restrictor_plate     BOOL           not null
   ,  playoff_round        int            not null
)
;