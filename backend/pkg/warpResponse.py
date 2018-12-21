from flask import jsonify
from pkg.logger import get_logger as log

responses = {200: "ok", 404: "ResourceNotFound", 400: "InvalidArguments", 401: "Wrong Username or Password"}


def warpResponse(data, respCode=200, message="ok"):
    if respCode in responses:
        if message is "ok":
            message = responses[respCode]
    return jsonify(data=data, code=respCode, message=message)
