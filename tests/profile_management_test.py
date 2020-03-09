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

# test if it has errors if it is given the wrong user id 
def test_incorrect_token():
    user1 = user1_regist()
    token = user1['token'] 
    incorrect_uid = user1['uid'] + 25
    with pytest.raises(InputError):
        assert user_profile(token, incorrect_uid)


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

invalid_name = "a" * 51

def is_invalid_name(given_name):
    length = len(given_name)    
    if length > 50:
        return "Invalid name"
    else:
        return "Valid name"

# test invalid first name
def test_first_name():
    user2 = auth_register("hkhkhk999@naver.com", "1234yu!", invalid_name, "Kim")
    token = user2['token']
    uid = user2['u_id'] 
    profile = user_profile(token, uid)
    given_first = profile['user']['name_first'] 
    with pytest.raises(InputError):
         assert user_profile_setname(token, given_first, "Kim") 

# test invalid last name
def test_last_name():
    user22 = auth_register("hkhkhk999@gmail.com", "13asdf4yu", "Eunseo", invalid_name)
    token = user22['token']
    uid = user22['u_id'] 
    profile = user_profile(token, uid)
    given_last = profile['user']['name_last'] 
    with pytest.raises(InputError):
         assert user_profile_setname(token, "Eunseo", given_last)    

def test_valid_length():
    user1_profile = return_profile()
    given_first = user1_profile['user']['name_first'] 
    given_last = user1_profile['user']['name_last']  
    assert is_invalid_name(given_first) == "Valid name"
    assert is_invalid_name(given_last) == "Valid name"    

###########################################################
#                test user_profile_setemail                #         
########################################################### 

# test if the email has been updated
def test_email_updated():
    user17 = auth_register("valide@gmail.com", "1123!", "Twice", "Special")
    u_token = user17['token']
    uid = user17['uid'] 
    profile = user_profile(u_token, uid)
    user_profile_setemail(u_token, "updated@gmail.com")
    assert profile['user']['email'] == "updated@gmail.com"

# invalid_email = "hahajk@unless...?"
# helper function to check if it is a valid email
def check_valid_email(given_email):
    if re.match(r"(^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$)", given_email):
        return "Valid email"
    else:
        return "Invalid email"

def test_email_exception():
    # assumtion = if i register a user the token and id is all different
    user9 = user1_regist()
    token = user9['token']
    with pytest.raises(InputError):
         assert user_profile_setemail(token, "hahajk@unless...?")    
    with pytest.raises(InputError):
         assert user_profile_setemail(token, "thisisainvalidemail")    
    with pytest.raises(InputError):
         assert user_profile_setemail(token, "wotif@disisnotanemail")
    with pytest.raises(InputError):
         assert user_profile_setemail(token, "testingggdifferent.emails")

# test a valid email
def test_valid_email():
    user1_profile = return_profile()
    given_email = user1_profile['user']['email']  
    assert check_valid_email(given_email) == "Valid email"

# test to change it to a email that already exists
def test_existing_email():
    auth_register("v1email@gmail.com", "haha?", "Blackpink", "BOOMBAYA")
    user_v2 = auth_register("v2email@gmail.com", "hehehe!", "Redvelvet", "psycho")
    v2_token = user_v2['token']
    with pytest.raises(InputError):
         assert user_profile_setemail(v2_token, "v1email@gmail.com")    

###########################################################
#                test user_profile_sethandle              #         
########################################################### 

invalid_handle1 = "ifeellikeireallyneedtosleepatmaaaaa"
invalid_handle2 = "hi"

def is_invalid_handle(given_handle):
    length = len(given_handle)    
    if length > 2 and length < 21:
        return "Valid handle"
    else:
        return "Invalid handle"

def test_long_handle():
    userr = user1_regist()
    token = userr['token']
    with pytest.raises(InputError):
         assert user_profile_sethandle(token, invalid_handle1)    
    with pytest.raises(InputError):
         assert user_profile_sethandle(token, invalid_handle2)    

# test to change it to a handle that already exists
def test_existing_handle():
    user1 = auth_register("user1@gmail.com", "haha???", "Black", "Pink")
    user1_token = user1['token']
    user2 = auth_register("user2@gmail.com", "hehe!!", "Red", "Velvet")
    user2_token = user2['token']
    user_profile_sethandle(user2_token, "Handle")
    with pytest.raises(InputError):
         assert user_profile_setemail(user1_token, "Handle")  
