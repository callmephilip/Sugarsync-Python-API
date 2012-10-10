import urllib, httplib2
import xml.dom.minidom

class AccessToken:
    AUTH_ACCESS_TOKEN_API_URL = "https://api.sugarsync.com/authorization"
    API_SAMPLE_USER_AGENT = "SugarSync API Sample/1.0"
    ACCESS_TOKEN_AUTH_REQUEST_TEMPLATE = """<tokenAuthRequest>
                                            <accessKeyId>%(accessKey)s</accessKeyId>
                                            <privateAccessKey>%(privateAccessKey)s</privateAccessKey>
                                            <refreshToken>%(refreshToken)s</refreshToken>
                                            </tokenAuthRequest>"""

    def __init__(self,token):
        self.token = token

    def __str__(self):
        return self.token

    @staticmethod
    def getAccessToken(accessKeyId, privateAccessKey, refreshToken):
        request_body = xml.dom.minidom.parseString(AccessToken.ACCESS_TOKEN_AUTH_REQUEST_TEMPLATE % { "accessKey" : accessKeyId, "privateAccessKey" : privateAccessKey, "refreshToken" : refreshToken})

        print "request: %s" % request_body.toxml()

        http = httplib2.Http()
        resp, content = http.request(AccessToken.AUTH_ACCESS_TOKEN_API_URL, method='POST', body=request_body.toxml(), headers={"User-Agent" : AccessToken.API_SAMPLE_USER_AGENT, "Content-type": "application/xml; charset=UTF-8"})
        
        print "response: %s" % resp

        try:
            return AccessToken(resp["location"])
        except:
            return None