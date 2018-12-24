from sqlalchemy.exc import InvalidRequestError, IntegrityError
from config.DBindex import db_session
from models.mission import Missions, MissionClientOrderRelate
from models.order import ClientOrders
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
        data.__dict__.pop("_sa_instance_state")
        data = data.__dict__

        queryPairOrder = MissionClientOrderRelate.query.filter_by(mission_id=data['id']).all()
        qdataDict = []
        for qdata in queryPairOrder:
            clientOrder = ClientOrders.query.filter_by(id=qdata.clientOrder_id).one_or_none()
            clientOrder = clientOrder.__dict__
            clientOrder.pop("_sa_instance_state")
            qdataDict.append(clientOrder)

        data['pair_order'] = qdataDict
        dataDict.append(data)
    return dataDict, 200

def FindOne(cond):
    try:
        if 'create_by' not in cond:
            return None, 400
        createBy = cond.pop('create_by')
        querydict, isMatch = checkDictKeyMatchArray(modelKey, cond)
        if not isMatch:
            return None, 400

        query = Missions.query.filter_by(**querydict, create_by=createBy)
        if query.one_or_none() is not None:
            q = query.all()
            dataDict = []
            for data in q:
                data.__dict__.pop("_sa_instance_state")
                data = data.__dict__

                queryPairOrder = MissionClientOrderRelate.query.filter_by(mission_id=data['id']).all()
                qdataDict = []
                for qdata in queryPairOrder:
                    clientOrder = ClientOrders.query.filter_by(id=qdata.clientOrder_id).one_or_none()
                    clientOrder = clientOrder.__dict__
                    clientOrder.pop("_sa_instance_state")
                    qdataDict.append(clientOrder)

                data['pair_order'] = qdataDict
                dataDict.append(data)
            return dataDict, 200
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
        createMission = Missions(**querydict)
        try:
            db_session.add(createMission)
            db_session.commit()
        except:
            log().error("Unable to add mission")
            return 400
        for values in pair:
            createRelation = MissionClientOrderRelate(mission_id=createMission.id, clientOrder_id = values)
            try:
                db_session.add(createRelation)
                db_session.commit()
            except:
                log().error("Unable to add mission clientOrder relation with id: " + str(values))
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