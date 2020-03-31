
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

def handle(fname, lname):
    return fname+lname

def token(fname, lname):
    return lname+fname

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
    u_id = helper.u_id()
    storage.add_user(name_first, name_last, email, password, token(name_first,name_last), u_id,handle(name_first,name_last))
    # print(storage.load_user_all())
    
    return {
        'u_id':u_id ,
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
    data = storage.load_user_active()
    if token in data:
        storage.unactivate(token)
        return True
    raise Exception
    # return False