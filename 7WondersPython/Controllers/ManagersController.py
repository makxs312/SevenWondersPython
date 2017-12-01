from BLL.ManagersService import ManagersService
from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity
import pdb

managers_controller = Blueprint("managers_controller", __name__, url_prefix = "/api/Managers")
service = ManagersService()

class Responce(object):
    Countries = [],
    DateOfBirth = "",
    Email = "",
    FirstName = "",
    Id = "",
    IsDeleted = "",
    LastName = "",
    PhoneNumber = ""

@managers_controller.route("/GetManagers", methods=["POST"])
def get_managers():
    data = service.get_managers()
    return jsonify(data)

@managers_controller.route("/GetCountries", methods=["GET"])
def get_countries():
    data = service.get_countries()
    return jsonify(data)

@managers_controller.route("/GetManager/<int:id>", methods=["GET"])
def get_manager(id):
    data = service.get_manager(id)
    result = data[0]
    responce = Responce(),
    #responce.DateOfBirth = result.DateOfBirth
    result["Countries"] = service.get_countries()
    return jsonify(result)

@managers_controller.route("/ChangeManagerStatus/<int:id>", methods=["POST"])
def change_manager_status(id):
    service.change_manager_status(id)
    return 'Ok'

@managers_controller.route("/AddManager", methods=["POST"])
def add_manager():
    service.add_manager(request.form)
    return 'Ok'