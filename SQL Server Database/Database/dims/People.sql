CREATE TABLE dbo.People
(
      PersonID       INT            NOT NULL IDENTITY(1, 1)
   ,  PersonName     VARCHAR(200)   NOT NULL
   ,  DateOfBirth    DATE
   ,  HomeCity       VARCHAR(200)
   ,  HomeState      VARCHAR(200)
   ,  HomeCountry    VARCHAR(200)

   ,  CONSTRAINT PK_People PRIMARY KEY (PersonID)
)
