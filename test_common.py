from tools.dbclient import DBClient
from tools.apiclient import APIClient
from test_config import *
from datetime import datetime

# create DB connection
dbclient = DBClient(test_table)

# create APIClient client
apiclient = APIClient(test_env)

dt = datetime.now()


def millis(dt):
    return int(dt.timestamp()*1000)

def initiate_req(devId):

    # delete test id from dB
    dbclient.delete_key(devId)
    # get first bubble pack
    effects = apiclient.effects_recommended(devId)
    # check if devId has been created in DB
    assert 'generatedEffects' in dbclient.select_item(devId).keys(), '%s hasn\'t  been created in DB' % devId
    return effects
