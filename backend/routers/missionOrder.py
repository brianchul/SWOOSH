from flask import request, Blueprint
from controllers import missionOrders
from pkg.warpResponse import warpResponse


missionOrder = Blueprint('missionOrder', __name__)


@missionOrder.route("/", methods=['GET'])
def getAllMissionOrder():
    resp, code = missionOrders.FindAll()
    if resp is not None:
        return warpResponse(resp)
    else:
        return warpResponse(None, code)


@missionOrder.route("/", methods=['POST'])
def getOneMissionOrder():
    r = request.get_json()
    resp, code = missionOrders.FindOne(r)
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


@missionOrder.route("/<id>", methods=['POST'])
def patchMissionOrder(id):
    r = request.get_json()
    code = missionOrders.Patch(id, r)
    if code is not None:
        return warpResponse(None, code)
    else:
        return warpResponse(None, code)