from sqlalchemy.exc import InvalidRequestError, IntegrityError
from passlib.context import CryptContext
from config.DBindex import db_session
from models.client import Clients
from models.order import ClientOrders
from pkg.logger import get_logger as log
from pkg.checkDictMatch import checkDictKeyMatchArray
from datetime import datetime

pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=30000
)
modelKey = [
    "name",
    "phone",
    "email",
    "is_launch_company",
    "username"
]

def encrypt_password(password):
    return pwd_context.encrypt(password)


def check_encrypted_password(password, hashed):
    return pwd_context.verify(password, hashed)

def FindAll():
    try:
        query = Clients.query.all()
        dataDict = []
        for data in query:
            data.__dict__.pop("_sa_instance_state")
            dataDict.append(data.__dict__)
        return dataDict, 200
    except Exception as e:
        log().error(e.message)
        return None, 404


def FindOne(ids):
    try:
        query = Clients.query.filter_by(id=ids)
        if query.one_or_none() is not None:
            q = query.one_or_none()
            q.__dict__.pop("_sa_instance_state")
            q.__dict__.pop("passwd")
            return q.__dict__, 200
        else:
            return None, 404
    except InvalidRequestError:
        log().error("InvalidRequestError")
        return None, 400

def Login(content):
    try:
        username = content['username']
        passwd = content['passwd']
        query = Clients.query.filter_by(username=username)
        if query.one_or_none() is not None:
            q = query.one_or_none()
            if check_encrypted_password(passwd, q.passwd):
                orders = ClientOrders.query.filter_by(request_by=query.one().id).all()
                q.__dict__.pop("passwd")
                q.__dict__.pop("_sa_instance_state")
                if orders is not None:
                    tmp = []
                    for num in range(len(orders)):
                        tmpDict = orders[num].__dict__
                        tmpDict.pop("_sa_instance_state")
                        tmp.append(tmpDict)
                    resp = q.__dict__
                    resp["orders"] = tmp
                else:
                    resp = {**q.__dict__, "orders": "null"}
                
                return resp, 200
            return None, 401
        else:
            return None, 401
    except InvalidRequestError:
        log().error("InvalidRequestError")
        return None, 400
    except ValueError as e:
        log().error(e)
        return None, 400

def Create(cond):
    passwd = encrypt_password(cond['passwd'])
    cond.pop('passwd')
    queryDict, isMatch = checkDictKeyMatchArray(modelKey, cond)
    if not isMatch:
        return None, 400
    createClients = Clients(**queryDict, passwd=passwd)
    
    try:
        db_session.add(createClients)
        db_session.commit()
        return 200
    except InvalidRequestError:
        log().error("Unable to create data")
        return 400
    except IntegrityError:
        log().error("Foreign key not found")
        return 400


def Patch(content):
    try:
        queryDict, isMatch = checkDictKeyMatchArray(modelKey, content)
        if not isMatch:
            return 400
        query = Clients.query.filter_by(username=queryDict['username']).one_or_none()
        if query is not None:
            for key in queryDict:
                setattr(query, key, queryDict[key])
            db_session.commit()
            return 200
        else:
            return 404
    except InvalidRequestError:
        log().error("Unable to patch data")
        return 400

def Delete(username):
    try:
        toDel = Clients.query.filter_by(username=username).first()
        if toDel is not None:
            db_session.delete(toDel)
            db_session.commit()
            return 200
        else:
            return 400
    except InvalidRequestError:
        log().error("Unable to delete data")
        return 400
