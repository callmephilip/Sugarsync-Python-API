import urllib, httplib2
import xml.dom.minidom
from bs4 import BeautifulSoup
import iso8601
from datetime import datetime
import pytz

class AccessToken:
    AUTH_ACCESS_TOKEN_API_URL = "https://api.sugarsync.com/authorization"
    API_SAMPLE_USER_AGENT = "SugarSync API Sample/1.0"
    ACCESS_TOKEN_AUTH_REQUEST_TEMPLATE = """<tokenAuthRequest>
                                            <accessKeyId>%(accessKey)s</accessKeyId>
                                            <privateAccessKey>%(privateAccessKey)s</privateAccessKey>
                                            <refreshToken>%(refreshToken)s</refreshToken>
                                            </tokenAuthRequest>"""

    def __init__(self,token, expiration):
        self.token = token
        self.expiration = expiration

    def __str__(self):
        return self.token

    @staticmethod
    def getAccessToken(accessKeyId, privateAccessKey, refreshToken):
        
        def __get__expiration_date(response):
            # parse iso date string -> convert to utc -> get a naive datetime
            date_string = str(BeautifulSoup(response).authorization.expiration.string)
            return iso8601.parse_date(date_string).astimezone(pytz.utc).replace(tzinfo=None)

        request_body = xml.dom.minidom.parseString(AccessToken.ACCESS_TOKEN_AUTH_REQUEST_TEMPLATE % { "accessKey" : accessKeyId, "privateAccessKey" : privateAccessKey, "refreshToken" : refreshToken})

        http = httplib2.Http()
        resp, content = http.request(AccessToken.AUTH_ACCESS_TOKEN_API_URL, method='POST', body=request_body.toxml(), headers={"User-Agent" : AccessToken.API_SAMPLE_USER_AGENT, "Content-type": "application/xml; charset=UTF-8"})

        try:
            return AccessToken(resp["location"], __get__expiration_date(content))
        except:
            return None