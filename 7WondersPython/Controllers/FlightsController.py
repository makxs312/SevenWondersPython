from BLL.FlightsService import FlightsService
from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity

flights_controller = Blueprint("flights_controller", __name__, url_prefix = "/api/Flights")
service = FlightsService()

@flights_controller.route("/GetFlights", methods=["GET"])
def get_flights():
    data = service.get_flights(request.args.get('pageIndex', ''), request.args.get('pageSize',''))
    return jsonify(data)

@flights_controller.route("/GetSchedule", methods=["GET"])
def get_schedule():
    data = service.get_flights(request.args.get('id', ''))
    return jsonify(data)