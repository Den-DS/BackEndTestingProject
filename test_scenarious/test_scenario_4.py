from test_common import *

def test_unseen_bubbles():
    devId = 'TC_4'

    '''
    Delete devId if exists, request bubbles as today, request bubbles as tomorrow.
    !!!!Make script take into account if featured effects changed in DB or delete them
    '''
    #Clear DB, get 1st request, check if new entry with test devID has been created
    effects = initiate_req(devId)

    # get tommorow bubble pack
    new_effects = apiclient.effects_recommended(devId, now=millis(tomm))

    # take bubles_ids in packs
    old_ids = set([effect.id for effect in effects])
    new_ids = set([effect.id for effect in new_effects])

    # check if 2 lists has the same ids
    assert(len(old_ids.intersection(new_ids)) == 10), '2 Packs are not identical'

if __name__ == '__main__':
    test_unseen_bubbles()