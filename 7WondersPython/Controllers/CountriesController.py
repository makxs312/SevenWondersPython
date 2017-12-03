from BLL.CountriesService import CountriesService
from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity
import pdb

countries_controller = Blueprint("countries_controller", __name__, url_prefix = "/api/Countries")
service = CountriesService()

@countries_controller.route("/GetCountries", methods=["GET"])
def get_countries():
    data = service.get_countries()
    return jsonify(data)

@countries_controller.route("/GetCountry", methods=["GET"])
def get_country():
    data = service.get_country(request.args.get('id', ''))
    return jsonify(data)

@countries_controller.route("/IsNameValid", methods=["GET"])
def is_name_valid():
    valid = service.is_name_valid(request.args.get('id', ''), request.args.get('name', ''))
    return jsonify(len(valid) == 0)

@countries_controller.route("/DeleteCountry", methods=["POST"])
def delete_country():
    service.delete_country(request.args.get('id', ''))
    return 'Ok'