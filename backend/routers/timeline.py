from flask import request, Blueprint
from controllers import timelines
from pkg.warpResponse import warpResponse


timeline = Blueprint('timeline', __name__)


@timeline.route("/", methods=['GET'])
def getAllTimelines():
    resp, code = timelines.FindAll()
    if resp is not None:
        return warpResponse(resp)
    else:
        return warpResponse(None, code)


@timeline.route("/", methods=['POST'])
def getOneTimelines():
    r = request.get_json()
    resp, code = timelines.FindOne(r)
    if resp is not None:
        return warpResponse(resp)
    else:
        return warpResponse(None, code)


@timeline.route("/add", methods=['POST'])
def createTimelines():
    r = request.get_json()
    code = timelines.Create(r)
    if code is not None:
        return warpResponse(None, code)
    else:
        return warpResponse(None, code)


@timeline.route("/<id>", methods=['POST'])
def patchTimelines(id):
    r = request.get_json()
    code = timelines.Patch(id, r)
    if code is not None:
        return warpResponse(None, code)
    else:
        return warpResponse(None, code)