from sqlalchemy.exc import InvalidRequestError, IntegrityError
from config.DBindex import db_session
from models.mission import Missions
from models.rocket import Rockets
from pkg.logger import get_logger as log
from pkg.checkDictMatch import checkDictKeyMatchArray
from datetime import datetime

modelKey = [
    "launch_date",
    "launch_rocket",
    "status",
    "target_inclination",
    "target_height_km",
    "create_by",
    "pair_order",
    "rocket_max_payload_weight"
]

def FindAll():
    query = Missions.query.all()
    dataDict = []
    for data in query:
        """if data.launch_rocket is not None:
            queryRocket = Rockets.query.filter_by(name=data.launch_rocket).one_or_none()
            queryRocket.__dict__.pop("_sa_instance_state")
            queryRocket.__dict__.pop('id')
            data.launch_rocket = [queryRocket.__dict__]"""
        data.__dict__.pop("_sa_instance_state")
        dataDict.append(data.__dict__)
    return dataDict, 200

def FindOne(cond):
    try:
        if 'id' not in cond:
            return None, 400
        cond.pop('id')
        querydict, isMatch = checkDictKeyMatchArray(modelKey, cond)
        if not isMatch:
            return None, 400
        query = Missions.query.filter_by(**querydict).one_or_none()
        if query is not None:
            """if query.launch_rocket is not None:
                queryRocket = Rockets.query.filter_by(name=query.launch_rocket).one_or_none()
                queryRocket.__dict__.pop("_sa_instance_state")
                queryRocket.__dict__.pop('id')
                query.launch_rocket = [queryRocket.__dict__]"""
            query.__dict__.pop("_sa_instance_state")
            return query.__dict__, 200
        else:
            return None, 404
    except InvalidRequestError:
        log().error("InvalidRequestError")
        return None, 400


def Create(cond):
    log().debug(cond)
    querydict = {}
    querydict, isMatch = checkDictKeyMatchArray(modelKey, cond)
    if not isMatch:
        return None, 400

    if "pair_order" in querydict:
        pair = querydict.pop('pair_order')
        pair = list(map(int, pair.split(',')))
        for values in pair:
            createMission = Missions(**querydict, pair_order=values)
            try:
                db_session.add(createMission)
                db_session.commit()
            except:
                log().error("Unable to add mission with pair order in " + str(values))
                return 400
        return 200

    else:
        createMission = Missions(**querydict)
        try:
            db_session.add(createMission)
            db_session.commit()
            return 200
        except InvalidRequestError:
            log().error("Unable to create mission data")
            return 400
        except IntegrityError:
            log().error("Foreign key not found")
            return 400


def Patch(content):
    try:
        if 'id' not in content:
            return None, 400
        cid = content.pop('id')
        querydict, isMatch = checkDictKeyMatchArray(modelKey, content)
        if not isMatch:
            return None, 400
        query = Missions.query.filter_by(id=cid).one_or_none()
        if query is not None:
            
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
        toDel = Missions.query.filter_by(id=id).first()
        if toDel is not None:
            db_session.delete(toDel)
            db_session.commit()
            return 200
        else:
            return 400
    except InvalidRequestError:
        log().error("Unable to delete data")
        return 400