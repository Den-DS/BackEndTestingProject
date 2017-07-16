from test_common import *
from tools.adminAPI import get_featured


def test_current_featured():
    '''
    Delete devId if exists, request bubbles as today, send them as viewed, request bubbles as tomorrow.
    '''

    devId = 'TC_1'

    # Clear DB, get 1st request, check if new entry with test devID has been created
    effects = initiate_req(devId)

    # crate set with effects' ids and soruces
    effects_sources = set([(effect.id,effect.source) for effect in effects])

    # get featured set
    featured_ls = get_featured()
    featured_effects = set((effect,'FEATURED') for effect in featured_ls)

    # check if total set includes featured set
    assert(featured_effects.issubset(effects_sources)), 'Reccomended bubbles list hasn\'t appropriate number of elemets'


if __name__ == '__main__':
    test_current_featured()