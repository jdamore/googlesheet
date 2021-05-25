import os
import flask

from .controllers import home, oauth2, googlesheet

def create_app(test_config=None):

    # App initialisation
    app = flask.Flask(__name__, instance_relative_config=True)
    app.secret_key = 'REPLACE ME - this value is here as a placeholder.'
    app.url_map.strict_slashes = False

    # Routing
    app.add_url_rule('/', endpoint='home.index', view_func=home.index)
    app.add_url_rule('/googlesheet', endpoint='googlesheet.index', view_func=googlesheet.index)
    app.add_url_rule('/oauth2', endpoint='oauth2.index', view_func=oauth2.index)
    app.add_url_rule('/oauth2/callback', endpoint='oauth2.callback', view_func=oauth2.callback)

    # Request pre and post processors
    app.before_request(oauth2.enforce_login)

    return app