import re
import error
def check_email(email):
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if re.search(regex,email): return True
    raise error.InputError
        # raise error.InputError

def check_email_exist(email,data):
    if any([True for i in data if data[i]['email'] == email ]):
        raise error.InputError
    

def check_name(fname,lname):
    if len(fname) >50 or len(lname) > 50: raise error.InputError
    return True

def check_pass(password):
     if len(password) < 6: raise error.InputError
     return True

# make it 
    