import requests
import json

id = 'f2a1ed52710d4533bde25be6da03b6e3'
secret = 'ZYDPLLBWSK3MVQJSIYHB1OR2JXCY0X2C5UJ2QAR2MAAIT5Q'
url = 'http://localhost:5000/v1/token'


def get_token(scope):
    payload = {'client_id': id, 'client_secret': secret, 'scope':scope}
    r = requests.post(url, data=json.dumps(payload))
    return r.json().get('auth_token')


# todo: add here functions for tokens testing