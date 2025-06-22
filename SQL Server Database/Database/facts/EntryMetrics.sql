CREATE TABLE dbo.EntryMetrics
(
      EntryMetricID  INT            NOT NULL IDENTITY(1, 1)
   ,  RaceID         INT            NOT NULL
   ,  SeasonCarID    INT            NOT NULL
   ,  MetricName     VARCHAR(200)   NOT NULL
   ,  MetricValue    VARCHAR(200)

   ,  CONSTRAINT PK_EntryMetrics PRIMARY KEY (EntryMetricID)
   ,  CONSTRAINT FK_EntryMetricsRaces FOREIGN KEY (RaceID) REFERENCES dbo.Races
   ,  CONSTRAINT FK_EntryMetricsSeasonCars FOREIGN KEY (SeasonCarID) REFERENCES dbo.SeasonCars
)
