from django.http import HttpResponse
from django.shortcuts import redirect
from django.conf import settings

from googleapiclient.discovery import build

from .oauth2flow import Oauth2flow

SPREADSHEET_ID = '1D1UxlZCocTj5UTnssNe0rSOH4BRPf014yZYxCCuNiqg'
SPREADSHEET_RANGE = 'Data!A2:E'

# TODO: fix this
oauth2flow = Oauth2flow('http://localhost:8000/googlesheet/oauth2callback')

'''
    Entry point
    Starts the Oauth2 authorization by redirecting 
    to the Google account login screen
'''
def index(request):
    return redirect(oauth2flow.authorization_url)

'''
    Google Oauth2 Callback
    Checks the Oauth2 authorization and serves the data
'''
def oauth2callback(request):

    credentials = oauth2flow.fetch_credentials(request.GET.get('code'))
    service = build('sheets', 'v4', credentials=credentials)

    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=SPREADSHEET_RANGE).execute()
    values = result.get('values', [])

    if not values:
        return HttpResponse('No values in Spreadsheet ' + SPREADSHEET_ID)
    else:
        return HttpResponse('Finished reading spreadsheet %s %s: first row is %s' % (settings.BASE_DIR, SPREADSHEET_ID, values[0]))