# SugarSync Python API (unofficial and very incomplete)

## What's in the box

Not much. You can authenticate to SugarSync using their pseudo OAuth model. Here's how you do it

```python

from sugarsync.auth.RefreshToken import RefreshToken
from sugarsync.auth.AccessToken import AccessToken

refresh_token = RefreshToken.getRefreshToken("email", "password", "application-id", "access-key", "private-access-key")
access_token = AccessToken.getAccessToken("access-key", "private-access-key", str(refresh_token))

```

Or you can use a shortcut:

```python

from auth import authenticate

access_token, refresh_token  = authenticate("email","password", "application-id", "app-key", "app-secret")

print "Access token: %s" % access_token
print "Refresh token: %s" % refresh_token 

```  