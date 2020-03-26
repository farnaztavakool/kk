import re
import error
def check_email(email,data):
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if re.search(regex,email): return True
    raise error.InputError
    print ([True for i in data if i['email'] == email])
        # raise error.InputError
    

def check_name(fname,lname):
    if len(fname) >50 or len(lname) > 50: raise error.InputError
    return True

def check_pass(password):
     if len(password) < 6: raise error.InputError
     return True

# make it 
    