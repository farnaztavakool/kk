import pickle

USER_DATABASE = {
    'user' : [
        {   
            'email':0,
            'token':0,
            "u_id":0,
            "pass":0
        }
    ]
}

with open("user.p",'wb') as FILE:
    pickle.dump(USER_DATABASE,FILE)