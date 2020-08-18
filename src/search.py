import storage
import helper

def return_time_created(message):
    return message['time_created']

def message_search(token,query_str):
    channels_all = storage.load_channel_all()
    u_id = helper.get_u_id_from_token(token)
    messages = []
    for channel in channels_all:
        for message in channel['messages']:
            if message['u_id'] != u_id:
                continue
            # so message is a message the user has posted themself.
            if query_str in message['message_text']:
                messages.append(message)
    # sort messages list by the 'time_created' key.
    messages.sort(key = return_time_created)
    return {
        'messages': messages,
    }