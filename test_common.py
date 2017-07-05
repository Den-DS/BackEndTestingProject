from tools.dbclient import DBClient
from tools.apiclient import APIClient
from tools.awsclient import AWSClient
from test_config import *
from datetime import timedelta, datetime

# create DB connection
dbclient = DBClient(test_table)

# create APIClient client
apiclient = APIClient(test_env)

# create AWSClient
awsclient = AWSClient()


dt = datetime.now()
tomm = dt + timedelta(days=1, seconds=1)

def millis(dt):
    return int(dt.timestamp()*1000)