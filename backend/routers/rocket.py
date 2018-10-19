from flask import request, Blueprint
from controllers import rockets
from pkg.warpResponse import warpResponse


rocket = Blueprint('rocket', __name__)


@rocket.route("/", methods=['GET'])
def getAllRockets():
    resp, code = rockets.FindAll()
    if resp is not None:
        return warpResponse(resp)
    else:
        return warpResponse(None, code)


@rocket.route("/", methods=['POST'])
def getOneRocket():
    r = request.get_json()
    resp, code = rockets.FindOne(r)
    if resp is not None:
        return warpResponse(resp)
    else:
        return warpResponse(None, code)


@rocket.route("/add", methods=['POST'])
def createRocket():
    r = request.get_json()
    code = rockets.Create(r)
    if code is not None:
        return warpResponse(None, code)
    else:
        return warpResponse(None, code)


@rocket.route("/<name>", methods=['POST'])
def patchRocket(name):
    r = request.get_json()
    code = rockets.Patch(name, r)
    if code is not None:
        return warpResponse(None, code)
    else:
        return warpResponse(None, code)