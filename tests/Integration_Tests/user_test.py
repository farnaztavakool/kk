import json
import urllib
import flask
import requests

BASE_URL = "http:127.0.0.1:8060"

def test_user_all():
    # Reset
    requests.get(f"{BASE_URL}/workspace/reset")
    
    # Initial attempt to access user/profile
    response = requests.get(f"{BASE_URL}/user/profile")
    payload = response.json()
    assert payload['email'] = ''
    assert payload['name_first'] = ''
    assert payload['name_last'] = ''
    assert payload['handle_str'] = ''
    
    # send POST request with user/profile/setname
    response = requests.post(f"{BASE_URL}/user/profile")
    payload = response.json()
    
    


