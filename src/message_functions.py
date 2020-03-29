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
