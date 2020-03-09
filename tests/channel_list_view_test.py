# Feature 3: Ability to see a list of channels
import pytest
import auth
import channels
import channel

@pytest.fixture
def get_new_user():
    user = auth.auth_register('bullshit@gmail.com', '1248901ha', 'Tim', 'Fan')
    return (user['u_id'], user['token'])

'''
testing channels_list() returns the correct number of key/value pairs.
'''

def test_channels_list_zero_channels(get_new_user):
    # dummy user.
    u_id, token = get_new_user
    # ensure channels list for dummy user has no channels.
    my_channels_list = channels.channels_list(token)
    assert len(my_channels_list) == 0

def test_channels_list_one_channels_none_authorized(get_new_user):
    # dummy user.
    u_id, token = get_new_user
    # create one channels. assumes creates valid channels.
    channel1 = channels.channels_create(token, 'channel1', True)
    # join channel
    channel.channel_join(token, channel1['channel_id'])
    # leave channel.
    channel.channel_leave(token, channel2['channel_id'])
    # ensure channels list for dummy user has no channels.
    my_channels_list = channels.channels_list(token)
    assert len(my_channels_list) == 0

def test_channels_list_one_channels_one_authorized(get_new_user):
    # dummy user.
    u_id, token = get_new_user
    # create one channels. assumes creates valid channels.
    channel1 = channels.channels_create(token, 'channel1', True)
    # join channel
    channel.channel_join(token, channel1['channel_id'])
    # ensure channels list for dummy user has one channel.
    my_channels_list = channels.channels_list(token)
    assert len(my_channels_list) == 1


def test_channels_list_two_channels_none_authorized(get_new_user):
    # dummy user.
    u_id, token = get_new_user
    # create two channels. assumes creates valid channels.
    channel1 = channels_create(token, 'channel1', True) 
    channel2 = channels_create(token, 'channel2', True)
    # join both channels.
    channel_join(token, channel1['channel_id'])
    channel_join(token, channel2['channel_id'])
    # leave both channels.
    channel_leave(token, channel1['channel_id'])
    channel_leave(token, channel2['channel_id'])
    # ensure channels list for dummy user has no channels.
    my_channels_list = channels.channels_list(token)
    assert len(my_channels_list) == 0

def test_channels_list_two_channels_one_authorized(get_new_user):
    # dummy user.
    u_id, token = get_new_user
    # create two channels. assumes creates valid channels.
    channel1 = channels.channels_create(token, 'channel1', True) 
    channel2 = channels.channels_create(token, 'channel2', True)
    # join both channels.
    channel.channel_join(token, channel1['channel_id'])
    channel.channel_join(token, channel2['channel_id'])
    # leave one channel.
    channel.channel_leave(token, channel1['channel_id'])
    # ensure channels list for dummy user has one channel.
    my_channels_list = channels.channels_list(token)
    assert len(my_channels_list) == 1

def test_channels_list_two_channels_both_authorized(get_new_user):
    # dummy user.
    u_id, token = get_new_user
    # create two channels. assumes creates valid channels.
    channel1 = channels.channels_create(token, 'channel1', True)
    channel2 = channels.channels_create(token, 'channel2', True)
    # join both channels.
    channel.channel_join(token, channel1['channel_id'])
    channel.channel_join(token, channel2['channel_id'])
    # ensure channels list for dummy user has both channels.
    my_channels_list = channels.channels_list(token)
    assert len(my_channels_list) == 2

'''
testing channels_list() returns the correct key/value pairs.
'''

def test_channels_list_two_channels_both_authorized_ensure_valid_return(get_new_user):
    # dummy user.
    u_id, token = get_new_user
    # create two channels. assumes creates valid channels.
    channel1 = channels.channels_create(token, 'channel1', True)
    channel2 = channels.channels_create(token, 'channel2', True)
    # join both channels.
    channel.channel_join(token, channel1['channel_id'])
    channel.channel_join(token, channel2['channel_id'])
    # ensure channels list for dummy user has both channels.
    my_channels_list = channels.channels_list(token)
    assert my_channels_list['channel1'] == channel1['channel_id']
    assert my_channels_list['channel2'] == channel2['channel_id']

