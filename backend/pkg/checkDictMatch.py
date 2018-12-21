from pkg.logger import get_logger as log

def checkDictKeyMatchArray(arrays, dicts):
    querydict = {}
    for key in arrays:
        if key in dicts:
            querydict[key] = dicts[key]
            del dicts[key]
    if dicts:
        log().withPrefix("[dict]").debug(dicts)
        return None, False
    return querydict, True