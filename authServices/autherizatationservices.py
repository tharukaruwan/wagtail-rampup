def userAuthorization(tocken,id):
    user_id=''
    try:
        user_id=tocken["user_id"]
    except:
        user_id=''
    if user_id=='' or user_id!=id:
        return False
    return True

def orderViewAuthorization(tocken,order):
    user_id=''
    try:
        user_id=tocken["user_id"]
    except:
        user_id=''
    if user_id=='' or user_id!=order["customer"]:
        return False
    return True