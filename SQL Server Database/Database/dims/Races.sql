CREATE TABLE dbo.Races
(
      RaceID      INT            NOT NULL IDENTITY(1, 1)
   ,  SeriesID    INT            NOT NULL
   ,  TrackID     INT            NOT NULL
   ,  RaceName    VARCHAR(200)   NOT NULL
   ,  RaceDate    DATE           NOT NULL

   ,  CONSTRAINT PK_Races PRIMARY KEY (RaceID)
   ,  CONSTRAINT FK_RacesSeries FOREIGN KEY (SeriesID) REFERENCES dbo.Series
   ,  CONSTRAINT FK_RacesTrack FOREIGN KEY (TrackID) REFERENCES dbo.Tracks
)
