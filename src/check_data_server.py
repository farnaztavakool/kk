
from error import HTTPException
def register_data(input_data):
    if not input_data['name_first'] or not input_data['name_last']or not input_data['email'] or not input_data['password']   : raise HTTPException

def login_data(input_data):
    if not input_data['email'] or not input_data['password']: raise HTTPException

def logout_data(input_data):
    if not input_data['token']: raise HTTPException

def channel_invite_data(input_data):
    if not input_data['channel_id'] or not input_data['token'] or not input_data['u_id']: raise HTTPException

def channel_create_data(input_data):
    if not input_data['name'] or not input_data['is_public'] or not input_data['token']: raise HTTPException

def channel_detail_data(input_data):
    if not input_data['token'] or not input_data['channel_id']: raise HTTPException