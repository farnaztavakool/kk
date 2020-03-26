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
import storage
import hashlib
import helper

# creating the database
storage.new_storage()

def uid(name):
    return name

def token(fname,lname):
    return fname+lname

def encrypt_pass(password):
    
    return hashlib.sha256(password.encode()).hexdigest()
    

def auth_register(email,password,name_first,name_last):
    data = storage.load_user_all()
    print ([i['email'] for i in data])
    helper.check_email(email,data)
    helper.check_name(name_first,name_last)
    helper.check_pass(password)
    password = encrypt_pass(password)
    storage.add_user(name_first,name_last,email,password,token(name_first,name_last),uid(name_first))
    print(storage.load_user_all())
    return {
        'u_id': uid(name_first),
        'token':token(name_first,name_last)
    }
    