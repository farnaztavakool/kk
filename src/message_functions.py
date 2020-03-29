import storage
import helper
from error import InputError, AccessError
import auth 
# creating the database



def message_send(token,channel_id,message):

    data = storage.load_channel_all()
    user_data = auth.get_data()
    u_id = helper.get_id(token, user_data)
    helper.check_access(u_id,data,channel_id)
    message_id = helper.channel_id()
    # helper.check_access(u_id,data, channel_id)
    if len(message) > 1000:
        raise InputError("Message should be under 1000 characters.")
    time_created = helper.get_current_time_as_unix_timestamp()
    message_data = {
        'message_id': message_id,
        'u_id': u_id,
        'reacts': {},
        'is_pinned': False,
        'message_text': message,
        'time_created': time_created,
    }
    
    storage.add_message(message_data, channel_id)
    # channel['messages_list'].prepend(message_data)
    return {'message_id': message_id} 

# WHY DO THEY NOT INPUT THE CHANNEL_ID REEE.
def message_pin(token,message_id):
    channels_all = storage.load_channel_all()
    # find the message dictionary with message_id message_id.
    # OH GOD OH FUCK WHAT AM I WRITING. (wait its not that bad).
    for channel in channels_all:
        messages = channel['messages']
        for message in messages:
            if message['message_id'] == message_id:
                if message['is_pinned'] == True:
                    raise InputError()
                message['is_pinned'] = True
    return {}

def message_unpin(token,message_id):
    channels_all = storage.load_channel_all()
    # find the message dictionary with message_id message_id..
    for channel in channels_all:
        messages = channel['messages']
        for message in messages:
            if message['message_id'] == message_id:
                if message['is_pinned'] == False:
                    raise InputError()
                message['is_pinned'] = False
    return {}
