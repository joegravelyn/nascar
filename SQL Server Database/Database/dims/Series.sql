CREATE TABLE dbo.Series
(
      SeriesID          INT            NOT NULL IDENTITY(1, 1)
   ,  SeriesName        VARCHAR(200)   NOT NULL
   ,  SeriesShortName   VARCHAR(200)

   ,  CONSTRAINT PK_Series PRIMARY KEY (SeriesID)
)
