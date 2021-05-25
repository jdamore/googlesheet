import os
import flask
import google_auth_oauthlib

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

OAUTH2_CLIENT = os.getenv('GOOGLESHEET_OAUTH2_CLIENT')
OAUTH2_SCOPES = [
        'https://www.googleapis.com/auth/drive.readonly',
        'https://www.googleapis.com/auth/spreadsheets.readonly']


def is_logged_in():
    return ('oauth2_credentials' in flask.session)


def is_logging_in():
    return ('oauth2' in flask.request.endpoint)


def enforce_login():
    if not is_logged_in() and not is_logging_in():
        flask.session['request_full_path'] = flask.request.full_path
        return flask.redirect(flask.url_for('oauth2.index'))


def create_flow(state=None):
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        OAUTH2_CLIENT, 
        scopes=OAUTH2_SCOPES,
        state=state)
    flow.redirect_uri = flask.url_for('oauth2.callback', _external=True)
    return flow


def index():
    flow = create_flow()
    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true')
    flask.session['oauth2_state'] = state
    return flask.redirect(authorization_url)


def callback():
    flow = create_flow(flask.session['oauth2_state'])
    flow.fetch_token(authorization_response=flask.request.url)
    flask.session['oauth2_credentials'] = oauth2_credentials_to_dict(flow.credentials)
    return flask.redirect(flask.session['request_full_path'])


def oauth2_credentials_to_dict(credentials):
    return {'token': credentials.token,
          'refresh_token': credentials.refresh_token,
          'token_uri': credentials.token_uri,
          'client_id': credentials.client_id,
          'client_secret': credentials.client_secret,
          'scopes': credentials.scopes}
