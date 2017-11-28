from os import environ
from flask import Flask, json, Response
from flask import render_template
from Controllers.ManagersController import managers_controller
from flask_jwt_extended import JWTManager
from Helpers.json_helper import json_types_handler
from jinja2 import TemplateNotFound

app = Flask(__name__, template_folder='templates')
app.config['JWT_SECRET_KEY'] = "YLU]o:qifk]Z17{H'l2hIC?7_YbQ]"
jwt = JWTManager(app)

wsgi_app = app.wsgi_app
app.register_blueprint(managers_controller)

json.JSONEncoder.default = json_types_handler


@app.route('/')
def index():
    data = {
        "title": 'Home Page',
        "msg":'GG wp',
        "me": environ.get('USERNAME')}
    return render_template('Home/Index.html',data=data)

@app.route('/ManagersManagement/Index.html')
def html_lookup():
    try:
        return render_template('ManagersManagement/Index.html')
    except TemplateNotFound:
        abort(404)

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, debug=True, threaded=True)