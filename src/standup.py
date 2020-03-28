import storage
import message
import helper
import datetime

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
    return {}
def standup_send(token, channel_id, message):
    return {}
