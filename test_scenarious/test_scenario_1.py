"Check if clent gets new set of bubbles next day"
from test_config import *
from test_common import *



def test_get_new_bubbles_tomorrow():
    '''
    Delete devId if exists, request bubbles as today, send them as viewed, request bubbles as tomorrow.
    Env - dev
    '''

    devId = 'TC_1'

    # delete test id from dB
    dbclient.delete_key(devId)

    # get first bubble pack
    effects = apiclient.effects_recommended(devId)

    # check if devId has been created in DB
    assert 'generatedEffectIds' in dbclient.select_item(devId).keys(), '%s hasn\'t  been created in DB' % devId

    # crate bubbleViewed data and send the request
    effect_timestamps = [(effect.id, millis(dt)) for effect in effects]
    apiclient.send_viewed_effects(devId, effect_timestamps)

    # get tommorow bubble pack
    new_effects = apiclient.effects_recommended(devId, now=millis(tomm))

    # take bubles_ids in packs
    old_ids = set([effect.id for effect in effects])
    new_ids = set([effect.id for effect in new_effects])

    # check if 2 lists has the same ids
    assert(len(old_ids.intersection(new_ids)) == 0), 'Pack\'s have similiar ids'
