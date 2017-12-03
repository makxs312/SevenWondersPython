CREATE PROCEDURE [dbo].[IsNameValid]
	@id BIGINT,
	@name NVARCHAR(MAX)
AS
    SELECT * FROM Countries
	WHERE Id <> @id AND Name = @name
RETURN 0