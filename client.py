import requests
import json
from datetime import datetime


envs = {

    'dev':  'https://api-dev.banuba.net',
    'uat':  'https://api-uat.banuba.net',
    'prod': 'https://api.banuba.net'
}


class Effect:

    def __init__(self, effect_id, name):
        self.id = effect_id
        self.name = name

    @staticmethod
    def from_dict(d):
        return Effect(d['id'], d['name'])

    def __str__(self):
        #review this functinon
        return 'Effect(%s)' % (self.id,)



class APIClient:
    '''
    Decsribe behavior as client side (i.e. mobile) would expected to
    '''
    def __init__(self, base_url=envs['dev']):
        self.base_url = base_url

    def effects_recommended(self, dev_id, now=None):
        req = {'dev_id': dev_id}
        if now:
            req['now'] = now
        resp = requests.post(self.base_url + '/v1.0/effects/recommended', data=json.dumps(req))
        effects_dict = json.loads(resp.text)
        effects = [Effect.from_dict(d) for d in effects_dict['effects']]
        return effects

    def send_viewed_effects(self, dev_id, effect_timestamps):
        new_viewed = [{'effectId': effect_id, 'timestamp': ts} for (effect_id, ts) in effect_timestamps]
        req = {
            'updates': {
                dev_id: {
                    'newViewed': new_viewed,
                }
            }
        }
        requests.post(self.base_url + '/v1.0/devices/updateprofile', data=json.dumps(req))
        # return json.loads(resp.text)


