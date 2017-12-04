CREATE PROCEDURE [dbo].[GetCities]
		@id INT = NULL
AS
	IF @id IS NOT NULL
		SELECT Cities.Id, Cities.Name, Cities.CountryId, Countries.Name as CountryName
		FROM Cities
		JOIN Countries ON Cities.CountryId=Countries.Id
		WHERE Cities.IsDeleted = 0 AND Countries.IsDeleted = 0 AND Countries.Id=@id
		ORDER BY Name

	ELSE
		SELECT Cities.Id, Cities.Name, Cities.CountryId, Countries.Name as CountryName
		FROM Cities
		JOIN Countries ON Cities.CountryId=Countries.Id
		WHERE Cities.IsDeleted = 0 AND Countries.IsDeleted = 0
		ORDER BY CountryName, Name
RETURN 0
