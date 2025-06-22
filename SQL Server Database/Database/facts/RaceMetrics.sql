CREATE TABLE dbo.RaceMetrics
(
      RaceMetricID   INT            NOT NULL IDENTITY(1, 1)
   ,  RaceID         INT            NOT NULL
   ,  Stage          INT            NOT NULL CONSTRAINT DF_RaceMetrics_Stage DEFAULT 0
   ,  MetricName     VARCHAR(200)   NOT NULL
   ,  MetricValue    VARCHAR(200)   NOT NULL

   ,  CONSTRAINT PK_RaceMetrics PRIMARY KEY (RaceMetricID)
   ,  CONSTRAINT FK_RaceMetricsRace FOREIGN KEY (RaceID) REFERENCES dbo.Races
)
