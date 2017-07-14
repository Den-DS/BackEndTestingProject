from test_common import *


def test_get_new_bubbles_tomorrow():
    '''
    Delete devId if exists, request bubbles as today, send them as viewed, request bubbles as tomorrow.
    '''

    devId = 'TC_1'

    # Clear DB, get 1st request, check if new entry with test devID has been created
    effects = initiate_req(devId)

    # create bubbleViewed data and send the request
    effect_timestamps = [(effect.id, millis(dt)) for effect in effects]
    apiclient.send_viewed_effects(devId, effect_timestamps)

    # take bubbles_sources in  new pack
    new_sources = set([effect.source for effect in effects])

    # check if 2 lists has the same ids
    assert(len(new_sources.intersection('NOT_VIEWED')) == 0), 'Pack\'s have OLD effects'

if __name__ == '__main__':
    test_get_new_bubbles_tomorrow()