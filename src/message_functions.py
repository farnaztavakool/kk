import storage
import helper
from error import InputError, AccessError
from datetime import datetime
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
  

    message_data = {
        'message_id': message_id,
        'u_id':u_id,
        'reacts': False,
        'is_pinned': False,
        'message_text': message,
    }
    
    storage.add_message(message_data, channel_id)
    # channel['messages_list'].prepend(message_data)
    return {'message_id': message_id} 


# WHY DO THEY NOT INPUT THE CHANNEL_ID REEE.
def message_pin(token,message_id):
    channels_all = storage.load_channel_all()
    message = helper.get_message_dictionary(message_id,channels_all)
    if message['is_pinned'] == True:
        raise InputError()
    message['is_pinned'] = True
    storage.save_channel_all(channels_all)
    return {}

def message_unpin(token,message_id):
    channels_all = storage.load_channel_all()
    message = helper.get_message_dictionary(message_id,channels_all)
    if message['is_pinned'] == False:
        raise InputError()
    message['is_pinned'] = False
    storage.save_channel_all(channels_all)
    return {}

def message_remove(token,message_id):
    channels_all = storage.load_channel_all()
    messages = helper.get_messages_list_containing_message(message_id,channels_all)
    message = helper.get_message_dictionary(message_id,channels_all)
    ### ERROR: message no longer exists.
    if message == {}:
        raise InputError()
    # remove message from the messages list.
    messages.remove(message)
    storage.save_channel_all(channels_all)
    return {}

def message_edit(token,message_id,message):
    channels_all = storage.load_channel_all()
    message_dict = helper.get_message_dictionary(message_id,channels_all)
    message_dict['message_text'] = message 
    storage.save_channel_all(channels_all)
    return {}

def message_sendlater(token, channel_id, message, time_sent):

    data = storage.load_channel_all()
    user_data = auth.get_data()
    helper.check_access(u_id,data,channel_id)
    u_id = helper.get_id(token, user_data)

    message_id = helper.channel_id()
    
    # Channel ID is not a valid channel
    if not helper.valid_channel_id(channel_id, data):
        raise InputError('Channel id is not a valid channel')

    # helper.check_access(u_id,data, channel_id)
    if len(message) > 1000:
        raise InputError("Message should be under 1000 characters.")

    now = datetime.now()
    current_time = datetime.timestamp(now)
    if time_sent < current_time:
        raise InputError('The time entered is a time in the past')


    message_data = {
        'message_id': message_id,
        'u_id':u_id,
        'reacts': False,
        'is_pinned': False,
        'message_text': message,
    }
    
    time = time_sent - get_timestamp()
    timer = threading.Timer(interval, storage.add_message(message_data, channel_id), \
                            [message_data, channel_id])
    timer.start()


    return {'message_id': message_id} 



