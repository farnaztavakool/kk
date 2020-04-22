import sys
from json import dumps, dump, load
from flask import Flask, request
from flask_cors import CORS
from error import InputError
import auth
import message_functions
import channel
import channel_first
import user_remove
import user_functions as user
import standup
import reset
import admin
from  check_data_server import *
import password
import threading
import storage



# def defaultHandler(err):
#     response = err.get_response()
#     print('response', err, err.get_response())
#     response.data = dumps({
#         "code": err.code,
#         "name": "System Error",
#         "message": err.get_description(),
#     })
#     response.content_type = 'application/json'
#     return response

APP = Flask(__name__)
CORS(APP)

# APP.config['TRAP_HTTP_EXCEPTIONS'] = True
# APP.register_error_handler(Exception, defaultHandler)

'''
Automatic persistent data saving and loading
'''
def reload_state_data():
    try:
        with open("user_all_state.json", "r") as FILE1:
            storage.user_all = load(FILE1)
        with open("channel_all_state.json", "r") as FILE2:
            storage.channel_all = load(FILE2)
        with open("user_active_state.json", "r") as FILE3:
            storage.user_active = load(FILE3)
    except Exception:
        storage.user_all = {}
        storage.channel_all = {}
        storage.user_active = {}

if __name__ == "__main__":
    reload_state_data()

