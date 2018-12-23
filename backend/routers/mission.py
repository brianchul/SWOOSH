from flask import request, Blueprint
from controllers import missions
from pkg.warpResponse import warpResponse


mission = Blueprint('mission', __name__)


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
    return warpResponse(None, code)


@mission.route("/patch", methods=['POST'])
def patchMissionOrder():
    r = request.get_json()
    resp, code = missions.Patch(r)
    if resp is not None:
        return warpResponse(resp, code)
    else:
        return warpResponse(None, code)

@mission.route("/delete", methods=['POST'])
def deleteMissionOrder():
    r = request.get_json()
    code = missions.Delete(r['id'])
    return warpResponse(None, code)