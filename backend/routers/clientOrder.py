from flask import request, Blueprint
from controllers import clientOrders
from pkg.warpResponse import warpResponse


clientOrder = Blueprint('clientOrder', __name__)


@clientOrder.route("/", methods=['GET'])
def getAllClients():
    resp, code = clientOrders.FindAll()
    if resp is not None:
        return warpResponse(resp)
    else:
        return warpResponse(None, code)


@clientOrder.route("/", methods=['POST'])
def getOneClient():
    r = request.get_json()
    resp, code = clientOrders.FindOne(r)
    if resp is not None:
        return warpResponse(resp)
    else:
        return warpResponse(None, code)


@clientOrder.route("/add", methods=['POST'])
def createClientOrder():
    r = request.get_json()
    code = clientOrders.Create(r)
    if code is not None:
        return warpResponse(None, code)
    else:
        return warpResponse(None, code)


@clientOrder.route("/<id>", methods=['POST'])
def patchClient(id):
    r = request.get_json()
    code = clientOrders.Patch(id, r)
    if code is not None:
        return warpResponse(None, code)
    else:
        return warpResponse(None, code)