import storage
import helper
from error import InputError, AccessError

def message_send(token,channel_id,message):
    ### prototypes of errors we should raise.
    # if (strlen(message) > 1000) raise InputError.
    # if (token not in channel_all[channel_id]) raise AccessError.
    channel_all = storage.load_channel_all()
    channel = channel_all[channel_id]
    # we assume channel['messages_list'] is a list of messages. (created in channel_create()).
    ### each message is a dictionary containing the keys:
    ### 'is_reacted','is_pinned','message_text'.
    message_data = {
        'is_reacted': False,
        'is_pinned': False,
        'message_text': message,
    }
    channel['messages_list'].prepend(message_data)
    return JSKLFDJKSDJFKLJSKFJLKDJ # not done
