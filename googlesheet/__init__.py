import os
import flask

from .controllers import home, oauth2, googlesheet

def create_app(test_config=None):

    print('hello_create_app')
    app = flask.Flask(__name__, instance_relative_config=True)
    app.secret_key = 'REPLACE ME - this value is here as a placeholder.'
    app.add_url_rule('/', 'home', view_func=home.index)
    app.add_url_rule('/googlesheet', 'googlesheet', view_func=googlesheet.index)
    app.add_url_rule('/oauth2', 'oauth2', view_func=oauth2.index)
    app.add_url_rule('/oauth2/callback', 'oauth2_callback', view_func=oauth2.callback)

    return app