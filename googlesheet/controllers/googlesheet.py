import flask
import google.oauth2.credentials
import googleapiclient.discovery

SPREADSHEET_ID = '1D1UxlZCocTj5UTnssNe0rSOH4BRPf014yZYxCCuNiqg'
SPREADSHEET_RANGE = 'Data!A2:E'

def index():
    oauth2_credentials = google.oauth2.credentials.Credentials(**flask.session['oauth2_credentials'])
    service = googleapiclient.discovery.build('sheets', 'v4', credentials=oauth2_credentials)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=SPREADSHEET_RANGE).execute()
    values = result.get('values', [])

    if not values:
         return 'No values in Spreadsheet ' + SPREADSHEET_ID
    else:
        return 'Finished reading spreadsheet %s: first row is %s' % (SPREADSHEET_ID, values[0])