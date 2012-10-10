# SugarSync Python API (unofficial and very incomplete)

## What's in the box

Not much. You can authenticate to SugarSync using their pseudo OAuth model. Here's how you do it

```python

from sugarsync.auth.RefreshToken import RefreshToken
from sugarsync.auth.AccessToken import AccessToken

refresh_token = RefreshToken.getRefreshToken("email", "password", "application-id", "access-key", "private-access-key")
access_token = AccessToken.getAccessToken("access-key", "private-access-key", str(refresh_token))

```  