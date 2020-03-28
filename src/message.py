import storage
import helper
from error import InputError, AccessError

# creating the database
def get_data():
    try:
        data = storage.load_channel_all()
    except Exception:
        storage.new_storage()
        data = storage.load_channel_all()
    return data

def uid(name):
    return name

def token(fname, lname):
    return fname + lname


def message_send(token,channel_id,message):

    data = get_data()
    user_data = auth.get_data()
    u_id = helper.get_id(token, user_data)

    channel = channel_all[channel_id]
    # we assume channel['messages_list'] is a list of messages. (created in channel_create()).
    ### each message is a dictionary containing the keys:
    ### 'is_reacted','is_pinned','message_text'.
    message_data = {
        'is_reacted': False,
        'is_pinned': False,
        'message_text': message,
    }
    # if (strlen(message) > 1000) raise InputError.
    if len(message_text) > 1000:
        raise InputError("Message should be under 1000 characters.")
    # if (token not in channel_all[channel_id]) raise AccessError.
    helper.check_access(u_id, data, channel_id)
    
    message_id = add_message(u_id, message_text, channel_id)

    # channel['messages_list'].prepend(message_data)
    return {'message_id': message_id} 
