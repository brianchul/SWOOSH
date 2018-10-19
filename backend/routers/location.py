from flask import request, Blueprint
from controllers import locations
from pkg.warpResponse import warpResponse


location = Blueprint('location', __name__)


@location.route("/", methods=['GET'])
def getAllLocations():
    resp, code = locations.FindAll()
    if resp is not None:
        return warpResponse(resp)
    else:
        return warpResponse(None, code)


@location.route("/", methods=['POST'])
def getOneLocation():
    r = request.get_json()
    resp, code = locations.FindOne(r)
    if resp is not None:
        return warpResponse(resp)
    else:
        return warpResponse(None, code)


@location.route("/add", methods=['POST'])
def createLocation():
    r = request.get_json()
    code = locations.Create(r)
    if code is not None:
        return warpResponse(None, code)
    else:
        return warpResponse(None, code)


@location.route("/<id>", methods=['POST'])
def patchLocation(id):
    r = request.get_json()
    code = locations.Patch(id, r)
    if code is not None:
        return warpResponse(None, code)
    else:
        return warpResponse(None, code)