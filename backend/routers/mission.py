from flask import request, Blueprint
from controllers import missions
from pkg.warpResponse import warpResponse


mission = Blueprint('hello', __name__)


@mission.route("/", methods=['GET'])
def getAllMissions():
    resp, code = missions.FindAll()
    if resp is not None:
        return warpResponse(resp)
    else:
        return warpResponse(None, code)


@mission.route("/", methods=['POST'])
def getOneMission():
    r = request.get_json()
    resp, code = missions.FindOne(r)
    if resp is not None:
        return warpResponse(resp)
    else:
        return warpResponse(None, code)


@mission.route("/add", methods=['POST'])
def createMission():
    r = request.get_json()
    code = missions.Create(r)
    if code is not None:
        return warpResponse(None, code)
    else:
        return warpResponse(None, code)


@mission.route("/<id>", methods=['POST'])
def patchMission(id):
    r = request.get_json()
    code = missions.Patch(id, r)
    if code is not None:
        return warpResponse(None, code)
    else:
        return warpResponse(None, code)