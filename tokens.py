import requests
import json

url = 'http://localhost:5000/v1/token'


def prepare_token_payload(client_id, client_secret, scope):
    return json.dumps({'client_id': client_id, 'client_secret': client_secret, 'scope': scope})


def send_token_generation_request(payload):
    response = requests.post(url, data=payload)
    print('Response to token generation request is received with code {}'
          .format(response.status_code))
    print(response.text)
    return response

