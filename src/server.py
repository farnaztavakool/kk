import sys
from json import dumps
from flask import Flask, request
from flask_cors import CORS
from error import InputError
import auth

import message
import channel_first

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
@APP.route('/message/login',methods=['POST'])
def message_send():
    input_data = request.get_json()
    token = input_data['token']
    channel_id = input_data['channel_id']
    message = input_data['message']
    returned_data = message.message_send(token,channel_id,message)
    return dumps({
        'message_id': returned_data['message_id'],
    })

<<<<<<< HEAD
'''
server initialization
'''
||||||| merged common ancestors
=======
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
   

>>>>>>> agreed_structure
if __name__ == "__main__":
    APP.run(debug = True,port=(int(sys.argv[1]) if len(sys.argv) == 2 else 8060))
