import requests
import json
import time

curr_ts = time.time()

envs = {

    'dev':  'https://api-dev.banuba.net',
    'uat':  'https://api-uat.banuba.net',
    'prod': 'https://api.banuba.net'
}

effects_viewed = {
    "updates": {
        "test_1" : {
            "newViewed" : [
                         {"effectId":"21A204AE853EAA932D84B7053CF8CE6CA7F8835F800F17CE4E84864692B05B2B", "timestamp":curr_ts}
            ]
        }
    }
}

