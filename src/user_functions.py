import storage
import error
import helper
import requests
import shutil
import random
import string
import PIL
import os

# gets data of a single user identified by u_id from user_all 
# database in storage.py, and returns data as a dictionary
def user_profile(token, u_id):
    user_all = storage.load_user_all()

    # helper.check_user(u_id, user_all)

    user = {
        'u_id': u_id,
        'email': user_all[str(u_id)]['email'],
        'name_first': user_all[str(u_id)]['name_first'],
        'name_last': user_all[str(u_id)]['name_last'],
        'handle_str': user_all[str(u_id)]['token'],
    }
    return user
    
def user_profile_setname(token, name_first, name_last): 
    helper.check_name(name_first, name_last)
    user_all = storage.load_user_all()
    u_id = helper.get_id(token,user_all)
    user_all[str(u_id)]['name_first'] = name_first
    user_all[str(u_id)]['name_last'] = name_last
    storage.save_user_all(user_all)

def user_profile_setemail(token, email): 
    data = storage.load_user_all()
    
    helper.check_email(email)
    helper.check_email_exist(email,data)
    user_all = storage.load_user_all()
    u_id = helper.get_id(token,data)
    user_all[str(u_id)]['email'] = email
    storage.save_user_all(user_all)

def user_profile_sethandle(token, handle_str): 
    # InputError if length of handle_str invalid
    user_all = storage.load_user_all()
    if len(handle_str) < 2 or len(handle_str) > 20:
        raise error.InputError
    # InputError if handle is taken by another user
    u_id = str(helper.get_id(token,user_all))
    for user in user_all:
        if handle_str == user_all[user]['handle']:
            raise error.InputError
            
    user_all = storage.load_user_all()
   
    user_all[u_id]['handle'] = handle_str
    storage.save_user_all(user_all)

def users_all(token):
    user_all = storage.load_user_all()
    users = {"users":[]}
    for user in user_all:
        user_data = {
            'u_id': user_all[user]['u_id'],
            'email': user_all[user]['email'],
            'name_first': user_all[user]['name_first'],
            'name_last': user_all[user]['name_last'],
            'handle_str': user_all[user]['handle'],
        }
        users["users"].append(user_data)
    return users
            
def user_profiles_uploadphoto(token, img_url, x_start, y_start, x_end, y_end):

    # get file from img_url.
    response = requests.get(img_url, stream=True)
    if response.status_code != 200:
        raise error.InputError()
    # make a new file with filename: image12characters.jpg.
    filename = f'{get_random_alphaNumeric_string(12)}.jpg'
    # stored in filepath: /pictures.
    filepath = f'/pictures/{filename}'
    with open(filepath, 'wb') as OUT_FILE:
        # copy data into file without checking its type.
        shutil.copyfileobj(response.raw, OUT_FILE)
    del response

    # check file is a jpg.
    try:
        with PIL.Image.open(filepath) as IMAGE_FILE:
            if IMAGE_FILE.format != 'JPEG':
                # remove the file we created.
                os.remove(filepath)
                raise InputError("Image given is not a jpeg.")
    except IOError:
        # remove the file we created.
        os.remove(filepath)
        raise InputError("PIL failed to open the file. Likely file isn't a valid image.")

    # we now know filepath *is* a jpg image.
    # check the dimensions of the image.
    with PIL.Image.open(filepath) as IMAGE_FILE:
        # IMAGE_FILE.size returns tuple (width, height) of IMAGE_FILE.
        width, height = IMAGE_FILE.size
        if ((x_end - x_start) >= width) or ((y_end - y_start) >= height):
            # remove the file we created.
            os.remove(filepath)
            raise InputError("You gave the wrong dimensions for cropping dummy.")

    # crop image.
    with PIL.Image.open(filepath) as IMAGE_FILE:
        box = (x_start,y_start,x_end,y_end)
        CROPPED_IMAGE_FILE = IMAGE_FILE.crop(box)
        # save cropped image into a new file.
        new_filename = 'cropped' + filename
        new_filepath = f'/pictures/{new_filename}'
        CROPPED_IMAGE_FILE.save(new_filepath)
        # for debugging purposes, don't bother removing the IMAGE_FILE.

    # attach the CROPPED_IMAGE_FILE to its respective user profile image.

    ### hmmm now how to let front end know where the file is...
    
    return {}
    
def get_random_alphaNumeric_string(stringLength):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join((random.choice(lettersAndDigits) for i in range(stringLength)))
