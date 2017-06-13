from client import *
from datetime import datetime, timedelta


def millis(dt):
    return int(dt.timestamp()*1000)

if __name__ == '__main__':
    dt = datetime.now()
    client = APIClient(envs['dev'])
    effects = client.effects_recommended('fr_test')
    effect_timestamps = [(effect.id, millis(dt)) for effect in effects]
    client.send_viewed_effects('fr_test', effect_timestamps)
    tomm = dt + timedelta(days=1, seconds=1)
    new_effects = client.effects_recommended('fr_test', now=millis(tomm))
    old_ids = set([effect.id for effect in effects])
    new_ids = set([effect.id for effect in new_effects])
    print(len(old_ids.intersection(new_ids)) == 0)
