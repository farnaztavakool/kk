import sys
from json import dumps
from flask import Flask, request
from flask_cors import CORS
from error import InputError
import auth

import message_functions
import channel_first
import standup
import reset
from  check_data_server import *

# 93858500 -->financial help

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

APP.config['TRAP_HTTP_EXCEPTIONS'] = True
# APP.register_error_handler(Exception, defaultHandler)

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
    return dumps({
        'message_id': returned_data['message_id'],
    })


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
@APP.route('/channel/create',methods=['POST'])
def channel_create():
    input_data = request.get_json()
    channel_create_data(input_data)
    token = input_data['token'] 
    name = input_data['name']
    is_public = input_data['is_public']
    returndata =  channel_first.channel_create(token,name,is_public)
    return str(returndata)
@APP.route('/channel/detail',methods = ["GET"])
def channel_detail():
    token = request.args.get('token')
    channel_id = request.args.get('channel_id')
    returndata = channel_first.channel_detail(token,channel_id)
    return dumps({
        "name": returndata['name'],
        'owner_members': returndata['owner'],
        'all_members': returndata['members']
    })


''' 
user routes
'''
# @APP.route('/user/profile/setname',methods=['PUT'])
# def user_profile_setname():
#     input_data = request.get_json()
#     token = input_data['token']
#     name_first = input_data['name_first']
#     name_last = input_data['name_last']
#     user.user_profile_setname(token, name_first, name_last)
#     return ''
    
# @APP.route('/user/profile/setemail',methods=['PUT'])
# def user_profile_setemail():
#     input_data = request.get_json()
#     token = input_data['token']
#     email = input_data['email']
#     user.user_profile_setemail(token, email)
#     return ''

# @APP.route('/user/profile/sethandle',methods = ["PUT"])
# def user_profile_sethandle():
#     input_data = request.get_json()
#     token = input_data['token']
#     handle_str = input_data['handle_str']
#     user.user_profile_sethandle(token, handle_str)
#     return ''
'''
server initialization
'''

@APP.route('/channel/message',methods = ['GET'])
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
    input_data = request.get_json()
    token = input_data['token']
    channel_id = input_data['channel_id']
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
if __name__ == "__main__":
    APP.run(debug = True,port=(int(sys.argv[1]) if len(sys.argv) == 2 else 8060))
