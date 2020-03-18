from auth import *
import pytest
from error import InputError
#check the function raise expection for wrong emails
email = "tavakolfarnaz@gmail.com"
password = "123456"
fname = "farnaz"
lname = "tavakol"
longname = "a" * 1001 
li = ["a","a@b.co","a@b","a@b.c","a@b.co","a@b.","a@b,com","a.com"]

# checking if the register and login works
def test_register_works():
    auth_register(email,password,fname,lname)
    auth_login(email,password)

# cheking if the function returns error when registering with an unvalid email
def test_register():
    with pytest.raises(InputError):
        assert auth_register("123","12345","fl","th")

# checking function returns error when using short password
def test_password():

    with pytest.raises(InputError):
        assert auth_register(email,"123",fname,lname)
        
# checking function returns error when using long fname
def test_long_first_name():
    with pytest.raises(InputError):
        assert auth_register(email,password,longname,lname)
        
# checking function returns error when using long lname
def test_long_last_name():
    with pytest.raises(InputError):
        assert auth_register(email,password,fname,longname)
        
#token passes to us from login == register

def test_token():

    user_id1, user_token1 = auth_register(email,password,fname,lname)
    user_id2, user_token2 = auth_login(email,password)
    assert user_id2 == user_id1
    assert user_token1 == user_token2

#checking the function throwing an error when registering with an email already registered 
def test_check_user_email():
    #register a user with email
    auth_register(email,password,fname,lname)
    # should raises error for registering the same email again
    with pytest.raises(InputError):
        assert auth_register(email,"1111111","jack","tom")
        
        
#checking the function raise error when entered the
   
def test_user_pass():
    auth_register(email,password,fname,lname)
    with pytest.raises(InputError):
        assert auth_login(email,"123")

# checking the function returns an error entering an unvalid email
def test_user_login_email():
    with pytest.raises(InputError):
        assert [auth_register(email,password = "12345678910",name_first = "farnaz",name_last = "jade") for email in li]
       
#checking each user having a unique token and id 
def check_unique_token():

    user1_token,user1_id = auth_register(email,password,fname,lname)
    user2_token,user2_id = auth_register("z5212916@unsw.edu.au","56789","lou","james")
    assert user1_token != user2_token
    assert user1_id != user2_id

# checking the logout function works when the user is active
def test_auth_logout():

    auth_register(email,password,fname,lname)
    usr = auth_login(email,password)
    usr_token = usr['token'] 


    k = auth_logout(usr_token)
    assert k['is_success'] == True


#raising exception when the token is not active

def test_unactive_logout():
    auth_register(email,password,fname,lname)
    usr = auth_login(email,password)
    usr_token = usr['token'] 
    auth_logout('token')
    with pytest.raises(Exception):
        assert auth_logout(usr_token) 


# tying to log out an unvalid token

# def test_unvalid_token():

#     with pytest.raises(Exception):
#         assert auth_logout("THISISNOTATOKEN")