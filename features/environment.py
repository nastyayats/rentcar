from tokens import *


client_id = 'f2a1ed52710d4533bde25be6da03b6e3'
client_secret = 'ZYDPLLBWSK3MVQJSIYHB1OR2JXCY0X2C5UJ2QAR2MAAIT5Q'


def before_feature(context, feature):
    if 'cars' in feature.tags:
        response_with_r_token = send_token_generation_request(prepare_token_payload(client_id, client_secret, 'R'))
        response_with_w_token = send_token_generation_request(prepare_token_payload(client_id, client_secret, 'W'))
        context.r_token = response_with_r_token.json().get('auth_token')
        context.w_token = response_with_w_token.json().get('auth_token')
