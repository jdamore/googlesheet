import os

from flask import Flask, redirect, request, url_for
from googleapiclient.discovery import build
from .oauth2flow import Oauth2flow

SPREADSHEET_ID = '1D1UxlZCocTj5UTnssNe0rSOH4BRPf014yZYxCCuNiqg'
SPREADSHEET_RANGE = 'Data!A2:E'

# TODO: fix this
oauth2flow = Oauth2flow('http://localhost:8000/googlesheet')

def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)


    @app.route('/')
    def googlesheet():
        return redirect(oauth2flow.authorization_url)

    
    @app.route('/googlesheet')
    def oauth2callback():
        credentials = oauth2flow.fetch_credentials(request.args.get('code'))
        service = build('sheets', 'v4', credentials=credentials)

        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=SPREADSHEET_RANGE).execute()
        values = result.get('values', [])

        if not values:
            return 'No values in Spreadsheet ' + SPREADSHEET_ID
        else:
            return 'Finished reading spreadsheet %s: first row is %s' % (SPREADSHEET_ID, values[0])

    return app