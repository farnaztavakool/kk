import storage
import helper
import error

# Users can be removed via API call
# Frontend modified to provide an interface for removal
# Javascript code is consistent with the rest of the frontend in terms of style
# Added UI components are simple, clear and consistent with the rest of the UI

# def get_data():
#     user_all = storage.load_user_all()
# Input error: u_id does not refer to a valid user
# Access error: The authorised user is not an owner of the slackr
def user_remove(token, u_id):
    # Check valid user
    user_all = storage.load_user_all()
    helper.check_user(u_id, user_all)
    # The authorised user is not an owner of the slackr
    t_u_id = str(helper.get_id(token, user_all))
    helper.check_user(t_u_id, user_all) 

    delete = [i for i in user_all if i['u_id'] == u_id]
    user_all[str(u_id)].remove(delete[0])
    storage.save_user_all(user_all)