import json

# creates new empty database, stored in json files.
def new_storage():
    user_all = {}
    channel_all = {}
    save_user_all(user_all)
    save_channel_all(channel_all)

# saves to locally stored user_all database.
def save_user_all(user_all):
    with open("user_all.json", "w") as FILE:
        json.dump(user_all, FILE)
        return

# saves to locally stored channel_all database.
def save_channel_all(channel_all):
    with open("channel_all.json", "w") as FILE:
        json.dump(channel_all, FILE)
        return

# loads and returns locally stored user_all database.
def load_user_all():
    with open("user_all.json", "r") as FILE:
        user_all = json.load(FILE)
        return user_all

# loads and returns locally stored channel_all database.
def load_channel_all():
    with open("channel_all.json", "r") as FILE:
        channel_all = json.load(FILE)
        return channel_all
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
# adds user to database given email, password, name_first, name_last.
def add_user(name_first,name_last,email,encrypted_password,token,u_id,handle,permission_id):
    user_all = load_user_all()
    # generate a user dictionary unique to the given user.
    user_data = {}
    user_data['name_first'] = name_first
    user_data['name_last'] = name_last
    user_data['email'] = email
    user_data['encrypted_password'] = encrypted_password
    user_data['token'] = token
    user_data['u_id'] = u_id
    user_data['handle'] = handle
    user_data['permission_id'] = permission_id
    # recall that each u_id is unique.
    user_all['u_id'] = user_data
    save_user_all(user_all)
    return
