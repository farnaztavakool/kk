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