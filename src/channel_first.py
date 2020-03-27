
'''
    channel database would be 
    channle is a dict of channel_ids
    and channle_ids would be a list of the members
    channle {
        channle_id:[
            u_id
        ]
    }
'''

# invite a user with its u_id to the channel
# is there an option to reject or accep the request?
import helper
import storage
import auth
def get_data():
    try:
        data = storage.load_channel_all()
    except Exception:
        storage.new_storage()
        data = storage.load_channel_all()
    return data

def get_channel_id(name):
    return name

def channel_invite(token,channel_id,u_id):
    data_channel = get_data()
    data_user = auth.get_data()
    print(data_channel)
    helper.check_channel(channel_id,data_channel)
    helper.check_user(u_id,data_user)
    if data_user[u_id]['token'] not in data_channel[channel_id]['member']:
        helper.check_access(token, data_channel, channel_id)
        token = data_user[u_id]['token']
        storage.add_member(token, channel_id)


def channel_create(token,name,is_public):
    helper.check_channel_name(name)
    storage.add_channel(token, get_channel_id(name), name,is_public)
    return get_channel_id(name)

def channel_detail(token, channel_id):
    channel_data = get_data()
    helper.check_channel(channel_id, channel_data)
    helper.check_access(token,channel_data, channel_id)
    return {
        "owner":channel_data[channel_id]['owner'],
        "members":len(channel_data[channel_id]['member'])
    }
