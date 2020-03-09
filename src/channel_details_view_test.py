# Feature 5: Within a channel, ability to view all messages, view the members of the channel, and the details of the channel

import pytest
import pytest
import message
import auth
from error import AccessError
from error import InputError
import channel
import channels

@pytest.fixture
def authUser():
    message_id = 0
    return auth.auth_register("somebody@gmail.com", "password", "firstName", "lastName")
    
@pytest.fixture
def unAuthUser():
    return auth.auth_register("somebody2@gmail.com", "password", "firstName", "lastName")
    
@pytest.fixture
def channel_id(authUser):
    channel_id = channels.channels_create(authUser['token'], 'channel1', True)['channel_id']
    return channel_id

        
# Test if the channel id is not valid  
def test_channel_id_valid(channel_id):
    with pytest.raises(InputError):
        assert(channel_id >= 1)
    
# test details function if user it not a member of the channel
def test_details_user_member(authUser, channel_id):
    with pytest.raises(AccessError):
        assert(any(channel.channel_details(authUser['token'], channel_id)['all_members']['name_first'] == authUser["firstName"]))

# test if index start is greater than total messages
def test_index_greater(authUser, channel_id):
    with pytest.raises(AccessError):
        assert(channel.channel_messages(authUser['token'], channel_id, 0)['start'] > max(channel.channel_messages(authUser['token'], channel_id, 0)['messages']['message_id']))
        
# test messages function if user is not member of channel
def test_messages_user_member(authUser, channel_id):
    with pytest.raises(AccessError):
        assert(any(channel.channel_messages(authUser['token'], channel_id)['messages']['u_id'] == authUser['u_id']))
        
# test messages function returns 3 elements
def test_messages_return(authUser, channel_id):
    assert(len(channel.channel_messages(authUser['token'], channel_id)) == 3)
    
# test messages function returns -1 in "end" after showing oldest messages
def test_messages_oldest(authUser, channel_id):
    if channel.channel_messages(authUser['token'], channel_id)['messages']['message_id'] == channel.channel_messages(authUser['token'], channel_id)['end']:
        assert (channel.channel_messages(authUser['token'], channel_id)['end'] == -1)
        
# test messages function only displays 50 messages at most
def test_messages_display(authUser, channel_id):
    assert(channel.channel_messages((authUser['token'], channel_id)['start'] + 50) == channel.channel_messages((authUser['token'], channel_id)['end']))
    



 

