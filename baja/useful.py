'''
utils
pre/post function wrappers
serialize/deserialize functions
'''
import config
import flask
import functools
import jwt
import time
from flask import request
from passlib.hash import pbkdf2_sha512

def authorized(f):
    @functools.wraps(f)
    def _wrapped(*args, **kwargs):
        # verify token
        token = request.headers.get('AUTHORIZATION','')
        token = token.split('Bearer ') or ''
        if len(token) == 1:
            return flask.abort(401)
        try:
            decoded = jwt.decode(token[1], config.SECRET, algorithms=['HS256']) 
        except jwt.exceptions.DecodeError, e:
            # TODO: handle failure
            return flask.abort(401)

        # TODO: check expiration
        now = time.time()
        expires_at = decoded.get('exp')

        res = f(*args, **kwargs)
        return res
    return _wrapped

def encrypt(password):
    return pbkdf2_sha512.encrypt(password)

