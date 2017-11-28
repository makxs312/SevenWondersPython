from BLL.ManagersService import ManagersService
from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity

managers_controller = Blueprint("managers_controller", __name__, url_prefix = "/api/Managers")
service = ManagersService()

@managers_controller.route("/GetManagers", methods=["POST"])
def get_managers():
    data = service.get_managers()
    return jsonify(data)

@managers_controller.route("/ChangeManagerStatus/<int:id>", methods=["POST"])
def change_manager_status(id):
    service.change_manager_status(id)
    return 'Ok'

