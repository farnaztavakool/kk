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
    assert payload['email'] == ''
    assert payload['name_first'] == ''
    assert payload['name_last'] == ''
    assert payload['handle_str'] == ''
    
    # Send POST request with user/profile/setname
    response = requests.post(f"{BASE_URL}/user/profile/setname", json = {
        'token' : 'tokenStr'
        'name_first' = 'fName'
        'name_last' = 'lName'
    })
    payload = response.json()
    assert payload['name_first'] == 'fName'
    assert payload['name_last'] == 'lName'
    
    # Send POST request with user/profile/setemail
    response = requests.post(f"{BASE_URL}/user/profile/setemail", json = {
        'token' : 'tokenStr'
        'email' = 'testEmail@hotmail.com'
    })
    payload = response.json()
    assert payload['email'] == 'testEmail@hotmail.com'
    
    # Send POST request with user/profile/sethandle
    response = requests.post(f"{BASE_URL}/user/profile/sethandle", json = {
        'token' : 'tokenStr'
        'handle_str' = 'handleName'
    })
    payload = response.json()
    assert payload['handle_str'] == 'handleName'
    
    # Final attempt to access user/profile
    response = requests.get(f"{BASE_URL}/user/profile")
    payload = response.json()
    assert payload['email'] == 'testEmail@hotmail.com'
    assert payload['name_first'] == 'fName'
    assert payload['name_last'] == 'lName'
    assert payload['handle_str'] == 'handleName'
    
    # Attempt to access users/all
    response = requests.get(f"{BASE_URL}/users/all")
    payload = response.json()
    assert payload['email'] == 'testEmail@hotmail.com'
    assert payload['name_first'] == 'fName'
    assert payload['name_last'] == 'lName'
    assert payload['handle_str'] == 'handleName'

    


