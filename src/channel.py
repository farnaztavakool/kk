import helper
import storage
import auth
import error

def get_data():
    try:
        data = storage.load_channel_all()
    except Exception:
        storage.new_storage()
        data = storage.load_channel_all()
    return data


def channel_addowner(token,channel_id,u_id):
    channel_id = str(channel_id)
    channel_data = get_data()
    # Error check that channel_id refers to a valid channel
    helper.check_channel(channel_id, data)

    # Error check if the user is already an owner
    data_user = auth.get_data()
    if data_user[u_id] in channel_data[channel_id]['owner']:
        raise error.InputError

    # Error if the authorised user is not already a member of the channel

    channel_data = get_data()
    helper.check_channel(channel_id, channel_data)
    helper.check_access(token, channel_data, channel_id)

    # Add to owner list
    # channel.add_owners(u_id, info['name_first'], info['name_last'], info['profile_img_url'])

def channel_remove(token,channel_id,u_id):

    helper.check_access(token,channel_data, channel_id)

    # Add to owner list
    storage.add_owner(u_id, channel_id)


def channel_removeowner(token,channel_id,u_id):
    channel_id = str(channel_id)
    channel_data = get_data()
    # Error check that channel_id refers to a valid channel
    helper.check_channel(channel_id, data)

    # Error check if the user is not an owner
    data_user = auth.get_data()
    if data_user[u_id] not in channel_data[channel_id]['owner']:
        raise error.InputError

    # Error if the authorised user is not already a member of the channel
    helper.check_access(token,channel_data, channel_id)

    storage.remove_owner(u_id, channel_id)

def channels_list(token):
    channel_data = get_data()
    user_data = auth.get_data()
    u_id = helper.get_id(token, user_data)

    channel_list = []

    for channel_id in channel_data:
        for member in channel_data[channel_id]['member']:
            if u_id == member['u_id']:

                channel_list.append({'channel_id' : channel_id, \
                                    'name' :  channel_data[channel_id]['name'])

    return {'channels' : channel_list}


                channel_list.append({'channel_id' : channel_id,'name' :  channel_data[channel_id]['name']})

    return {'channels' : channel_list}


def channels_listall(token):
    "Provide a list of all channels (and their associated details)"

    channel_data = get_data()
    # return channel_data
    # print(channel_data)
    channel_list = []

    for channel_id in channel_data:
        channel_list.append({'channel_id' : channel_id, 'name' : channel_data[channel_id]['name']})

    return {'channels' : channel_list}


