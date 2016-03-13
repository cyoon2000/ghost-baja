import config
import os
import pymongo
from passlib.hash import pbkdf2_sha512

def client():
    return pymongo.MongoClient(config.MONGO_HOST, config.MONGO_PORT)

def verify(username, password):
    '''verify user account'''
    try:
        db = client().baja
        user = db.accounts.find_one({'username':username})
    except pymongo.errors.ConnectionFailure, e:
        print 'connection failed'
        verified = False
    hashed = user.get('hashed')
    verified = pbkdf2_sha512.verify(password, hashed)
    return verified

def create_availability(**kwargs):
    db = client().baja
    try:
        result = db.available.insert(kwargs)
    except pymongo.errors.DuplicateKeyError, e:
        return {'rc':-1, 'message':'Entry already created:%s'%(kwargs)}
    return str(result)

def update_availability(**kwargs):
    db = client().baja
    assert kwargs.get('unit_id'), "missing unit id: %s" %(kwargs)
    try:
        update = db.available.update(kwargs)
    except pymongo.errors.DuplicateKeyError, e:
        return {'rc':-1, 'message':'Entry already created:%s'%(kwargs)}
    return str(update)

