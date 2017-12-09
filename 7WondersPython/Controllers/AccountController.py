from BLL.AccountService import AccountService
from flask import Blueprint, jsonify, request, abort 

account_controller = Blueprint("account_controller", __name__, url_prefix = "/api/Account")
service = AccountService()

@account_controller.route("/Login", methods=["POST"])
def login():
    succeeded = service.login(request.form)
    if (succeeded == True):
        return 'Ok'
    else:
        return abort(400)

@account_controller.route("/LogOut", methods=["POST"])
def logout():
    service.logout()
    return 'Ok'
