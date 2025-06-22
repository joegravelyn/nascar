/*
Post-Deployment Script Template                     
--------------------------------------------------------------------------------------
 This file contains SQL statements that will be appended to the build script.      
 Use SQLCMD syntax to include a file in the post-deployment script.         
 Example:      :r .\myfile.sql                        
 Use SQLCMD syntax to reference a variable in the post-deployment script.      
 Example:      :setvar TableName MyTable                     
               SELECT * FROM [$(TableName)]               
--------------------------------------------------------------------------------------
*/
INSERT INTO dbo.Manufacturers (ManufacturerName)
VALUES
      ('Ford')
   ,  ('Chevrolet')
   ,  ('Toyota')
;

INSERT INTO dbo.Series (SeriesName, SeriesShortName)
VALUES
      ('Cup Series', 'Cup')
   ,  ('Xfinity Series', 'NXS')
   ,  ('Craftsman Truck Series', 'Truck')
   ,  ('ARCA Menards Series', 'ARCA')
   ,  ('ARCA Menards Series East', 'ARCA East')
   ,  ('ARCA Menards Series West', 'ARCA West')
;

INSERT INTO dbo.Tracks (TrackName, TrackShortName, LocationCity, LocationState, Latitude, Longitude, FirstRace)
VALUES
      ('Bowman Gray Stadium', 'BOW', 'Winston-Salem', 'North Carolina', 36.082778, -80.222222, '1949/05/18')
   ,  ('Daytona International Speedway', 'DAY', 'Daytona Beach', 'Florida', 29.185556, -81.069444, '1959/02/06')
   ,  ('Atlanta Motor Speedway', 'ATL', 'Hampton', 'Georgia', 33.383494, -84.317856, '1960/07/31')
;