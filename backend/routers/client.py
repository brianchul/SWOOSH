from flask import request, Blueprint
from controllers import clients
from pkg.warpResponse import warpResponse


client = Blueprint('client', __name__)


@client.route("/", methods=['GET'])
def getAllClients():
    resp, code = clients.FindAll()
    if resp is not None:
        return warpResponse(resp)
    else:
        return warpResponse(None, code)


@client.route("/", methods=['POST'])
def getOneClient():
    r = request.get_json()
    resp, code = clients.FindOne(r)
    if resp is not None:
        return warpResponse(resp)
    else:
        return warpResponse(None, code)


@client.route("/add", methods=['POST'])
def createClient():
    r = request.get_json()
    code = clients.Create(r)
    if code is not None:
        return warpResponse(None, code)
    else:
        return warpResponse(None, code)


@client.route("/<name>", methods=['POST'])
def patchClient(name):
    r = request.get_json()
    code = clients.Patch(name, r)
    if code is not None:
        return warpResponse(None, code)
    else:
        return warpResponse(None, code)