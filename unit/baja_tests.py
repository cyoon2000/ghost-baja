import baja
import datetime
import pymongo
import requests
import time
import unittest

from baja import model


class TokenTestCase(unittest.TestCase):
    def test_get_auth(self):
        response = requests.post('http://localhost:5000/auth',
            data={'username':'faker', 'password':'faker'})
        token = response.json()
        token = token.get('token')
        self.assertTrue(token, 'Failure to generate token')

    def test_create_availability(self):
        mock = {
            'unit_id':'20160329:20160415:bajapete41',
            'from_date':time.mktime(datetime.datetime(2016,3,29).timetuple()),
            'start_date':time.mktime(datetime.datetime(2016,4,15).timetuple()),
            'calendar_id':'gcal_bajapete_41',
            'room_type':'casita',
            'capacity':10,
            'status':'hold',
            'updated_by':'test',
            'updated_date':time.time(),
        }

        response = requests.post('http://localhost:5000/auth',
            data={'username':'faker', 'password':'faker'})
        token = response.json()
        token = token.get('token')
 
        headers = {'Authorization':'Bearer %s'%(token)}
        response = requests.post('http://localhost:5000/freebusy',
            json=mock,
            headers=headers)

        _id = response.json().get('_id')
        self.assertTrue(_id)

        # cleanup
        db = model.client().baja
        db.available.remove({'_id':_id})

if __name__ == '__main__':
    unittest.main()
