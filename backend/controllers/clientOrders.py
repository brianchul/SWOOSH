from sqlalchemy.exc import InvalidRequestError, IntegrityError
from config.DBindex import db_session
from models.order import ClientOrders
from models.mission import MissionClientOrderRelate
from pkg.logger import get_logger as log
from datetime import datetime
from pkg.checkDictMatch import checkDictKeyMatchArray


modelKey = [
    "satellite_name" ,
    "weight_kg" ,
    "purpose" ,
    "request_by" ,
    "eta_height_km" ,
    "arrival_date" ,
    "inclination" ,
    "budget_billion",
    "launch_day",
    "status"
]

def FindAll():
    try:
        query = ClientOrders.query.all()
        dataDict = []
        for data in query:
            data.__dict__.pop("_sa_instance_state")
            dataDict.append(data.__dict__)
        return dataDict, 200
    except :
        log().error("clientOrder controller findall")
        return None, 404


def FindOne(cond):
    try:
        """if "id" not in cond:
            return None, 400
        orderID = cond.pop("id")

        querydict, isMatch = checkDictKeyMatchArray(modelKey, cond)
        if not isMatch:
            return None, 400"""
        query = ClientOrders.query.filter_by(id=cond)

        if query.one_or_none() is not None:
            q = query.one_or_none()
            q.__dict__.pop("_sa_instance_state")
            return q.__dict__, 200
        else:
            return None, 404
    except InvalidRequestError:
        log().error("InvalidRequestError")
        return None, 400


def Create(cond):
    querydict = {}
    querydict, isMatch = checkDictKeyMatchArray(modelKey, cond)
    if not isMatch:
        return None, 400

    createClientOrder = ClientOrders(**querydict)
    
    try:
        db_session.add(createClientOrder)
        db_session.commit()
        return querydict, 200
    except InvalidRequestError:
        log().error("Unable to create data")
        return None, 400
    except IntegrityError:
        log().error("Foreign key not found")
        return None, 400


def Patch(content):
    try:
        if not content['id']:
            return None, 400
        query = ClientOrders.query.filter_by(id=content.pop("id")).one_or_none()
        if query is not None:
            querydict = {}
            querydict, isMatch = checkDictKeyMatchArray(modelKey, content)
            if not isMatch:
                return None, 400
            for key in querydict:
                setattr(query, key, querydict[key])
            db_session.commit()
            return querydict, 200
        else:
            return None, 404
    except InvalidRequestError:
        log().error("Unable to patch data")
        return None, 400

def Delete(id):
    try:
        toDel = ClientOrders.query.filter_by(id=id).first()
        if toDel is not None:
            delRelate = MissionClientOrderRelate.query.filter_by(clientOrder_id=id)
            if delRelate.one_or_none() is not None:
                for data in delRelate.all():
                    db_session.delete(data)
            db_session.commit()
            
            db_session.delete(toDel)
            db_session.commit()
            return 200
        else:
            return 400
    except InvalidRequestError:
        log().error("Unable to delete clientOrder data")
        return 400
