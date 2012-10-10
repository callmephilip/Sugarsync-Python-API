import urllib, httplib2
import xml.dom.minidom


class RefreshToken:
	APP_AUTH_REFRESH_TOKEN_API_URL = "https://api.sugarsync.com/app-authorization"
	API_SAMPLE_USER_AGENT = "xendo/1.1"
	APP_AUTH_REQUEST_TEMPLATE = """<appAuthorization>
        	<username>%(username)s</username>
            <password>%(password)s</password>
            <application>%(application)s</application>
            <accessKeyId>%(accessKey)s</accessKeyId>
            <privateAccessKey>%(privateAccessKey)s</privateAccessKey>
        </appAuthorization>
    """

	def __init__(self,token):
		self.token = token

	def __str__(self):
		return self.token

	@staticmethod
	def getRefreshToken(username, password, application, accessKey, privateAccessKey):
		request_body = auth_dom=xml.dom.minidom.parseString(RefreshToken.APP_AUTH_REQUEST_TEMPLATE % { "username" : username, "password" : password, "application" : application, "accessKey" : accessKey, "privateAccessKey" : privateAccessKey})

		print "request: %s" % request_body.toxml()

		http = httplib2.Http()
		resp, content = http.request(RefreshToken.APP_AUTH_REFRESH_TOKEN_API_URL, method='POST', body=request_body.toxml(), headers={"User-Agent" : RefreshToken.API_SAMPLE_USER_AGENT, "Content-type": "application/xml; charset=UTF-8"})
		
		try:
			return RefreshToken(resp["location"])
		except:
			return None