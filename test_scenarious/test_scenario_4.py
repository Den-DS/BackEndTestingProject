"Check if clent gets new set of bubbles next day"
from test_config import *
from test_common import *

def test_unseen_bubbles():
    devId = 'TC_4'

#if __name__ == '__main__':
    '''
    Delete devId if exists, request bubbles as today, request bubbles as tomorrow.
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

    # get tommorow bubble pack
    new_effects = apiclient.effects_recommended(devId, now=millis(tomm))

    # take bubles_ids in packs
    old_ids = set([effect.id for effect in effects])
    new_ids = set([effect.id for effect in new_effects])

    # check if 2 lists has the same ids
    assert(len(old_ids.intersection(new_ids)) == 10), '2 Packs are not identical'
