#Ability to view user anyone's user profile, 
#and modify a user's own profile 
#(name, email, handle, and profile photo)

#user_profile
#user_profile_setname
#user_profile_setemail
#user_profile_sethandle

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

# invalid_name = "a" * 101

# def test_invalid_name(given_name):
# #     profile = return_profile()
# #     profile_first_name = profile['user']['name_first']  
# #     length = len(profile_first_name)
#     length = len(given_name)    
#     if length > 100:
#         raise Exception("Invalid name")
#     else:
#         return "Valid name"

# def test_name_exception():
#     with pytest.raises(Exception, match = "Invalid name"):
#         assert test_invalid_name(invalid_name)

###########################################################
#                test user_profile_setemail                #         
########################################################### 

# invalid_email = "hahajk@unless...?"
def check_valid_email(given_email):
    if re.match(r"(^[a-zA-Z0-9]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", given_email):
        return "Valid email"
    else:
        return "Invalid email"

def test_email_exception():
    user2 = auth_register("hahajk@unless...?", "1234yu!", "Hailey", "Jung")
    token = user2['token']
    uid = user2['u_id'] 
    profile = user_profile(token, uid)
    given_email = profile['user']['email']
    assert check_valid_email(given_email) == "Valid email"



    
    


    













