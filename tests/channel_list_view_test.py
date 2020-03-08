# Feature 3: Ability to see a list of channels
import pytest
'''
# channels (outputs only) is a list of dictionaries, 
# where each dictionary contains types { channel_id, name }

# return type: { channels }
# Provide a list of all channels (and their associated details) 
that the authorised user is part of
def channels_list(token):
    return {
        'channel1': [
            {
                'channel_id': 1,
                'name': 'My Channel',
            }
        ],
        'channel2': [
            {
                'channel_id': 2,
                'name': 'My Channel 2'
            }
        ],
    }

def channels_listall(token):
    return {
        'channel1': [
            {
                'channel_id': 1,
                'name': 'My Channel',
            }
        ],
        'channel2': [
            {
                'channel_id': 2,
                'name': 'My Channel 2'
            }
        ],
    }

def channels_create(token, name, is_public):
    return {
        'channel_id': 1,
    }
'''
# returns true if given channel (note, singular) is a valid channel entry.
@pytest.fixture
def is_valid_channel(channel):
    return true

def test_channels_list_valid_channels():
    # assume register is successful.
    my_user = auth_register("bullshit@gmail.com", "1248901ha", "Tim", "Fan")
    # view the channel list that i am authorized to view.
    my_channels_list = channels_list(my_user['token'])
    for channel in my_channels_list:
        assert is_valid_channel(channel) == true

