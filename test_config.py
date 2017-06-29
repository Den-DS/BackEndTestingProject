envs = {

    'dev':  'https://api-dev.banuba.net',
    'uat':  'https://api-uat.banuba.net',
    'prod': 'https://api.banuba.net'
}

dbtables = {

    'dev':  'devices-dev',
    'uat':  'devices-uat',
    'prod': 'devices-prod'
}


set_env = 'uat'

test_env = envs[set_env]
test_table = dbtables[set_env]



