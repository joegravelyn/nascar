CREATE TABLE dbo.SeasonCars
(
      SeasonCarID    INT         NOT NULL IDENTITY(1, 1)
   ,  TeamID         INT
   ,  SeriesID       INT         NOT NULL
   ,  Season         SMALLINT    NOT NULL
   ,  CarNumber      VARCHAR(3)  NOT NULL

   ,  CONSTRAINT PK_SeasonCars PRIMARY KEY (SeasonCarID)
   ,  CONSTRAINT FK_SeasonCarsTeams FOREIGN KEY (TeamID) REFERENCES dbo.Teams
   ,  CONSTRAINT FK_SeasonCarsSeries FOREIGN KEY (SeriesID) REFERENCES dbo.Series
)
