CREATE TABLE dbo.Manufacturers
(
      ManufacturerID    INT            NOT NULL IDENTITY(1, 1)
   ,  ManufacturerName  VARCHAR(200)   NOT NULL

   ,  CONSTRAINT PK_Manufacturers PRIMARY KEY (ManufacturerID)
)
