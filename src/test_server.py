import json
import urllib
import flask # needed for urllib parse
import pytest
import requests
import storage
from login_test import *
# from tests/Integration_Tests import *
BASE_URL = "http://127.0.0.1:8060"
def reset():
    # req = urllib.request.Request(f"{BASE_URL}/workspace/reset",method = 'POST')
    # urllib.request.urlopen(req)  
    storage.new_storage()

def test_register_funcs():

    test_register_works()
    test_register()
    test_password()
    test_long_first_name()
    test_long_last_name()
   


def test_login__funcs():

    test_token()
    test_check_user_email()
    test_server.reset()
    test_user_login_email()
    test_check_unique_token()


def test_logout_funcs():
    test_auth_logout()
    test_unactive_logout()

#     test_register()
    # request 
  
    # data = json.dumps({
    #     'name_first':'Farnaz',
    #     'name_last':'Tavakol',
    #     'email': "elnaztavakol@gmail.com",
    #     "password":'0312138'
    # }).encode('utf_8')
    # req = urllib.request.Request(f"{BASE_URL}/auth/register", data = data,headers = {'Content-Type':'application/json'})
    # result = json.load(urllib.request.urlopen(req))
    # data = json.dumps({
    #     'email' : 'elnaztavakol@gmail.com',
    #     'password' : '0312138'
    # }).encode('utf_8')
    # req = urllib.request.Request(f"{BASE_URL}/auth/login",data = data, headers = {'Content-Type':'application/json'})
    # result1 = json.load(urllib.request.urlopen(req))
    # assert result1['u_id'] == result['u_id']
    # assert result1['token'] == result['token']


# def test_register_url():

#     data = {
#         'email':'',
#         'password':'0312138'
#     }
    
#     with pytest.raises(requests.exceptions.HTTPError):
#         requests.post(url = f"{BASE_URL}/auth/login",json = data).raise_for_status()