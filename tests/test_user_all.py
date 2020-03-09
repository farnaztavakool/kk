from auth import auth_register
import pytest
from other import users_all


# this test file will should all of the users registered
def test_all_user():

    usr = auth_register("tavakolfarnaz@gmail.com","0312138","farnaz","tavakol")
    usrid = usr['u_id']
    usrtoken = usr['token']

    users = users_all(usrtoken)
    user = users['users']
    assert user[0]['u_id'] == usrid