CREATE  PROCEDURE [dbo].[GetCountries]
AS
	SELECT * FROM Countries WHERE IsDeleted = 0
RETURN 0
