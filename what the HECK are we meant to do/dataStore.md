# dataStore.md: What data do we store/load and how?

## What data do we store? (per function).
- auth/login:
    - The valid active token generated for the user.
- auth/logout:
    - That the input valid active token is now an invalid inactive token.
- auth/register:
    - Store some dictionary like
    ```python
    {
        'first_name':'timothy',
        'last_name':'fan',
        'email':'bsEmail@gmail.com',
        # we note that this password should be encrypted...
        'password':encrypt('goodPassword:)'),
        'token':generateToken(),
        'handle':getHandle(first_name,last_name)
    }
    ```
    - Store the new token generated for authentication...
    - Store the handle? (a nickname for the user.)
-
-
-

