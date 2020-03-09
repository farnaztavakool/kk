# Feature 6: Within a channel, ability to send a message now, or to send a message at a specified time in the future

from datetime import datetime, timedelta
import pytest
import message
import auth
import error
import channel

@pytest.fixture
def authUser():
    message_id = 0
    return auth.auth_register("somebody@gmail.com", "password", "firstName", "lastName")
    
@pytest.fixture
def unAuthUser():
    return auth_register("somebody2@gmail.com", "password", "name1", "name2")
    
# authUser's channel    
@pytest.fixture
def channel_id(request,authUser,unAuthUser):
    channel_1 = channels_create(authUser['token'], 'channel1', True)['channel_id']
    return channel_id

def reset():
    data = getData()
    for channel in data['channel']:
        channel['messages'] = []
        
# Test if a member sends messages    
def test_message_send_valid(authUser, unAuthUser,  channel_1):
    message_send(authUser['token'], channel_id, "Message 1")
    message_send(authUser['token'], channel_id, "Message 2")
    message_send(authUser['token'], channel_id, "Message 3!")
    assert channel_messages(authUser['token'], channel_id, 0)['messages'][0]['message'] == "Message 3!"
    assert channel_messages(authUser['token'], channel_id, 0)['messages'][1]['message'] == "Message 2"
    assert channel_messages(authUser['token'], channel_id, 0)['messages'][2]['message'] == "Message 1"

# Test if an unauthorized member sends messages
def test_message_send_invalid_user(authUser, unAuthUser, channel_1):
    reset()
    
    print(data)
    with pytest.raises(AccessError):
        message_send(unAuthUser['token'], channel_id, "I am invalid")

# Test if message is too long
def test_message_send_invalid_message_length(authUser, unAuthUser, channel_id:
    reset()
    
    with pytest.raises(InputError):
       message_send(authUser['token'], channel_id, "Mess"*5000)
       
# Test if user sends message in the future
def test_message_sendlater_success(authUser, unAuthUser, channel_id):
    timeSent = datetime.datetime.now(datetime.timezone.utc).astimezone().timestamp()+0.1
    message_id = message_sendlater(authUser['token'], channel_id, "Message 4", timeSent)        

# Test if user sends message that is too long in the future
def test_message_sendlater_too_long(authUser, unAuthUser, channel_id):
    timeSent = datetime.datetime.now(datetime.timezone.utc).astimezone().timestamp()+1
    with pytest.raises(ValueError):
        message_sendlater(authUser['token'], channel_id, "Mess"*5000, timeSent)

# Test if unauthorized user sends message in the future
def test_message_sendlater_unauthorized(authUser, unAuthUser, channel_id):
    timeSent = datetime.datetime.now(datetime.timezone.utc).astimezone().timestamp()+1
    with pytest.raises(AccessError):
        message_sendlater(unAuthUser['token'], channel_id, "Message 5", timeSent)
        
# Test if user sends message in the future
def test_message_sendlater_past(authUser, unAuthUser, channel_id):
    timeSent = datetime.datetime.now(datetime.timezone.utc).astimezone().timestamp()-0.5
    with pytest.raises(ValueError):
        message_sendlater(authUser['token'], channel_id, "Message 6", timeSent)

