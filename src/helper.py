import re
import error
from random import randint
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
    if data[channel_id]['access'] == "False": raise error.AccessError
def get_id(token,data):
    x = [i for i in data if data[i]['token'] == token]
    return x[0]

def u_id():
    return randint(0,500)

def channel_id():
    return randint(0,500)

# make it 
    