CREATE TABLE py.AuditLog
(
      LogDate           DATETIME       NOT NULL
   ,  SourceFileName    VARCHAR(200)   NOT NULL
   ,  SourcePageNum     VARCHAR(200)
   ,  SourcePageMetric  VARCHAR(200)
   ,  SeriesShortName   VARCHAR(200)
   ,  RaceDate          VARCHAR(200)
   ,  TrackName         VARCHAR(200)
   ,  RaceName          VARCHAR(200)
   ,  CarNumber         VARCHAR(200)
   ,  MetricName        VARCHAR(200)
   ,  MetricValue       VARCHAR(200)
   ,  LogMessage        VARCHAR(200)
)
