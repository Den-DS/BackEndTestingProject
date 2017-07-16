from test_common import *
from tools.adminAPI import get_next_surprise


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

    # get tommorow bubble pack
    new_effects = apiclient.effects_recommended(devId, now=millis(get_next_surprise(dt)))

    # take bubbles_sources in  new pack
    new_sources = set([effect.source for effect in new_effects])

    # check if 2 lists has the same ids
    assert('NOT_VIEWED' not in new_sources), 'Pack\'s have NOT_VIEWED effects'

def test_get_bubbles_today_again():

    '''
    Delete devId if exists, request bubbles as today, send them as viewed, request bubbles as tomorrow.
    '''

    devId = 'TC_2'

    # Clear DB, get 1st request, check if new entry with test devID has been created
    effects = initiate_req(devId)

    # crate bubbleViewed data and send the request
    effect_timestamps = [(effect.id, millis(dt)) for effect in effects]
    apiclient.send_viewed_effects(devId, effect_timestamps)

    # get today's bubble pack
    new_effects = apiclient.effects_recommended(devId)

    # get bubles_ids in packs
    old_ids = set([effect.id for effect in effects])
    new_ids = set([effect.id for effect in new_effects])

    # get bubles_ids in packs
    old_sources = set([effect.source for effect in effects])
    new_sources = set([effect.source for effect in new_effects])

    # check if 2 lists has the same ids
    assert(len(old_ids.intersection(new_ids)) == 10), 'Pack\'s aren\'t identical, ids do not match'
    assert(old_sources == new_sources), 'Pack\'s aren\'t identical, sources do not match'


def test_unseen_bubbles():
    devId = 'TC_4'

    '''
    Delete devId if exists, request bubbles as today, request bubbles as tomorrow.
    !!!!Make script take into account if featured effects changed in DB or delete them
    '''
    #Clear DB, get 1st request, check if new entry with test devID has been created
    effects = initiate_req(devId)

    # get tommorow bubble pack
    new_effects = apiclient.effects_recommended(devId, now=millis(get_next_surprise(dt)))

    # take bubles_ids in packs
    old_ids = set([effect.id for effect in effects])
    new_ids = set([effect.id for effect in new_effects])

    # check if 2 lists has the same ids
    assert(len(old_ids.intersection(new_ids)) == 10), '2 Packs are not identical'


if __name__ == '__main__':
    test_get_new_bubbles_tomorrow()
    # test_get_bubbles_today_again()
    # test_unseen_bubbles()