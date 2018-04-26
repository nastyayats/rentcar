import requests
import json

def get_token(scope):
    payload = {'client_id': 'f2a1ed52710d4533bde25be6da03b6e3', 'client_secret': 'ZYDPLLBWSK3MVQJSIYHB1OR2JXCY0X2C5UJ2QAR2MAAIT5Q', 'scope':scope}
    r = requests.post('http://localhost:5000/v1/token', data=json.dumps(payload))
    return r.json().get('auth_token')

