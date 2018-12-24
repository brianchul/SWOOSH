from flask import request, Blueprint
from controllers import missionOrders
from pkg.warpResponse import warpResponse
from pkg.logger import get_logger as log


missionOrder = Blueprint('missionOrder', __name__)


@missionOrder.route("/", methods=['GET'])
def getAllMissionOrder():
    resp, code = missionOrders.FindAll()
    if resp is not None:
        return warpResponse(resp)
    else:
        return warpResponse(None, code)


@missionOrder.route("/findOne", methods=['POST'])
def getOneMissionOrder():
    r = request.get_json()
    resp, code = missionOrders.FindOne(r['id'])
    if resp is not None:
        return warpResponse(resp)
    else:
        return warpResponse(None, code)


@missionOrder.route("/add", methods=['POST'])
def createMissionOrder():
    r = request.get_json()
    code = missionOrders.Create(r)
    if code is not None:
        return warpResponse(None, code)
    else:
        return warpResponse(None, code)


@missionOrder.route("/patch", methods=['POST'])
def patchMissionOrder():
    r = request.get_json()
    log().debug(r)
    resp, code = missionOrders.Patch(r)
    if resp is not None:
        return warpResponse(resp, code)
    else:
        return warpResponse(None, code)

@missionOrder.route("/delete", methods=['POST'])
def deleteMissionOrder():
    r = request.get_json()
    code = missionOrders.Delete(r['id'])
    return warpResponse(None, code)