CREATE TABLE py.EtlLog
(
      LogDate           DATETIME       NOT NULL
   ,  Process           VARCHAR(200)   NOT NULL
   ,  ProcessStart      DATETIME
   ,  ProcessEnd        DATETIME
   ,  LogMessage        VARCHAR(200)
   ,  Files             VARCHAR(MAX)
)
