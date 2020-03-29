import re
import error
from random import randint
import datetime
def check_email(email):
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if re.search(regex,email): return True
    raise error.InputError
        # raise error.InputError

def check_email_exist(email,data):
    if any([True for i in data if data[i]['email'] == email ]):
        raise error.InputError
    

def check_name(fname,lname):
    if len(fname) >50 or len(lname) > 50: raise error.InputError
    return True

def check_pass(password):
     if len(password) < 6: raise error.InputError
     return True

def check_channel(channel_id,data):
    if channel_id in data: return True
    raise error.InputError

def check_user(u_id,data):
    if u_id in data: return True
    raise error.InputError

def check_access(u_id, data, channel_id):
    if any([i for i in data[channel_id]['member'] if i['u_id'] == u_id]): return True
    if any([i for i in data[channel_id]['owner'] if i['u_id'] == u_id]): return True
    raise error.AccessError

def check_channel_name(name):
    if len(name) > 20: error.InputError

def check_public_channel(data,channel_id):
    if data[channel_id]['access'] == False: raise error.AccessError
# usage: 
# user_all_data = auth.get_data()
# u_id = helper.get_id(token,user_all_data)
def get_id(token,data):
    x = [i for i in data if data[i]['token'] == token]
    return x[0]

def u_id():
    return randint(0,500)

def channel_id():
    return randint(0,500)

'''
time helper functions.
'''
# returns current time as a python **datetime** object (note: NOT a Unix timestamp).
def get_current_time_as_datetime():
    return datetime.datetime.now()

# converts given python datetime object to a Unix timestamp.
def convert_datetime_to_unix_timestamp(datetime_object):
    # don't bother understanding this code LOL. idek.
    return datetime_object.replace(tzinfo=timezone.utc).timestamp()

# returns current time as a Unix timestamp.
def get_current_time_as_unix_timestamp():
    current_time_as_datetime = get_current_time_as_datetime()
    current_time_as_unix_timestamp = convert_datetime_to_unix_timestamp(current_time_as_datetime)
    return current_time_as_unix_timestamp

'''
message helper functions
'''

# finds and returns message dictionary corresponding to given message_id.
def get_message_dictionary(message_id):
    channels_all = storage.load_channel_all()
    # find the message dictionary with message_id message_id.
    for channel in channels_all:
        messages = channel['messages']
        for message in messages:
            if message['message_id'] == message_id:
                return message
    return {}
# finds and returns messages dictionary that contains the message with given message_id.
def get_messages_list_containing_message(message_id):
    channels_all = storage.load_channel_all()
    # find the message dictionary with message_id message_id.
    for channel in channels_all:
        messages = channel['messages']
        for message in messages:
            if message['message_id'] == message_id:
                return messages
    return {}
# make it 
    