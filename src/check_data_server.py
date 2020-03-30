
from error import HTTPException
def register_data(input_data):
    if not input_data['name_first'] or not input_data['name_last']or not input_data['email'] or not input_data['password']   : raise HTTPException

def login_data(input_data):
    if not input_data['email'] or not input_data['password']: raise HTTPException

def logout_data(input_data):
    if not input_data['token']: raise HTTPException