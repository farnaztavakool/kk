import storage
import helper 
from error import InputError

def admin_userpermission_change(token,u_id,permission_id):
    user_all = storage.load_user_all()
    if u_id not in user_all:
        raise InputError()
    user = user_all[u_id]
    # if not valid_perm_id(permission_id)
    user['permission_id'] = permission_id
    storage.save_user_all(user_all)
    return {}