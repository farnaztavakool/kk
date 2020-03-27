'''
# EXAMPLE IMPLMENTATION OF auth.py !!!
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
import hashlib
import storage
import helper
import error

# creating the database
def get_data():
    try:
        data = storage.load_user_all()
    except Exception:
        storage.new_storage()
        data = storage.load_user_all()
    return data

   
    
    # storage.new_storage()


def uid(name):
    return name

def token(fname, lname):
    return fname+lname

def encrypt_pass(password):
    
    return hashlib.sha256(password.encode()).hexdigest()
    
# fix using same emails
def auth_register(email, password, name_first, name_last):
    data = get_data()
    helper.check_email(email)
    helper.check_email_exist(email, data)
    helper.check_name(name_first, name_last)
    helper.check_pass(password)
    password = encrypt_pass(password)
    storage.add_user(name_first, name_last, email, password, token(name_first,name_last), uid(name_first))
    print(storage.load_user_all())
    return {
        'u_id': uid(name_first),
        'token':token(name_first, name_last)
    }
    
def auth_login(email, password):
    helper.check_email(email)
    data = get_data()
   
    
    user = [i for i in data if data[i]['email'] == email]
    if user:
        password = encrypt_pass(password)
        if data[user[0]]['encrypted_password'] == password:
            storage.active_user(data[user[0]]['token'])
            print(storage.load_user_active())
            return {
                'u_id': data[user[0]]['u_id'],
                'token':data[user[0]]['token']
            }
        raise error.InputError
    raise error.InputError


def auth_logout(token):
    data = get_data()
    if token in data:
        storage.unactivate(token)
        return True
    return False