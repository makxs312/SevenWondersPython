from BLL.FlightService import FlightService
from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity
import pdb

flight_controller = Blueprint("flightt_controller", __name__, url_prefix = "/api/Flights")
service = FlightService()

@flight_controller.route("/GetFlightsShortInfo", methods=["GET"])
def get_flights_short_info():
    data = service.get_flight_short_info(request.get_json("id"))
    result = dict()
    return jsonify(result)