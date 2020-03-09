# Ability to view user anyone's user profile, 
# and modify a user's own profile 
# (name, email, handle, and profile photo)

# user_profile
# user_profile_setname
# user_profile_setemail
# user_profile_sethandle

from auth import auth_register
from user import *
from error import InputError
import pytest
import re

def user1_regist():
    user = auth_register("cs1531@cse.unsw.edu.au", "1234yu!", "Hayden", "Jacobs")
    return { 'token': user['token'], 'uid': user['u_id'] }

def return_profile():
    user1 = user1_regist()
    token = user1['token']
    uid = user1['uid'] 
    profile = user_profile(token, uid)
    return profile    


###########################################################
#                   test user_profile                     #
###########################################################

# test if it has errors if it is given the wrong token for the user id
def test_incorrect_token():
    user1 = user1_regist()
    incorrect_token = user1['token'] + '7676'
    uid = user1['uid']
    with pytest.raises(InputError):
        user_profile(incorrect_token, uid)
        raise InputError


# check if the profile information matches with the expectation
def test_profile():
    profile = return_profile()
    profile_email = profile['user']['email']
    email = 'cs1531@cse.unsw.edu.au'
    profile_name = profile['user']['name_first']
    name = 'Hayden'
    assert email == profile_email
    assert name == profile_name

###########################################################
#                test user_profile_setname                #         
###########################################################

# if the first or last name is more than 100 charactors 
# it is too long and considered invalid

invalid_name = "a" * 101

def is_invalid_name(given_name):
    length = len(given_name)    
    if length > 100:
        return "Invalid name"
    else:
        return "Valid name"

def test_long_name():
    user2 = auth_register("hkhkhk999@naver.com", "1234yu!", invalid_name, invalid_name)
    token = user2['token']
    uid = user2['u_id'] 
    profile = user_profile(token, uid)
    given_first = profile['user']['name_first'] 
    given_last = profile['user']['name_last']  
    assert is_invalid_name(given_first) == "Invalid name"
    assert is_invalid_name(given_last) == "Invalid name"

def test_valid_length():
    user1_profile = return_profile()
    given_first = user1_profile['user']['name_first'] 
    given_last = user1_profile['user']['name_last']  
    assert is_invalid_name(given_first) == "Valid name"
    assert is_invalid_name(given_last) == "Valid name"    

###########################################################
#                test user_profile_setemail                #         
########################################################### 

# invalid_email = "hahajk@unless...?"
def check_valid_email(given_email):
    if re.match(r"(^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$)", given_email):
        return "Valid email"
    else:
        return "Invalid email"

def test_email_exception():
    # assumtion = if i register a user the token and id is all different
    user3 = auth_register("hahajk@unless...?", "1234yu!", "Hailey", "Jung")
    token = user3['token']
    uid = user3['u_id'] 
    profile = user_profile(token, uid)
    given_email = profile['user']['email']
    assert check_valid_email(given_email) == "Invalid email"


###########################################################
#                test user_profile_sethandle              #         
########################################################### 

# invalid_handle = "ifeellikeireallyneedtosleepatm"

def is_invalid_handle(given_handle):
    length = len(given_handle)    
    if length > 4 and length < 15:
        return "Valid handle"
    else:
        return "Invalid handle"

def test_long_handle():
    profile = return_profile()
    given_handle = profile['user']['handle_str']   
    assert is_invalid_handle(given_handle) == "Valid handle"

    
    


    













