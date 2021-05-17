
import os
from django.conf import settings

from google_auth_oauthlib.flow import Flow


GOOGLESHEET_OAUTH2_CLIENT = os.getenv('GOOGLESHEET_OAUTH2_CLIENT')

SCOPES = [
        'https://www.googleapis.com/auth/drive.readonly',
        'https://www.googleapis.com/auth/spreadsheets.readonly']


'''
    Google Oauth2 Facade for Web Server auth.
    https://developers.google.com/identity/protocols/oauth2/web-server
'''
class Oauth2flow(object):

    def __init__(self, redirect_uri):
        flow = Flow.from_client_secrets_file(
            GOOGLESHEET_OAUTH2_CLIENT, 
            scopes=SCOPES)
        self._flow = flow
        self._flow.redirect_uri = redirect_uri
    
    @property
    def flow(self):
        return self._flow

    @property
    def authorization_url(self):
        authorization_url, state = self._flow.authorization_url(
            access_type='offline',
            include_granted_scopes='true')
        return authorization_url

    def fetch_credentials(self, code):
        self._flow.fetch_token(code=code)
        return self._flow.credentials
