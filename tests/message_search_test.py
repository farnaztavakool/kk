from message import message_send
from channels import channels_create
from auth import auth_register
from other import search
import pytest


def messagefunc(message):
    user = auth_register("tavakolfarnaz@gmail.com","0312138261","farnaz","tavakol")
    token = user['token']
    channel = channels_create(token,"test",True)
    cid = channel['channel_id']
    message = message_send(token,cid,message)
    
    mid = message['message_id']
    return {
        'token': token,
        'uid': user['u_id'],
        'mid': mid,
        'cid': cid
    }
# returns the right result
def test_search_message():
    mess = messagefunc("hello world")
    token= mess['token']
    mid = mess['mid']
    result = search(token,"he")
    assert mid == result['messages'][0]['message_id']

# where there is no matching query 
def test_serch_empty():
    mess = messagefunc("hello world")
    token= mess['token']
    result = search(token,"tango")
    assert len(result['messages']) == 0

# returns the right author
def test_search_author():
    mess = messagefunc("hello world")
    token= mess['token']
    uid = mess['uid']
    result = search(token,"he")
    assert uid == result['messages'][0]['u_id']

# send two messages containing the query 
#checks if the functions returns both of them 

def test_mutli_message():
    mess1 = messagefunc("hello world")
    mid1 = mess1['mid']
    cid = mess1['cid']
    token = mess1['token']
    mess2 = message_send(token,cid,"hell got loose")
    mid2 = mess2['message_id']
    result = search(token,"hell")
    res = result['messages']
    check = 0
    for i in range(len(res)):
        if mid2 in res[i].values() or mid1 in res[i].values():
            check+=1 
            
    assert check == 2

    #different channels

def test_differnt_channels():

    mess1 = messagefunc("yo how are you today")
    token = mess1['token']
    ch2 = channels_create(token,"test1",True)
    cid2 = ch2['channel_id']
    mess2 = message_send(token,cid2,"tommorow is better")
    result = search(token,"to")
    res = result['messages']
    check = 0
    mid1 = mess1['mid']
    mid2 = mess2['message_id']
    for i in range(len(res)):
        if mid2 in res[i].values() or mid1 in res[i].values():
            check+=1 

    assert check == 2

