# W17A-17 Assumptions Markdown File
### Ability to login, register if not registered, and log out
```
login_test.py
```
**Assumptions**:
- THISISNOTTOKEN would never be a token and in invalid.

### Ability to reset password if forgotten it
```
reset_password_test.py
```
### Ability to see a list of channels
```
channel_list_view_test.py
```
### Ability to create a channel, join a channel, invite someone else to a channel, and leave a channel
```
channel_management_test.py
```
**Assumptions**:
- User who creates channel is not necessarily a member of the channel immediately after creating the channel?

### Within a channel, ability to view all messages, view the members of the channel, and the details of the channel
``` 
channel_details_view_test.py
```
### Within a channel, ability to send a message now, or to send a message at a specified time in the future
```
message_send_test.py
```
**Assumptions**:
- There is no maximum length of a message

### Within a channel, ability to edit, remove, pin, unpin, react, or unreact to a message
```
message_modification_test.py
```
**Assumptions**:
- If the message is removed and when you search the removed message, the return value is 0
- If the message has been edited the message before editing it gone

### Ability to view user anyone’s user profile, and modify a user’s own profile (name, email, handle, and profile photo)
```
profile_management_test.py
```
**Assumptions**:
- When you register a user they all have different u_id and tokens

### Ability to search for messages based on a search string
```
message_search_test.py
```
### Ability to modify a user’s admin privileges: (MEMBER, OWNER)
```
privilege_modification_test.py
```
### Ability to begin a “standup”, which is an X minute period where users can send messages that at the end of the period will automatically be collated and summarised to all users
```
standup_initialization_test.py
```
