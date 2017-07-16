import json
import requests

_USERS_DATABASE = {
                   'test_user': {
                                 'client_id': '5967b7a2ec135e279d8b4d68',
                                 'client_secret': 'D5Hf2iFdwWXinNQifIkAAjt0mcDiB',
                                 'username': 'pedrorjorge@hotmail.com',
                                 'password': '1qaz2wsX',
                                 }
                   }

def __get_user_oauth_values(user_name):
    return _USERS_DATABASE[user_name]

def oauth_authentication(user_name, auth_scope='read_station'):
    user_oauth_values = __get_user_oauth_values(user_name)
    user_oauth_values.update({
                              'scope': auth_scope,
                              'grant_type': 'password',
                              })
    auth_response = requests.post('https://api.netatmo.com/oauth2/token', data=user_oauth_values)
    if auth_response.status_code == 200:
        response_body = json.loads(auth_response.text)
        print response_body #{u'access_token': u'5967b7742b2b4649358b5bb9|3848526c2bcd34117eb892779dc212a8', u'scope': [u'read_station'], u'expires_in': 10800, u'expire_in': 10800, u'refresh_token': u'5967b7742b2b4649358b5bb9|f440027cc3422ffcab0d5c0fb9e9ff6b'}

    else:
        raise Exception(u'Ups... something is wrong: %s' % json.loads(auth_response.text)['error'])
    
if __name__ == "__main__":
    oauth_authentication('test_user')
    