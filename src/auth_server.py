# get the info
# check the info
# add them to pickle
# return the result 
from flask import request
from json import dumps
import error
import pickle
import helper
dataStore = {}
def uid(name):
    return name

def token(fname,lname):
    return fname+lname

def getData():
    global dataStore
    with open("user.p","rb") as FILE:
        dataStore = pickle.load(FILE)
        
        return dataStore 

# def resetStore():
# implement the reset route 

# how can I make change to the pickle code 
def make_data(data):
    dic = {}
    dic['u_id'] = uid(data['name'])
    dic['token'] =token (data['name'],data['lastname'])
    dic['email'] = data['email']
    dic['pass'] = data['password']
    return dic


def auth_register():
    store = getData()
    data = request.get_json()
    if helper.check_detail(store,data) == False:
        raise error.InputError


    else:
        dic = make_data(data)
        store['user'].append(dic)
        with open("user.p","wb") as FILE:
            pickle.dump(store,FILE)
    
    return {}
