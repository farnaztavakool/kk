import json
import urllib
import pytest
import requests
import storage
import helper
# from login_test import *
# from tests/Integration_Tests import *
BASE_URL = "http://127.0.0.1:8060"
def reset():
    # req = urllib.request.Request(f"{BASE_URL}/workspace/reset",method = 'POST')
    # urllib.request.urlopen(req)  
    storage.new_storage()

# sending empty data for parameters

def register_user():
    data = {
        'name_last':'farnaz',
        'name_first':'tavakol',
        'email':'tavakolfarnaz@gmail.com',
        'password':'0312138'
    }
    data_register = json.loads(requests.post(url = f"{BASE_URL}/auth/register",json = data).content)
    return {
        "data":data,
        "data_register":data_register
    }
def test_empty_arguments():

    data = {
        'name_last':'',
        'name_first':'',
        'email':'',
        'password':'0312138'
    }
    
    with pytest.raises(requests.exceptions.HTTPError):
        requests.post(url = f"{BASE_URL}/auth/register",json = data).raise_for_status()

# checks the server send the correct data to the functions
def test_check_argumetns():
    reset()
    data = register_user()['data']
    data_send = storage.load_user_all()
    name_first = list(data_send.values())[0]['name_first']
    name_last = list(data_send.values())[0]['name_last']
    assert data['name_first'] == name_first
    assert data['name_last'] == name_last
    

def test_empty_login():
    reset()
    data = {
        "email":"",
        "password": "0312138"
    }
    with pytest.raises(requests.exceptions.HTTPError):
        requests.post(url = f"{BASE_URL}/auth/login",json = data).raise_for_status()

# loging in with correct data
def test_login_success():
    reset()
    data1 = register_user()['data']
    email = data1['email']
    password = data1['password'] 
    data = {
        "email":email,
        "password":password,
    }
    requests.post(url = f"{BASE_URL}/auth/login",json = data).raise_for_status()

def test_logout_arguments():
    reset()
    data = {
        "token":""
    }
    with pytest.raises(requests.exceptions.HTTPError):
        requests.post(url = f"{BASE_URL}/auth/logout",json = data).raise_for_status()

# loggin out an active member 
def test_logout_sucess():
    reset()
    data1 = register_user()['data']
    email = data1['email']
    password = data1['password'] 
    
    data = {
        "email":email,
        "password":password
    }
    data2 = json.loads(requests.post(url = f"{BASE_URL}/auth/login",json = data).content)
   
    token = data2['token']
    data = {
        "token":token
    }
    requests.post(url = f"{BASE_URL}/auth/logout",json = data).raise_for_status()
