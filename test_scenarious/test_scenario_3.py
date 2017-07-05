from test_config import *
from test_common import *


def test_bubbles_viewed():

    devId = 'TC_3'

    '''
    Check if shared effects exists in a pack. First pack becomes totally viewed
    !!! exclude influence of featured variables
    '''

    # get sharet effects count based on evn variables
    env_vars = awsclient.get_environment_variable()
    shared_to_mix = env_vars['MAX_SHARED_EFFECTS_TO_MIX'] if ('MAX_SHARED_EFFECTS_TO_MIX' in env_vars) else 1

    # delete test id from dB
    dbclient.delete_key(devId)

    # get first bubble pack
    effects = apiclient.effects_recommended(devId)

    # check if devId has been created in DB
    assert 'generatedEffects' in dbclient.select_item(devId).keys(), '%s hasn\'t  been created in DB' % devId

    # create bubbleViewed data and send the request
    effect_timestamps = [(effect.id, millis(dt)) for effect in effects]
    apiclient.send_viewed_effects(devId, effect_timestamps)

    # create bubblesShared data and send the request, save shared effects ids
    effect_timestamps = [(effect.id, millis(dt)) for effect in effects[:10]]
    apiclient.send_shared_effects(devId, effect_timestamps)
    shared_ids = set([(effect.id, 'SHARED') for effect in effects[:10]])

    # get tommorow bubble pack
    new_effects = apiclient.effects_recommended(devId, now=millis(tomm))

    # get tomorrow ids
    new_ids = set([(effect.id, effect.source) for effect in new_effects])

    # check if new pack contains shared effects ids
    assert(len(new_ids.intersection(shared_ids))) == shared_to_mix, 'Pack\'s hasn\'s required shared effect\'s ids'

if __name__ == '__main__':
    test_bubbles_viewed()
