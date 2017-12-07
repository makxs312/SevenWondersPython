CREATE PROCEDURE [dbo].[GetFlightShortInfoModel]
	@id BIGINT
AS
	SELECT LeaveFlightInfo.Number AS LeaveFlightNumber,
	LeaveAirplanes.Model AS LeaveFlightAirplaneModel,
	LeaveAirplanes.Company AS LeaveFlightAirplaneCompany, 
	LeaveDepAirport.Name AS LeaveFlightDepartureAirport,
	LeaveDepCity.Name AS LeaveFlightDepartureCity,
	LeaveDepCountry.Name AS LeaveFlightDepartureCountry,
	Res.LeaveDate + ' ' + LeaveSchedules.DepartureTime AS LeaveFlightDepartureTime,
	LeaveArrAirport.Name AS LeaveFlightArrivalAirport,
	LeaveArrCity.Name AS LeaveFlightArrivalCity,
	LeaveArrCountry.Name AS LeaveFlightArrivalCountry,
	Res.LeaveDate + ' ' + LeaveSchedules.ArrivalTime AS LeaveFlightArrivalTime,

	ReturnFlightInfo.Number AS ReturnFlightNumber,
	ReturnAirplanes.Model AS ReturnFlightAirplaneModel,
	ReturnAirplanes.Company AS ReturnFlightAirplaneCompany, 
	ReturnDepAirport.Name AS ReturnFlightDepartureAirport,
	ReturnDepCity.Name AS ReturnFlightDepartureCity,
	ReturnDepCountry.Name AS ReturnFlightDepartureCountry,
	Res.ReturnDate + ' ' + ReturnSchedules.DepartureTime AS ReturnFlightDepartureTime,
	ReturnArrAirport.Name AS ReturnFlightArrivalAirport,
	ReturnArrCity.Name AS ReturnFlightArrivalCity,
	ReturnArrCountry.Name AS ReturnFlightArrivalCountry,
	Res.ReturnDate + ' ' + ReturnSchedules.ArrivalTime AS ReturnFlightArrivalTime

	FROM Tours
	JOIN Reservations AS Res ON Tours.ReservationId=Res.Id
	JOIN Schedules AS LeaveSchedules ON Res.LeaveScheduleId = LeaveSchedules.Id
	JOIN Flights AS LeaveFlightInfo ON LeaveSchedules.FlightId = LeaveFlightInfo.Id
	JOIN Airplanes AS LeaveAirplanes ON LeaveFlightInfo.AirplaneId = LeaveAirplanes.Id
	JOIN Airports AS LeaveDepAirport ON LeaveFlightInfo.DepartureAirportId = LeaveDepAirport.Id
	JOIN Cities AS LeaveDepCity ON LeaveDepAirport.CityId = LeaveDepCity.Id
	JOIN Countries AS LeaveDepCountry ON LeaveDepCity.CountryId = LeaveDepCountry.Id
	JOIN Airports AS LeaveArrAirport ON LeaveFlightInfo.ArrivalAirportId = LeaveArrAirport.Id
	JOIN Cities AS LeaveArrCity ON LeaveArrAirport.CityId = LeaveArrCity.Id
	JOIN Countries AS LeaveArrCountry ON LeaveArrCity.CountryId = LeaveArrCountry.Id

	JOIN Schedules AS ReturnSchedules ON Res.ReturnScheduleId = ReturnSchedules.Id
	JOIN Flights AS ReturnFlightInfo ON ReturnSchedules.FlightId = ReturnFlightInfo.Id
	JOIN Airplanes AS ReturnAirplanes ON ReturnFlightInfo.AirplaneId = ReturnAirplanes.Id
	JOIN Airports AS ReturnDepAirport ON ReturnFlightInfo.DepartureAirportId = ReturnDepAirport.Id
	JOIN Cities AS ReturnDepCity ON ReturnDepAirport.CityId = ReturnDepCity.Id
	JOIN Countries AS ReturnDepCountry ON ReturnDepCity.CountryId = ReturnDepCountry.Id
	JOIN Airports AS ReturnArrAirport ON ReturnFlightInfo.ArrivalAirportId = ReturnArrAirport.Id
	JOIN Cities AS ReturnArrCity ON ReturnArrAirport.CityId = ReturnArrCity.Id
	JOIN Countries AS ReturnArrCountry ON ReturnArrCity.CountryId = ReturnArrCountry.Id
	WHERE Tours.Id = @id
RETURN 0
