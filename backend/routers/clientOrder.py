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


@clientOrder.route("/findOne", methods=['POST'])
def getOneClient():
    r = request.get_json()
    resp, code = clientOrders.FindOne(r['id'])
    if resp is not None:
        return warpResponse(resp, code)
    else:
        return warpResponse(None, code)


@clientOrder.route("/add", methods=['POST'])
def createClientOrder():
    r = request.get_json()
    resp, code = clientOrders.Create(r)
    if resp is not None:
        return warpResponse(resp, code)
    else:
        return warpResponse(None, code)


@clientOrder.route("/patch", methods=['POST'])
def patchClientOrder():
    r = request.get_json()
    resp, code = clientOrders.Patch(r)
    if resp is not None:
        return warpResponse(resp, code)
    else:
        return warpResponse(None, code)

@clientOrder.route("/delete", methods=['POST'])
def deleteClientOrder():
    r = request.get_json()
    code = clientOrders.Delete(r['id'])
    return warpResponse(None, code)