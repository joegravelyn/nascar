CREATE TABLE dbo.Tracks
(
      TrackID        INT            NOT NULL IDENTITY(1, 1)
   ,  TrackName      VARCHAR(200)   NOT NULL
   ,  TrackShortName VARCHAR(200)
   ,  LocationCity   VARCHAR(200)
   ,  LocationState  VARCHAR(200)
   ,  Latitude       DECIMAL(8, 4)
   ,  Longitude      DECIMAL(8, 4)
   ,  FirstRace      DATE

   ,  CONSTRAINT PK_Tracks PRIMARY KEY (TrackID)
)
