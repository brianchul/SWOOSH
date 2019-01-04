from flask import Flask, jsonify, make_response
from config.DBindex import db_session

from routers.mission import mission
from routers.location import location
from routers.rocket import rocket
from routers.client import client
from routers.clientOrder import clientOrder
from routers.missionOrder import missionOrder
from routers.timeline import timeline
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.register_blueprint(mission, url_prefix="/mission")
app.register_blueprint(location, url_prefix="/location")
#app.register_blueprint(rocket, url_prefix="/rocket")
app.register_blueprint(client, url_prefix="/client")
app.register_blueprint(clientOrder, url_prefix="/clientOrder")
app.register_blueprint(missionOrder, url_prefix="/missionOrder")
# app.register_blueprint(timeline, url_prefix="/timeline")


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.before_request
def befReq():
    db_session.rollback()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()