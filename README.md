
## Setup

**mongo**  
brew install mongodb
https://docs.mongodb.org/master/tutorial/install-mongodb-on-os-x/

`mongod` to start  
`mongo` to connect

for setup  
`use baja`  
`db.createCollection('available')`  
`db.createCollection('accounts')`  

**python**  
https://www.python.org/ftp/python/2.7.11/python-2.7.11-macosx10.6.pkg

**virtualenv**  
`pip install virtualenv`  
from repo:  
`virtualenv env`  
`source env/bin/activate`    

**python packages**  
`pip install -r requirements.txt`

**run.py**  
`source env/bin/activate`  
`export PYTHONPATH=.`  
`python run.py`  
defaults to localhost:5000  

## Baja
REST service for availability table