def save_state_data():
    with open("user_all_state.json"w") as FILE1:
        dump(storage.user_all, FILE1)
    with open("channel_all_state.json", "w") as FILE2:
        dump(storage.channel_all, FILE2)
    with open("user_active_state.json", "w") as FILE3:
        dump(storage.user_active, FILE3)
    t1 = threading.Timer(1.0, save_state_data)
    t1.daemon = True
    t1.start()
    
save_state_data()


# Example
@APP.route("/workspace/reset",methods = ['POST'])
def reset_workspace():
    reset.reset()
    return dumps({})


'''
auth routes.
'''
@APP.route("/auth/register", methods=['POST'])
def auth_register():
    input_data = request.get_json()
    register_data(input_data)
    email = input_data['email']
    password = input_data['password']
    name_first = input_data['name_first']
    name_last = input_data['name_last']
    # auth.auth_register() is what actually fucks with the database.
    returned_data = auth.auth_register(email,password,name_first,name_last)
    return dumps({
        'u_id': returned_data['u_id'],
        'token': returned_data['token'],
    })

@APP.route('/auth/login',methods=['POST'])
def auth_login():
    input_data = request.get_json()
    login_data(input_data)
    email = input_data['email']
    password = input_data['password']
    returned_data = auth.auth_login(email,password)
    return dumps({
        'u_id': returned_data['u_id'],
        'token': returned_data['token'],
    })

@APP.route('/auth/logout',methods = ['POST'])
def auth_logout():
    input_data = request.get_json()
    logout_data(input_data)
    token = input_data['token']
    returned_data = auth.auth_logout(token)
    if returned_data == True:
        return dumps(True)
    else:
        return dumps(False)

@APP.route("/auth/passwordreset/request",methods = ['POST'])
def auth_passwordreset_request():
    data = request.get_json()
    email = data['email']
    password.auth_passwordreset_request(email)
    return dumps({})

@APP.route("/auth/passwordreset/reset",methods = ['POST'])
def auth_passwordreset_reset():
    input_data = request.get_json()
    code = input_data['reset_code']
    new_pass = input_data['new_password']
    password.auth_passwordreset(code,new_pass)
    return dumps({})
    
'''
message routes.
'''
@APP.route('/message/send',methods=['POST'])
def message_send():
    input_data = request.get_json()
    token = input_data['token']
    channel_id = input_data['channel_id']
    message = input_data['message']
    returned_data = message_functions.message_send(token,channel_id,message)
    if returned_data == -1: return dumps({"code":-1})
    return dumps({
        'message_id': returned_data['message_id'],
    })

@APP.route('/message/react',methods=['POST'])
def message_react():
    input_data = request.get_json()
    token = input_data['token']
    message_id = input_data['message_id']
    react_id = input_data['react_id']
    returned_data = message_functions.message_react(token, message_id, react_id)
    return dumps({})


'''
channel routes
'''

@APP.route('/channel/invite',methods=['POST'])
#token channle_id user_id
def channel_invite():
    input_data = request.get_json()
    channel_invite_data(input_data)
    token = input_data['token']
    channle_id = input_data['channel_id']
    u_id = input_data['u_id']
    channel_first.channel_invite(token, channle_id, u_id)
    return dumps({})
@APP.route('/channels/create',methods=['POST'])
def channel_create():
    input_data = request.get_json()
    channel_create_data(input_data)
    token = input_data['token'] 
    name = input_data['name']
    is_public = input_data['is_public']
    returndata =  channel_first.channel_create(token,name,is_public)
    return dumps({'channel_id':returndata})
@APP.route('/channel/details',methods = ["GET"])
def channel_detail():
    token = request.args.get('token')
    channel_id = request.args.get('channel_id')
    returndata = channel_first.channel_detail(token,channel_id)
    return dumps({
        "name": returndata['name'],
        'owner_members': returndata['owner'],
        'all_members': returndata['members']
    })

@APP.route('/channels/list',methods = ["GET"])
def channels_list():
    token = request.args.get('token')
    returndata = channel.channels_list(token)
    return dumps({
        'channels': returndata['channels'],
    })

@APP.route('/channels/listall',methods = ["GET"])
def channels_listall():
    token = request.args.get('token')
    returndata = channel.channels_listall(token)
    # print(returndata)
    return dumps({
        'channels': returndata['channels'],
    })
''' 
user routes
'''
@APP.route('/user/profile',methods=['GET'])
def user_profile():
    user_dict = user.user_profile(request.args.get('token'),int(request.args.get('u_id')))
    return dumps(user_dict)
    

@APP.route('/user/profile/setname',methods=['PUT'])
def user_profile_setname():
    data = request.get_json()
    token = data['token']
    name_first =  data['name_first']
    name_last =  data['name_last']
    user.user_profile_setname(token, name_first, name_last)
    
    return dumps({})

    
@APP.route('/user/profile/setemail',methods=['PUT'])
def user_profile_setemail():
    data = request.get_json()
    token = data['token']
    email = str(data['email'])
    print(email)
    # return "hey"
    user.user_profile_setemail(token, email)
    return dumps({})

@APP.route('/user/profile/sethandle',methods = ["PUT"])
def user_profile_sethandle():
    data = request.get_json()
    token = data['token']
    handle_str = data['handle_str']
    user.user_profile_sethandle(token, handle_str)
    return ''
    
@APP.route('/user/profile/uploadphoto', methods=['POST'])
def user_profiles_uploadphoto_fn():
    data = request.get_json()
    token = data['token']
    img_url = data['img_url']
    x_start = data['x_start']
    y_start = data['y_start']
    x_end = data['x_end']
    y_end = data['y_end']
    user.user_profiles_uploadphoto(token, img_url, x_start, y_start, x_end, y_end)
    return ''

@APP.route('/users/all', methods=['GET'])
def users_all():
    token = request.form.get('token')
    all_users = user.users_all(token)
    return dumps(all_users)

@APP.route('/admin/user/remove', methods=['DELETE'])
def user_remove():
    data = request.get_json()
    token = data['token']
    u_id = data['u_id']
    user_remove.user_remove(token, u_id)
    return ''


'''
server initialization
'''

@APP.route('/channel/messages',methods = ['GET'])
def channel_message():
    token = request.args.get('token')
    channel_id = request.args.get('channel_id')
    start_index = int(request.args.get('start'))
    returnedata = channel_first.channel_message(token,channel_id, start_index)
    return dumps({
        'messages': returnedata['messages'],
        'start': returnedata['start'],
        'end': returnedata['end']
    })
@APP.route('/channel/leave',methods = ['POST'])
def channel_leave():
    data = request.get_json()
    token = data['token']
    channel_id = data['channel_id']
    channel_first.channel_leave(token,channel_id)
    return dumps({})
@APP.route('/channel/join',methods = ['POST'])
def channel_join():
    data = request.get_json()
    token = data['token']
    channel_id = data['channel_id']
    channel_first.channel_join(token, channel_id)
    return dumps({})


'''
standup routes.
'''
@APP.route('/standup/start',methods = ["POST"])
def standup_start():
    input_data = request.get_json()
    token = input_data['token']
    channel_id = input_data['channel_id']
    length = input_data['length']
    returned_data = standup.standup_start(token, channel_id, length)
    return dumps({
        'time_finish': returned_data['time_finish'],
    })

@APP.route('/standup/active',methods = ["GET"])
def standup_active():
    token = request.args.get('token')
    # token = input_data['token']
    channel_id =request.args.get('channel_id')
    returned_data = standup.standup_active(token, channel_id)
    return dumps({
        'is_active': returned_data['is_active'],
        'time_finish': returned_data['time_finish'],
    })

@APP.route('/standup/send',methods = ["POST"])
def standup_send():
    input_data = request.get_json()
    token = input_data['token']
    channel_id = input_data['channel_id']
    message = input_data['message']
    returned_data = standup.standup_send(token, channel_id, message)
    return dumps({})

''' 
admin routes
pyt'''

@APP.route('/admin/userpermission/change',methods=['POST'])
def admin_userpermission_change():
    input_data = request.get_json()
    token = input_data['token']
    u_id = input_data['u_id']
    permission_id = input_data['permission_id']
    returned_data = admin.admin_userpermission_change(token,u_id,permission_id)
    return dumps({})
if __name__ == "__main__":
    APP.run(debug = True,port=(int(sys.argv[1]) if len(sys.argv) == 2 else 8010))
