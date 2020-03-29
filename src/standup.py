import storage
import message_functions
import helper
import datetime
import auth
from error import InputError, AccessError

def standup_start(token, channel_id, length):
    channel_all = storage.load_channel_all()
    ### ERROR: channel_id is not a valid channel.
    if channel_id not in channel_all:
        raise InputError()
    channel = channel_all[channel_id]
    standup = channel['standup']
    ### ERROR: an active standup is currently running in this channel.
    if standup['is_active'] == True:
        raise InputError()

    ### we ensure that is_active is set to true AFTER finding the rest of the information.
    standup['length'] = length
    # finding time_finish (a Unix timestamp).
    now = helper.get_current_time_as_datetime()
    now_plus_length = now + datetime.timedelta(seconds = length)
    time_finish = helper.convert_datetime_to_unix_timestamp(now_plus_length)
    standup['time_finish'] = time_finish
    standup['message_queue'] = ''
    ### start standup.
    standup['is_active'] = True

    ### sleep for length seconds (during this period standup_send() calls will be successful).
    time.sleep(length)
    ### stop standup.
    standup['is_active'] = False
    ### send the standup['message_queue'] to the channel.
    message_functions.message_send(token, channel_id, standup['message_queue'])
    storage.save_channel_all(channel_all)
    return {
        'time_finish': time_finish,
    }
def standup_active(token, channel_id):
    channel_all = storage.load_channel_all()
    ### ERROR: channel_id is not a valid channel.
    if channel_id not in channel_all:
        raise InputError()

    ### finding is_active.
    channel = channel_all[channel_id]
    standup = channel['standup']
    is_active = channel['is_active']
    ### finding time_finish.
    if is_active == True:
        time_finish = standup['time_finish']
    else:
        time_finish = None

    return {
        'is_active': is_active,
        'time_finish': time_finish,
    }
def standup_send(token, channel_id, message):
    ##### ALL ERROR CHECKING.
    channel_all = storage.load_channel_all()
    ### ERROR: channel_id is not a valid channel.
    if channel_id not in channel_all:
        raise InputError()
    channel = channel_all[channel_id]
    standup = channel['standup']
    ### ERROR: an active standup is not currently running in this channel
    if standup['is_active'] == False:
        raise InputError()
    ### ERROR: message is more than 1000 characters.
    if len(message) > 1000:
        raise InputError()
    ### ERROR: user is not a member of the channel that the standup is occurring in.
    user_all_data = auth.get_data()
    u_id = helper.get_id(token, user_all_data)
    members_list = channel['member']
    owners_list = channel['owner']
    if u_id not in (members_list or owners_list):
        raise AccessError()
    ### ERROR: if because of all the above checks the standup becomes not active, dont send the message.
    if standup['is_active'] == False:
        raise InputError()

    ##### ACTUALLY SENDING THE MESSAGE TO THE QUEUE.
    user_data = user_all_data[u_id]
    handlestr = user_data['handlestr']
    standup['message_queue'] += generate_standup_message(handlestr, message)
    return {}

# helper function, only used in standup.py so won't include in helper.py for cleanliness.
def generate_standup_message(handlestr, message):
    # assuming the standup['message_queue'] string starts off as ''.
    # if a user with the handlestr "tfan" calls standup_send(),
    # then the message that should be added to standup['message_queue'] is:
    # "tfan: hello world!\n"
    # if another user with handlestr "karen" calls standup_send() after "tfan",
    # then the message that should be added to standup['message_queue'] still is:
    # "karen: hello!\n".
    # and the standup['message_queue'] string would be the contatenation of the two strings.
    # "tfan: hello world!\nkaren: hello!\n".
    return handlestr + ': ' + message + '\n'
