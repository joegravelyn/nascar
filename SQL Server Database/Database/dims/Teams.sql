CREATE TABLE dbo.Teams
(
      TeamID      INT            NOT NULL IDENTITY(1, 1)
   ,  TeamName    VARCHAR(200)   NOT NULL
   ,  OwnerName   VARCHAR(200)   NOT NULL

   ,  CONSTRAINT PK_Teams PRIMARY KEY (TeamID)
)