'''
testing channels_listall() returns the correct number of key/value pairs
'''

def test_channels_listall_zero_channels(get_new_user):
    # dummy user.
    u_id, token = get_new_user
    # ensure channels list for dummy user has no channels.
    my_channels_list = channels.channels_list(token)
    assert len(my_channels_list) == 0

def test_channels_listall_one_channels_none_authorized(get_new_user):
    # dummy user.
    u_id, token = get_new_user
    # create one channels. assumes creates valid channels.
    channel1 = channels.channels_create(token, 'channel1', True)
    # join channel
    channel.channel_join(token, channel1['channel_id'])
    # leave channel.
    channel.channel_leave(token, channel2['channel_id'])
    # ensure channels list for dummy user has all channels.
    my_channels_list = channels.channels_listall(token)
    assert len(my_channels_list) == 1

def test_channels_listall_one_channels_one_authorized(get_new_user):
    # dummy user.
    u_id, token = get_new_user
    # create one channels. assumes creates valid channels.
    channel1 = channels.channels_create(token, 'channel1', True)
    # join channel
    channel.channel_join(token, channel1['channel_id'])
    # ensure channels list for dummy user has all channels.
    my_channels_list = channels.channels_listall(token)
    assert len(my_channels_list) == 1


def test_channels_listall_two_channels_none_authorized(get_new_user):
    # dummy user.
    u_id, token = get_new_user
    # create two channels. assumes creates valid channels.
    channel1 = channels_create(token, 'channel1', True) 
    channel2 = channels_create(token, 'channel2', True)
    # join both channels.
    channel_join(token, channel1['channel_id'])
    channel_join(token, channel2['channel_id'])
    # leave both channels.
    channel_leave(token, channel1['channel_id'])
    channel_leave(token, channel2['channel_id'])
    # ensure channels list for dummy user has all channels.
    my_channels_list = channels.channels_listall(token)
    assert len(my_channels_list) == 2

def test_channels_listall_two_channels_one_authorized(get_new_user):
    # dummy user.
    u_id, token = get_new_user
    # create two channels. assumes creates valid channels.
    channel1 = channels.channels_create(token, 'channel1', True) 
    channel2 = channels.channels_create(token, 'channel2', True)
    # join both channels.
    channel.channel_join(token, channel1['channel_id'])
    channel.channel_join(token, channel2['channel_id'])
    # leave one channel.
    channel.channel_leave(token, channel1['channel_id'])
    # ensure channels list for dummy user has all channels.
    my_channels_list = channels.channels_listall(token)
    assert len(my_channels_list) == 2

def test_channels_listall_two_channels_both_authorized(get_new_user):
    # dummy user.
    u_id, token = get_new_user
    # create two channels. assumes creates valid channels.
    channel1 = channels.channels_create(token, 'channel1', True)
    channel2 = channels.channels_create(token, 'channel2', True)
    # join both channels.
    channel.channel_join(token, channel1['channel_id'])
    channel.channel_join(token, channel2['channel_id'])
    # ensure channels list for dummy user has all channels.
    my_channels_list = channels.channels_listall(token)
    assert len(my_channels_list) == 2

'''
testing channels_listall() returns the correct key/value pairs.
'''

def test_channels_listall_two_channels_both_authorized_ensure_valid_return(get_new_user):
    # dummy user.
    u_id, token = get_new_user
    # create two channels. assumes creates valid channels.
    channel1 = channels.channels_create(token, 'channel1', True)
    channel2 = channels.channels_create(token, 'channel2', True)
    # join both channels.
    channel.channel_join(token, channel1['channel_id'])
    channel.channel_join(token, channel2['channel_id'])
    # ensure channels list for dummy user has both channels.
    my_channels_list = channels.channels_listall(token)
    assert my_channels_list['channel1'] == channel1['channel_id']
    assert my_channels_list['channel2'] == channel2['channel_id']
