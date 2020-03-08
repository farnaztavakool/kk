# Feature 3: Ability to see a list of channels
import pytest
import channels

@pytest.fixture
def get_new_user():
    user = auth_register('bullshit@gmail.com', '1248901ha', 'Tim', 'Fan')
    return (user['u_id'], user['token'])

def test_channels_list_zero_channels(get_new_user):
    # dummy user.
    u_id, token = get_new_user
    # ensure channels list for dummy user only has both channels
    my_channels_list = channels_list(token)
    assert len(my_channels_list) == 0

def test_channels_list_one_channels_none_authorized(get_new_user):
    # dummy user.
    u_id, token = get_new_user
    # create one channels. assumes creates valid channels.
    channel1 = channels_create(token, 'channel1', True)
    # join channel
    channel_join(token, channel1)
    # leave channel.
    channel_leave(token, channel2)
    # ensure channels list for dummy user has no channels.
    my_channels_list = channels_list(token)
    assert len(my_channels_list) == 0

def test_channels_list_one_channels_one_authorized(get_new_user):
    # dummy user.
    u_id, token = get_new_user
    # create one channels. assumes creates valid channels.
    channel1 = channels_create(token, 'channel1', True)
    # join channel
    channel_join(token, channel1)
    # ensure channels list for dummy user has one channels.
    my_channels_list = channels_list(token)
    assert len(my_channels_list) == 1

def test_channels_list_two_channels_both_authorized(get_new_user):
    # dummy user.
    u_id, token = get_new_user
    # create two channels. assumes creates valid channels.
    channel1 = channels_create(token, 'channel1', True)
    channel2 = channels_create(token, 'channel2', True)
    # join both channels.
    channel_join(token, channel1)
    channel_join(token, channel2)
    # ensure channels list for dummy user only has both channels
    my_channels_list = channels_list(token)
    assert len(my_channels_list) == 2

def test_channels_list_two_channels_one_authorized(get_new_user):
    # dummy user.
    u_id, token = get_new_user
    # create two channels. assumes creates valid channels.
    channel1 = channels_create(token, 'channel1', True) 
    channel2 = channels_create(token, 'channel2', True)
    # join both channels.
    channel_join(token, channel1)
    channel_join(token, channel2)
    # leave one channel.
    channel_leave(token, channel1)
    # ensure channels list for dummy user only has that one channel
    my_channels_list = channels_list(token)
    assert len(my_channels_list) == 1

def test_channels_list_two_channels_none_authorized(get_new_user):
    # dummy user.
    u_id, token = get_new_user
    # create two channels. assumes creates valid channels.
    channel1 = channels_create(token, 'channel1', True) 
    channel2 = channels_create(token, 'channel2', True)
    # join both channels.
    channel_join(token, channel1)
    channel_join(token, channel2)
    # leave one channel.
    channel_leave(token, channel1)
    channel_leave(token, channel2)
    # ensure channels list for dummy user only has that one channel
    my_channels_list = channels_list(token)
    assert len(my_channels_list) == 0

