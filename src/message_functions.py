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

    current_time = get_timestamp()
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

    # storage.add_message(message_data, channel_id)
    # channel['messages_list'].prepend(message_data)
    return {'message_id': message_id} 

# def message_react(token, message_id, react_id):

#     if not helper.check_valid_id(react_id):
#         raise InputError('react_id is not a valid React ID')
    
s