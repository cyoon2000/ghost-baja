import json
import jwt
import time
from baja import app
# circular
# see flask http://flask.pocoo.org/docs/0.10/patterns/packages/
from baja import useful
from baja import model
from baja import validators
from flask import jsonify, request
from werkzeug.datastructures import MultiDict

@app.route('/')
def hello():
    return 'foo'

@app.route('/auth', methods=['POST'])
def check_auth():
    username = request.form['username']
    password = request.form['password']
    verified = model.verify(username, password)
    if not verified:
        abort(501)
    # generate token
    secret = app.config['SECRET']
    payload = {
        'iss':request.host,
        'iat':int(time.time()),
        'exp': time.time() + app.config['EXPIRY']
    }
    encoded = jwt.encode(payload, secret, algorithm='HS256')

    return jsonify(token=encoded)

@app.route('/freebusy', methods=['POST', 'PUT'])
@useful.authorized
def freebusy():
    '''Admin from calendar
    POST initial creation 
    PUT update
    '''
    # TODO: validation, probably wtf-forms lib
    entry = request.get_json()
    form = validators.AvailableForm(data=entry, csrf_enabled=False)
    if not form.validate():
        print 'errors:%s'%(form.errors)
        return jsonify(rc=-1, message=form.errors)
    if request.method == 'POST':
        _id = model.create_availability(**entry)
    elif request.method == 'PUT':
        _id = model.update_availability(**entry)
    return jsonify(rc=0, _id=_id)

@app.route('/delete/<unit_id>/')
@useful.authorized
def delete():
    '''stub for removing availability'''
    pass

@app.route('/available/<unit_id>/')
@useful.authorized
def available(unit_id):
    '''stub for availability search'''
    pass

