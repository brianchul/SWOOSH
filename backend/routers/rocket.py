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


@rocket.route("/findOne", methods=['POST'])
def getOneRocket():
    r = request.get_json()
    resp, code = rockets.FindOne(r)
    if resp is not None:
        return warpResponse(resp, code)
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


@rocket.route("/patch", methods=['POST'])
def patchRocket():
    r = request.get_json()
    resp, code = rockets.Patch(r)
    if resp is not None:
        return warpResponse(resp, code)
    else:
        return warpResponse(None, code)

@rocket.route("/delete", methods=['POST'])
def deleteRocket():
    r = request.get_json()
    code = rockets.Delete(r['id'])
    return warpResponse(None, code)