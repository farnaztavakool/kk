# dataStore.md: What data do we store/load and how?

## What data do we store?

- Per User:
    - first_name, last_name, email, encrypted_password, token??, handle, u_id, permission_id.
    - note: we need some way to check if the token given is a valid active token or not.
    - we also need to keep a list of all users too...
- Per Channel:
    - channel_id, channel_name, owner_members_list, all_members_list, messages_list, standup.
    - we also need to keep a list of all channels too...
- Per Message:
    - message_index, is_reacted, is_pinned, message_text.
- Per Standup:
    - finish_time, message_queue, is_active.

## How do we store this data?
### Recall a .p file is what stores the pickled data.
### Think of it like a .zip file, its just a file that stores some data. 
### We can "unpickle" (or "unzip") the file to get what we originally stored back.
### I love dictionaries :frowning:
- Per User:
    - Dictionary? 
    - Keys: first_name, last_name, email, encrypted_password, token, u_id, handle, permission_id.
- All Users:``userAll.p``
    - Dictionary of users.
    - Keys: u_id.
- Per Channel:
    - Dictionary :slight_smile:.
    - Keys: channel_id, channel_name, owner_members_list, all_members_list, messages_list, standup.
- All Channels:``channelAll.p``
    - Dictionary of channels..
    - Keys: channel_id.
- Per Message:
    - Dictionary.
    - Keys: message_index, is_reacted, is_pinned, message_text.
- Per Standup:
    - Dictionary.
    - Keys: finish_time, message_queue, is_active.

### If we want to only use only one .p file, we can make a list (array) of 2 dictionaries, one dictionary being the dictionary in userAll.p, and the other dictionary being the dictionary in channelAll.p.

### Is this smart??? I have no clue.

# wtf. :tada:

