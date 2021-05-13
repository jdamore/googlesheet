
from django.http import HttpResponse

import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = os.getenv('GOOGLESHEET_SERVICE_ACCOUNT')

SCOPES = [
        'https://www.googleapis.com/auth/drive',
        'https://www.googleapis.com/auth/drive.file',
        'https://www.googleapis.com/auth/drive.readonly',
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/spreadsheets.readonly']
        
# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = '1D1UxlZCocTj5UTnssNe0rSOH4BRPf014yZYxCCuNiqg'
SPREADSHEET_RANGE = 'Data!A2:E'


def index(request):

    # Authenticate
    creds = None
    if os.path.exists(SERVICE_ACCOUNT_FILE):
        creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    else:
        return HttpResponse('Cannot find file ' + SERVICE_ACCOUNT_FILE)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=SPREADSHEET_RANGE).execute()
    values = result.get('values', [])

    if not values:
        return HttpResponse('No values in Spreadsheet ' + SPREADSHEET_ID)
    else:
        return HttpResponse('Finished reading spreadsheet %s: first row is %s' % (SPREADSHEET_ID, values[0]))
