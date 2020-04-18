import smtplib
import storage
from email.message import EmailMessage
import helper
import error
from random import randint
from auth import encrypt_pass
'''
when changing user_data we want that data to change 
in channel_data as well  




'''
# sending a code to the user for changing their email

def get_data():
    try:
        data = storage.load_code_file()
    except Exception:
        storage.new_code_file()
        data = storage.load_code_file()
    return data
def auth_passwordreset_request(email):
    code = str(randint(1,200))
    data = get_data()
    pass2 = "0312138261"
    msg = EmailMessage()
    msg['Subject'] = "passwofd_reset_code"
    msg['From'] = "iteration3.comp1531@gmail.com"
    msg['To'] = email
    msg.set_content(code)
    s = smtplib.SMTP( 'smtp.gmail.com',587)
    s.ehlo()
    s.starttls()
    s.login("iteration3.comp1531@gmail.com",pass2)
    s.send_message(msg)
    s.quit()
    data[code] = email
    storage.save_code_file(data)

def auth_passwordreset(code,new_pass):
    # check if the new email is valid
    new_pass = encrypt_pass(new_pass)
    user = storage.load_user_all()
    # check if the new email is not already in use
    data = get_data()
    
    # check if the code is valid
    if code not in data: raise error.InputError
    email = data[code]

    # find the user to change their email
    i = [i for i in user if user[i]['email'] == email][0]
    user[i]['encrypted_password'] = new_pass
    storage.save_user_all(user)
    
        
# auth_passwordreset_request("tavakolfarnaz@gmail.com")
# auth_passwordreset("0312138261","xxxx@gamil.com")