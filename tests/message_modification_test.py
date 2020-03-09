# Within a channel, ability to edit, remove a message

# message_remove
# message_edit

from message import *
from auth import auth_register
from channels import channels_create
from other import search
from error import InputError
import pytest


def message_function(message):
    user = auth_register("hkhkhk999@naver.com","1234yu!","Hailey","Jung")
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

###########################################################
#                  test message_remove                    #
###########################################################

# test if the message is actually removed
# assum that if the message is removed and you search the messagethe return value is 0

def test_message_remove():
    mess = message_function("Hellooo world")
    token = mess['token']
    mid = mess['mid']
    message_remove(token, mid)
    result = search(token, "Hellooo world")
    assert len(result['messages']) == 0

# give error if try to remove a message that does not exist

def test_nonexist_remove():
    mess = message_function("Hellooo world")
    wrong_token = mess['token'] + '7676'
    mid = mess['mid']   
    with pytest.raises(InputError):
        message_remove(wrong_token, mid)
        raise InputError

    
###########################################################
#                  test message_edit                      #
###########################################################

# test if the edited message exists

def test_edit_message():
    mess = message_function("Hellooo world")
    token = mess['token']
    mid = mess['mid']
    b4_edit = search(token, "Hello? This is the edited version")
    assert len(b4_edit['messages']) == 0
    message_edit(token, mid, "Hello? This is the edited version")
    after_edit = search(token,"Hello? This is the edited version")
    assert mid == after_edit['messages'][0]['message_id']

# test if the message before editting is gone
    
def test_before_message():
    mess = message_function("Hellooo world")
    token = mess['token']
    mid = mess['mid']
    b4_edit = search(token, "Hello? This is the edited version")
    assert len(b4_edit['messages']) == 0
    message_edit(token, mid, "Hello? This is the edited version")
    after_edit = search(token,"Hellooo world")
    assert len(after_edit['messages']) == 0