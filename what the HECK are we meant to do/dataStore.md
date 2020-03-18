# dataStore.md: What data do we store/load and how?

## What data do we store? (per function).

- Per User:
    - first_name, last_name, email, encrypted_password, token??, handle, u_id, permission_id.
    - note: we need some way to check if the token given is a valid active token or not.
    - we also need to keep a list of all users too...
- Per Channel:
    - channel_id, channel_name, owner_members_list, all_members_list, messages_list, standup??? (if standup exists, then it is active???).
    - we also need to keep a list of all channels too...
- Per Message:
    - message_index, is_reacted, is_pinned, message_text.
- Per Standup:
    - finish_time, message_queue.

## TOO HARD aaAAAaaaA.

