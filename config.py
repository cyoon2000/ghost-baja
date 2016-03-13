import os
import os.path

DEBUG = True
BASE_DIR = os.path.abspath(os.path.dirname(__file__)) 
BAJA_ENV = os.environ.get('BAJA_ENV', 'DEV')

# mongo
MONGO_HOST = 'localhost'
MONGO_PORT = 27017

# token secret
SECRET = os.environ.get('JWT_SHARED_SECRET', 'secret')
EXPIRY = 7*86400
