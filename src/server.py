import sys
from json import dumps
from flask import Flask, request
# from flask_cors import CORS
from error import InputError
import auth

import message_functions
import channel_first
import standup

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
# CORS(APP)

APP.config['TRAP_HTTP_EXCEPTIONS'] = True
# APP.register_error_handler(Exception, defaultHandler)

# Example
@APP.route("/echo", methods=['GET'])
def echo():
    data = request.args.get('data')
    if data == 'echo':
   	    raise InputError(description='Cannot echo "echo"')
    return dumps({
        'data': data
    })

'''
auth routes.
'''
@APP.route("/auth/register", methods=['POST'])
def auth_register():
    # all POST requests take input in json format.
    input_data = request.get_json()
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
    token = input_data['token']
    '''
    # remember "is_success" in the spec is a boolean XD.
    returned_data = auth.auth_logout(token)
    if returned_data == True:
        return dumps(True)
    else:
        return dumps(False)
    '''
    return dumps(auth.auth_logout(token))
    '''
    if auth.auth_logout(token) == True: return "is_success"
    return "is_failure"
    '''
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

@APP.route('/message/sendlater',methods=['POST'])
def message_sendlater():
    input_data = request.get_json()
    token = input_data['token']
    channel_id = input_data['channel_id']
    message = input_data['message']
    time_sent = input_data['time_sent']
    returned_data = message_functions.message_sendlater(token, channel_id, message, time_sent)
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
    token = input_data['token']
    channle_id = input_data['channel_id']
    u_id = input_data['u_id']
    channel_first.channel_invite(token, channle_id, u_id)
    return "right"

@APP.route('/channel/create',methods=['POST'])
def channel_create():
    input_data = request.get_json()
    token = input_data['token'] 
    name = input_data['name']
    is_public = input_data['is_public']
    returndata =  channel_first.channel_create(token,name,is_public)
    return returndata

@APP.route('/channel/detail',methods = ["GET"])
def channel_detail():
    token = request.args.get('token')
    channel_id = request.args.get('channel_id')
    returndata = channel_first.channel_detail(token,channel_id)
    return dumps({
        'owner': returndata['owner'],
        'number_of_members': returndata['members']
    })

@APP.route('/channel/addowner',methods = ["POST"])
def channel_addowner():
    input_data = request.get_json()
    token = input_data['token']
    channle_id = input_data['channel_id']
    u_id = input_data['u_id']
    returndata = channel.channel_addowner(token,channel_id,u_id)
    return dumps({})

@APP.route('/channel/removeowner',methods = ["POST"])
def channel_removeowner():
    input_data = request.get_json()
    token = input_data['token']
    channle_id = input_data['channel_id']
    u_id = input_data['u_id']
    returndata = channel.channel_removeowner(token,channel_id,u_id)
    return dumps({})

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
    returndata = channel.channels_list(token)
    return dumps({
        'channels': returndata['channels'],
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
