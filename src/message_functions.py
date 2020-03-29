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
    message = helper.get_message_dictionary(message_id)
    if message['is_pinned'] == True:
        raise InputError()
    message['is_pinned'] = True
    return {}

def message_unpin(token,message_id):
    message = helper.get_message_dictionary(message_id)
    if message['is_pinned'] == False:
        raise InputError()
    message['is_pinned'] = False
    return {}

def message_remove(token,message_id):
    messages = helper.get_messages_list_containing_message(message_id)
    message = helper.get_message_dictionary(message_id)
    ### ERROR: message no longer exists.
    if message == {}:
        raise InputError()
    # remove message from the messages list.
    messages.remove(message)
    return {}

def message_edit(token,message_id,message):
    message_dict = helper.get_message_dictionary(message_id)
    message_dict['message_text'] = message
    return {}