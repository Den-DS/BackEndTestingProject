"Check if clent gets new set of bubbles next day"

from apiclient import *
from dbclient import *
from datetime import datetime, timedelta


def millis(dt):
    return int(dt.timestamp()*1000)

def test_bubbles_viewed():

    devId = 'TC_3'
    dt = datetime.now()
    tomm = dt + timedelta(days=1, seconds=1)

# if __name__ == '__main__':
    '''
    Delete devId if exists, request bubbles as today, send them as viewed, request bubbles as tomorrow.
    Env - dev
    '''

    # delete test id from dB
    dbclient = DBClient('devices-dev')
    dbclient.delete_key(devId)

    # get first bubble pack
    apiclient = APIClient(envs['dev'])
    effects = apiclient.effects_recommended(devId)

    # check if devId has been created in DB
    print('Check if devId has been created in DB')
    assert 'generatedEffectIds' in dbclient.select_item(devId).keys(), '%s hasn\'t  been created in DB' % devId

    # create bubbleViewed data and send the request
    effect_timestamps = [(effect.id, millis(dt)) for effect in effects]
    apiclient.send_viewed_effects(devId, effect_timestamps)

    # create bubblesShared data and send the request
    effect_timestamps = [(effect.id, millis(dt)) for effect in effects[:2]]
    apiclient.send_shared_effects(devId, effect_timestamps)

    # get tommorow bubble pack
    new_effects = apiclient.effects_recommended(devId, now=millis(tomm))

    # take bubles_ids in packs
    old_ids = set([effect.id for effect in effects])
    new_ids = set([effect.id for effect in new_effects])

    # check if 2 lists has the same ids
    assert(len(old_ids.intersection(new_ids)) == 2), 'Pack\'s have similiar ids'
