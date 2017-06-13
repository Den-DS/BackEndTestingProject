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


class REQ:

    tomorrow = int((time.time()+86400)*1000)

    def __init__(self, env='dev'):
        self.endpoint = envs[env]
        # self.endpoint = 'https://gda4x1hled.execute-api.us-west-1.amazonaws.com/dev/v4..'
        self.request_data = {"devId": "test_script", "tz": "+00:00"}

    def post_req(self, endpoint=None, request_data=None):
        '''
        Send POST-request using default of custom endpoint and data
        :param endpoint - endpoint to environment
        :param request_data: - post_request_body
        '''

        endpoint = endpoint or self.endpoint
        request_data = request_data or self.request_data
        rs_body = requests.post(endpoint, json.dumps(request_data))
        rs_code = rs_body.status_code
        rs_body = json.loads(rs_body.text)
        return [rs_body, rs_code]

    def post_req_tomorrow(self, endpoint=None, request_data={}):
        '''
        Send POST-request using default of custom endpoint and current_ts+24hours
        :param endpoint - endpoint to environment
        :param request_data: - post_request_body
        '''
        #need modify incoming variables

        self.request_data['now'] = self.tomorrow
        return self.post_req(endpoint, self.request_data)

x = REQ()
print(x.post_req())



