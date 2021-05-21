import flask

def index():
    print('hello_home_controller')
    if 'oauth2_credentials' not in flask.session:
        return flask.redirect('oauth2')
    return flask.redirect('googlesheet')