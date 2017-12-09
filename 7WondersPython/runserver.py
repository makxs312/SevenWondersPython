from os import environ
from flask import Flask, json, Response
from flask import render_template, session
from Controllers.ManagersController import managers_controller
from Controllers.CustomersController import customers_controller
from Controllers.CountriesController import countries_controller
from Controllers.CitiesController import cities_controller
from Controllers.AirportsController import airports_controller
from Controllers.AccountController import account_controller
from flask_jwt_extended import JWTManager
from Helpers.json_helper import json_types_handler
from jinja2 import TemplateNotFound

app = Flask(__name__, template_folder='templates')
app.config['JWT_SECRET_KEY'] = "YLU]o:qifk]Z17{H'l2hIC?7_YbQ]"
jwt = JWTManager(app)

wsgi_app = app.wsgi_app
app.register_blueprint(managers_controller)
app.register_blueprint(customers_controller)
app.register_blueprint(countries_controller)
app.register_blueprint(cities_controller)
app.register_blueprint(airports_controller)
app.register_blueprint(account_controller)

json.JSONEncoder.default = json_types_handler

@app.route('/')
def index():
    data = {
        "title": 'Home Page',
        "msg":'GG wp',
        "me": environ.get('USERNAME')}
    return render_template('Home/Index.html',data=data)

@app.route('/ManagersManagement/Index.html')
def html_managers_management_lookup():
    try:
        return render_template('ManagersManagement/Index.html')
    except TemplateNotFound:
        abort(404)

@app.route('/CustomersManagement/Index.html')
def html_customers_management_lookup():
    try:
        return render_template('CustomersManagement/Index.html')
    except TemplateNotFound:
        abort(404)

@app.route('/Countries/Index.html')
def html_countries_lookup():
    try:
        return render_template('Countries/Index.html')
    except TemplateNotFound:
        abort(404)

@app.route('/Cities/Index.html')
def html_cities_lookup():
    try:
        return render_template('Cities/Index.html')
    except TemplateNotFound:
        abort(404)

@app.route('/Airports/Index.html')
def html_airports_lookup():
    try:
        return render_template('Airports/Index.html')
    except TemplateNotFound:
        abort(404)

@app.route('/Search/Index.html')
def html_search_lookup():
    try:
        return render_template('Search/Index.html')
    except TemplateNotFound:
        abort(404)

@app.route('/Home/Contact.html')
def html_contact_lookup():
    try:
        return render_template('Home/Contact.html')
    except TemplateNotFound:
        abort(404)

@app.route('/Account/Login.html')
def html_login_lookup():
    try:
        return render_template('Account/Login.html')
    except TemplateNotFound:
        abort(404)

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
   
    app.secret_key = os.urandom(12)
    app.run(HOST, PORT, debug=False, threaded=True)