from auth.RefreshToken import RefreshToken
from auth.AccessToken import AccessToken

def authenticate(email,password, application_id, application_key, application_secret):
	"""
		returns a tuple containing an access token and a refresh token like so:

			(access_token, refresh_token)
	"""
	refresh_token = RefreshToken.getRefreshToken(email,password, application_id, application_key, application_secret)
	access_token = AccessToken.getAccessToken(application_key, application_secret, str(refresh_token))
	return (access_token, refresh_token)