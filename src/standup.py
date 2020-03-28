import storage
import message
import helper
import datetime
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

    ### start standup.
    standup['is_active'] = True
    standup['length'] = length
    # finding time_finish (a Unix timestamp).
    now = helper.get_current_time()
    now_plus_length = now + datetime.timedelta(seconds = length)
    time_finish = helper.convert_datetime_to_unix_timestamp(now_plus_length)
    standup['time_finish'] = time_finish

    ### sleep for length seconds (during this period standup_send() calls will be successful).
    ### < we assume that the above lines are done almost instaneously :)))) >
    time.sleep(length)

    ### stop standup.
    standup['is_active'] = False

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
    user_all = storage.load_user_all()
    return {}
