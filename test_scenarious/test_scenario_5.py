from test_config import *
from test_common import *


def test_get_new_bubbles_tomorrow():
    '''
    Delete devId if exists, request bubbles as today, send them as viewed, request bubbles as tomorrow.
    Env - dev
    '''

    devId = 'TC_5'

    # delete test id from dB
    dbclient.delete_key(devId)

    # get first bubble pack
    effects = apiclient.effects_recommended(devId)

    # check if devId has been created in DB
    assert 'generatedEffects' in dbclient.select_item(devId).keys(), '%s hasn\'t  been created in DB' % devId

    # create bubbleViewed data and send the request
    effect_timestamps = [(effect.id, millis(dt)) for effect in effects]
    apiclient.send_viewed_effects(devId, effect_timestamps)

    # get tommorow bubble pack
    new_effects = apiclient.effects_recommended(devId, now=millis(tomm))

    # take bubbles_sources in  new pack
    new_sources = set([effect.source for effect in effects])

    # check if 2 lists has the same ids
    assert(len(new_sources.intersection('NOT_VIEWED')) == 0), 'Pack\'s have OLD effects'

test_get_new_bubbles_tomorrow()
