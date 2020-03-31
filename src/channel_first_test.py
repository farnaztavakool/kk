import json
import urllib
import flask # needed for urllib parse
import pytest
import requests
import storage
from helper import get_id
from  auth_test import *

BASE_URL = "http://127.0.0.1:8060"
def create_channel():
    data1 = register_user()['data_register']
    print(data1['token'])
    data = {
        'token': data1['token'],
        'name' : "channel1",
        'is_public': True
    }
    channel_id = json.loads(requests.post(url = f"{BASE_URL}/channel/create",json = data).content)['channel_id']
    return {
        'channel_id':channel_id,
        'owner_data': data1,
        "channel_property": data
    }
# def test_create_channel():
    reset()


def test_empty_arguments_invite():
    reset()
    data = {
        'token':'',
        'u_id':'',
        'channel_id':'',
        
    }
    # channel_id = create_channel()['channel_id']
    with pytest.raises(requests.exceptions.HTTPError):
        requests.post(url = f"{BASE_URL}/channel/invite",json = data).raise_for_status()

def test_empty_arguments_create():
    reset()
    data = {
        "token":"",
        "name" :"",
        "is_public":""
    }
    with pytest.raises(requests.exceptions.HTTPError):
        requests.post(url = f"{BASE_URL}/channel/create",json = data).raise_for_status()

def test_create_arguments():
    reset()
    channel_property = create_channel()['channel_property']
    user_data = storage.load_user_all()
    channel_data = storage.load_channel_all()
    channel_name = list(channel_data.values())[0]['name']
    is_public = list(channel_data.values())[0]['access']
    u_id = list(user_data.values())[0]['u_id']
    owner_uid = get_id(channel_property['token'],user_data)

    assert channel_name == channel_property['name']
    assert owner_uid == u_id
    assert is_public == channel_property['is_public']


def test_channel_detail_success():
    reset()
    channel_data = create_channel()
    # data = storage.load_user_all()
    token = channel_data['channel_property']['token']
    channel_id = channel_data['channel_id']
    data = {
        'token':token,
        'channel_id':channel_id
    }
    data = json.loads(requests.get(url = f"{BASE_URL}/channel/detail",params =data ).content)
    u_id = channel_data['owner_data']['u_id']
    u_id_return = int(data['owner_members'][0]['u_id'])
    assert data['name'] == channel_data['channel_property']['name']
    assert u_id == u_id_return


def test_channel_invite():
    reset()
    channel_data = create_channel()
    token = channel_data['owner_data']['token']
    channel_id = channel_data['channel_id']
    data = {
        "name_first":"elnaz",
        "name_last":"tavakol",
        "email":"elnaz@gmail.com",
        "password":"123456"
    }
    data_register = json.loads(requests.post(url = f"{BASE_URL}/auth/register",json = data).content)
    u_id = data_register['u_id']
    data = {
        "token":token,
        "u_id":u_id,
        "channel_id":channel_id

    }
    requests.post(url = f"{BASE_URL}/channel/invite",json = data)
    data1 = storage.load_channel_all()
    # print(data1[str(channel_id)]['member'][0]["u_id"])
    assert int(data1[str(channel_id)]['member'][0]["u_id"]) == int(u_id)

def test_channel_join():
    reset()
    channel_data = create_channel()
    token = channel_data['owner_data']['token']
    u_id = channel_data['owner_data']['u_id']
    channel_id = channel_data['channel_id']
    data = {
        'token': token,
        'channel_id': channel_id
    }
    requests.post(url = f"{BASE_URL}/channel/join",json = data).raise_for_status()
    data1 = storage.load_channel_all()
    # print(data1[str(channel_id)]['member'][0]["u_id"])
    # print(u_id)
    assert data1[str(channel_id)]['member'][0]["u_id"] == u_id

def test_channel_leave():
    reset()
    channel_data = create_channel()
    token = channel_data['owner_data']['token']
    channel_id = channel_data['channel_id']
    data = {
        'token': token,
        'channel_id': channel_id
    }
    requests.post(url = f"{BASE_URL}/channel/join",json = data).raise_for_status()
    requests.post(url = f"{BASE_URL}/channel/leave",json = data).raise_for_status()


def test_channel_message():
    reset()
    channel_data = create_channel()
    token = channel_data['owner_data']['token']
    channel_id = channel_data['channel_id']
    data = {
        "token": token,
        "channel_id": channel_id,
        "message":"hello there"
    }
    
    m1 = json.loads(requests.post(url = f"{BASE_URL}/message/send",json = data).content)
    data = {
        "token": token,
        "channel_id": channel_id,
        "message":"good morning"
    }
    m2 = json.loads(requests.post(url = f"{BASE_URL}/message/send",json = data).content)
    data = {
        "token": token,
        "channel_id": channel_id,
        "start": 3
    }
    with pytest.raises(requests.exceptions.HTTPError):
        requests.get(url = f"{BASE_URL}/channel/message",params = data).raise_for_status()
    data = {
        "token": token,
        "channel_id": channel_id,
        "start": 1
    }
    message = json.loads(requests.get(url = f"{BASE_URL}/channel/message",params = data).content)
    assert message['messages'][0]['message_id'] == m1['message_id']
    assert message['messages'][1]['message_id'] == m2['message_id']

