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

def user1_regist():
    user = auth_register("cs1531@cse.unsw.edu.au", "1234yu!", "Hayden", "Jacobs")
    return { 'token': user['token'], 'uid': user['u_id'] }


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
    user1 = user1_regist()
    token = user1['token']
    uid = user1['uid'] 
    profile = user_profile(token, uid)
    profile_email = profile['user']['email']
    email = 'cs1531@cse.unsw.edu.au'
    profile_name = profile['user']['name_first']
    name = 'Hayden'
    assert email == profile_email
    assert name == profile_name

###########################################################
#                test user_profile_setname                #         
###########################################################

    


    













