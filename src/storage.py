'''
# typical use case, say in auth.py (EXAMPLE!!!)
import storage
def auth_register(email,password,name_first,name_last):
    u_id = generate_u_id()                  # "unique" u_id.
    token = generate_token()                # "unique" token.
    handle = generate_handle()              # "unique" handle.
    permission_id = DEFAULT_PERM_ID         # check spec for this i guess.
    encrypted_password = encrypt(password)

    # storage.add_user() is what calls storage.load_user_all() and storage.save_user_all().
    storage.add_user(name_first,name_last,email,encrypted_password,token,u_id,handle,permission_id)
    return {
        'u_id': u_id,
        'token': token,
    }
'''

import json

################################################################################
# FUNCTIONS FOR CREATING, SAVING, AND LOADING DATABASES.
################################################################################

'''
database initialization.
'''
# creates new empty database, stored in json files.
def new_storage():
    user_all = {}
    channel_all = {}
    user_active = {}
    save_user_active(user_active)
    save_user_all(user_all)
    save_channel_all(channel_all)

'''
database of all registered users.
'''
# loads and returns locally stored user_all database.
### user_all.json is a dictionary indexed by u_id.
### user_all['u_id1'] is a dictionary of information unique to the user with u_id 'u_id1'.
### the keys in a user dictionary are:
### 'name_first','name_last','email','encrypted_password','token','u_id'.
def load_user_all():
    with open("user_all.json", "r") as FILE:
        user_all = json.load(FILE)
        return user_all

# saves to locally stored user_all database.
def save_user_all(user_all):
    with open("user_all.json", "w") as FILE:
        json.dump(user_all, FILE)
        return

'''
database that records which users are active (logged in).
'''
# load the file of the users who logged in 
### user_active.json is a dictionary indexed by token.
### user_active['token1'] is a boolean.
### if user_active['token1'] == True, then the user with token 'token1' is logged in.
def load_user_active():
    with open('user_active.json','r') as FILE:
        active = json.load(FILE)
        return active

def save_user_active(user_active):
    with open('user_active.json','w') as FILE:
        json.dump(user_active,FILE)

# would add the user who logged in 
### perhaps activate_user(token) makes more sense.
def active_user(token):
    user_active = load_user_active()
    user_active[token] = True
    save_user_active(user_active)

def unactivate(token):
    user_active = load_user_active()
    del user_active[token]
    save_user_active(user_active)

'''
database of all channels.
'''  
# loads and returns locally stored channel_all database.
### channel_all.json is a dictionary indexed by channel_id.
### channel_all['channel_id1'] is a dictionary of information unique to the user with channel_id 'channel_id1'.
### the keys in a channel dictionary are:
### 'channel_id','channel_name','owner_members_list','all_members_list','messages_list','standup'.a
def load_channel_all():
    with open("channel_all.json", "r") as FILE:
        channel_all = json.load(FILE)
        return channel_all

# saves to locally stored channel_all database.
def save_channel_all(channel_all):
    with open("channel_all.json", "w") as FILE:
        json.dump(channel_all, FILE)
        return

################################################################################
# FUNCTIONS FOR INTERACTING WITH DATABASES.
################################################################################

'''
functions for interacting with user_all
'''
# adds user to database given email, password, name_first, name_last.
def add_user(name_first, name_last, email, encrypted_password, token, u_id):
    user_all = load_user_all()
    # generate a user dictionary unique to the given user.
    user_data = {}
    user_data['name_first'] = name_first
    user_data['name_last'] = name_last
    user_data['email'] = email
    user_data['encrypted_password'] = encrypted_password
    user_data['token'] = token
    user_data['u_id'] = u_id
    # user_data['handle'] = handle
    # user_data['permission_id'] = permission_id
    # recall that each u_id is unique.
    user_all[u_id] = user_data
    save_user_all(user_all)
    return


def add_member(token, channel_id):
    channel_all = load_channel_all()
    channel_all[channel_id]['member'].append(token)
    save_channel_all(channel_all)

def add_channel(token, channel_id,name, is_public):
    channel = {}
    member = []
    channel_all = load_channel_all()
    channel['owner'] = token
    member.append(token)
    channel['name'] = name
    channel['access'] = is_public
    channel['member'] = member
    channel['messages'] = []
    channel_all[channel_id] = channel
    save_channel_all(channel_all)

