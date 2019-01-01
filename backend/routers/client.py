from flask import request, Blueprint
from controllers import clients
from pkg.warpResponse import warpResponse
from pkg.logger import get_logger as log


client = Blueprint('client', __name__)


@client.route("/", methods=['GET'])
def getAllClients():
    resp, code = clients.FindAll()
    return warpResponse(resp, code)


@client.route("/findOne", methods=['POST'])
def getOneClient():
    r = request.get_json()
    resp, code = clients.FindOne(r['id'])
    return warpResponse(resp, code)


@client.route("/register", methods=['POST'])
def registerClient():
    r = request.get_json()
    resp, code = clients.FindOne(r['username'])
    if code == 200:
        return warpResponse(None, 401, "User Exist")
    code = clients.Create(r)
    return warpResponse(None, code)

@client.route("/login", methods=['POST'])
def loginClient():
    r = request.get_json()
    resp, code = clients.Login(r)
    return warpResponse(resp, code)

@client.route("/patch", methods=['POST'])
def patchClient():
    r = request.get_json()
    code = clients.Patch(r)
    return warpResponse(None, code)

@client.route("/delete", methods=["POST"])
def deleteClient():
    r = request.get_json()
    user = r["username"]
    code = clients.Delete(user)
    return warpResponse(None, code)