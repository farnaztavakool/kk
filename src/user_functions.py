import storage
import error
import helper

# gets data of a single user identified by u_id from user_all 
# database in storage.py, and returns data as a dictionary
def user_profile(token, u_id):
    user_all = storage.load_user_all()
    # I think this function is correct
    user = {
        'u_id': u_id
        'email': user_all[u_id]['email']
        'name_first': user_all[u_id]['name_first']
        'name_last': user_all[u_id]['name_last']
        'handle_str': user_all[u_id]['token']
    }
    return (user)
    
def user_profile_setname(token, name_first, name_last): 
    user_all = storage.load_user_all()
    u_id = get_u_id_from_token(token)
    user_all[u_id]['name_first'] = name_first
    user_all[u_id]['name_last'] = name_last
    storage.save_user_all(user_all)

def user_profile_setemail(token, email): 

    user_all = storage.load_user_all()
    u_id = get_u_id_from_token(token)
    user_all[u_id]['email'] = name_first
    storage.save_user_all(user_all)

def user_profile_sethandle(token, handle_str): 
    # InputError if length of handle_str invalid
    if len(handle_str) < 2 or len(handle_str) > 20:
        raise error.InputError
    # InputError if handle is taken by another user
    for u_id in user_all[u_id]:
        if handle_str = user_all[u_id]['handle']:
            raise error.InputError
            
    user_all = storage.load_user_all()
    u_id = get_u_id_from_token(token)
    user_all[u_id]['handle'] = handle_str
    storage.save_user_all(user_all)

# should i move this to helper.py and import helper
def get_u_id_from_token(token):
    user_all = storage.load_user_all()
    for u_id in user_all[u_id]:
        if token = user_all[u_id]['token']:
            return u_id
            
        
    

