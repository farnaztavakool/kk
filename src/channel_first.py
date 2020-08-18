
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
import error
import datetime
 

def get_data():
    try:
        data = storage.load_channel_all()
    except Exception:
        storage.new_storage()
        data = storage.load_channel_all()
    return data

def get_channel_id():
    return helper.channel_id()

def channel_invite(token,channel_id,u_id):
    u_id = str(u_id)
    channel_id = str(channel_id)
    data_channel = get_data()
    data_user = auth.get_data()
    helper.check_channel(channel_id,data_channel)
    helper.check_user(u_id,data_user)
    if data_user[u_id] not in data_channel[channel_id]['member']:
        helper.check_access(helper.get_id(token,data_user), data_channel, channel_id)
        storage.add_member(u_id, channel_id)


def channel_create(token,name,is_public):
    helper.check_channel_name(name)
    channel_id = get_channel_id()
    storage.add_channel(token, channel_id, name,is_public)

    return channel_id

def channel_detail(token, channel_id):
    channel_data = get_data()
    data = storage.load_user_all()
    helper.check_channel(channel_id, channel_data)
    u_id = helper.get_id(token,data)
    helper.check_access(u_id,channel_data, channel_id)
    return {
        "name":channel_data[channel_id]['name'],
        "owner":channel_data[channel_id]['owner'],
        "members": channel_data[channel_id]['member']
    }

def channel_leave(token,channel_id):
    channel_id = str(channel_id)
    channel_data = get_data()
    user_data = auth.get_data()
    u_id = helper.get_id(token,user_data)
    helper.check_channel(channel_id,channel_data)
    helper.check_access(u_id,channel_data,channel_id)
    storage.remove_member(u_id,channel_id)

def channel_join(token, channel_id):
    channel_id = str(channel_id)
    channel_data = get_data()
    user_data = auth.get_data()
    # if channel_data[channel_id]['access'] == "False" : print("yeet")
    helper.check_channel(channel_id,channel_data)
    helper.check_public_channel(channel_data,channel_id)
    u_id = helper.get_id(token,user_data)
    storage.add_member(u_id,channel_id)
def channel_message(token,channel_id,start):
    channel_id = str(channel_id)
    user_data = auth.get_data()
    u_id = helper.get_id(token, user_data)
    channel_data = get_data()
    helper.check_channel(channel_id, channel_data)
    helper.check_access(u_id, channel_data, channel_id)
    index = start-1
    message = channel_data[channel_id]['messages']
    if start > len(message): raise error.InputError
    message_list = [i for i in message if message.index(i)>= index and message.index(i) <= 50+index]
    if len(message_list) < 50: end = -1
    else: end = 50
    
    return {
        'messages': message_list,
        'start': start,
        'end': end
    }

