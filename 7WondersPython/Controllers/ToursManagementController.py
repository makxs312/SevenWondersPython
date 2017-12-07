from BLL.ToursManagementService import ToursManagementService
from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity
import pdb

tours_management_controller = Blueprint("tours_management_controller", __name__, url_prefix = "/api/ToursManagement")
service = ToursManagementService()

@tours_management_controller.route("/GetToursForManager", methods=["GET"])
def get_tours_for_manager():
    data = service.get_tours_for_manager(27)
    result = dict()
    result["tours"] = data
    return jsonify(result)