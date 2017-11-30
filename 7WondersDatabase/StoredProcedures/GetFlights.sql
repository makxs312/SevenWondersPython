CREATE PROCEDURE [dbo].[GetFlights]
	@pageIndex BIGINT,
	@pageSize BIGINT
AS
SELECT * FROM [dbo].[Flights]
ORDER BY Id
OFFSET @pageSize * @pageIndex ROWS
FETCH NEXT @pageSize ROWS ONLY
RETURN 0