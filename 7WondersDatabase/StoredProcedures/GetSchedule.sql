CREATE PROCEDURE [dbo].[GetSchedule]
	@id BIGINT
AS
	SELECT * FROM [dbo].[Schedules]
	WHERE Id = @id
	ORDER BY DayOfWeek
RETURN 0
