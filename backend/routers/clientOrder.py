from flask import request, Blueprint
from controllers import clientOrders
from pkg.warpResponse import warpResponse
from pkg.datetimeValidator import validate


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
    if validate(r['arrival_date']) and validate(r['launch_day']):
        resp, code = clientOrders.Create(r)
        if resp is not None:
            return warpResponse(resp, code)
        else:
            return warpResponse(None, code)
    else:
        return warpResponse("Datetime error", 400)


@clientOrder.route("/patch", methods=['POST'])
def patchClientOrder():
    r = request.get_json()
    if 'arrival_date' in r and not validate(r['arrival_date']) or 'launch_day' in r and not validate(r['launch_day']):
        return warpResponse("Datetime error", 400)
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