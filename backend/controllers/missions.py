from sqlalchemy.exc import InvalidRequestError, IntegrityError
from config.DBindex import db_session
from models.mission import Missions, MissionClientOrderRelate
from models.order import ClientOrders, MissionOrders
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
        query = Missions.query.filter_by(id=cond).one_or_none()
        if query is not None:
            query.__dict__.pop("_sa_instance_state")
            data = query.__dict__

            queryPairOrder = MissionClientOrderRelate.query.filter_by(mission_id=cond).all()
            qdataDict = []
            for qdata in queryPairOrder:
                clientOrder = ClientOrders.query.filter_by(id=qdata.clientOrder_id).one_or_none()
                clientOrder = clientOrder.__dict__
                clientOrder.pop("_sa_instance_state")
                qdataDict.append(clientOrder)

            data['pair_order'] = qdataDict
            return data, 200
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
            if "pair_order" in querydict:
                pair = list(map(int, querydict["pair_order"].split(',')))
                relate = MissionClientOrderRelate.query.filter_by(mission_id=query.id).all()
                qPair = []
                for data in relate:
                    qPair.append(data.clientOrder_id)

                for toDel in list(set(qPair) - set(pair)):
                    m = MissionClientOrderRelate.query.filter_by(mission_id=query.id, clientOrder_id=toDel).one()
                    db_session.delete(m)
                    
                for toAdd in list(set(pair) - set(qPair)):
                    createRelate = MissionClientOrderRelate(mission_id=query.id, clientOrder_id=toAdd)
                    db_session.add(createRelate)

                try:
                    db_session.commit()
                except:
                    log().error("Unable to patch mission client order relate ")
                    return 400

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
            delRelate = MissionClientOrderRelate.query.filter_by(mission_id=id)
            if delRelate.one_or_none() is not None:
                for data in delRelate.all():
                    db_session.delete(data)
            db_session.commit()

            delRelate = MissionOrders.query.filter_by(mission_id=id)
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
        log().error("Unable to delete data")
        return 400