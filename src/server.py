import sys
from json import dumps
from flask import Flask, request
from flask_cors import CORS
from error import InputError
import auth

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
auth routes
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
if __name__ == "__main__":
    APP.run(debug = True,port=(int(sys.argv[1]) if len(sys.argv) == 2 else 8040))
