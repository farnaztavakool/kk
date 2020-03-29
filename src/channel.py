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
   "Make user with user id u_id an owner of this channel"

    # Error check that channel_id refers to a valid channel
    check_channel(channel_id, data)

    # Error check if the user is already an owner
    channel_data = get_data()
    data_user = auth.get_data()
    if data_user[u_id] in channel_data[channel_id]['owner']:
        raise error.InputError
        
    # Add to owner list
    # channel.add_owners(u_id, info['name_first'], info['name_last'], info['profile_img_url'])