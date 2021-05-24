import os
import flask

from .controllers import home, oauth2, googlesheet

def create_app(test_config=None):

    app = flask.Flask(__name__, instance_relative_config=True)
    app.secret_key = 'REPLACE ME - this value is here as a placeholder.'
    app.url_map.strict_slashes = False
    app.add_url_rule('/', endpoint='home', view_func=home.index)
    app.add_url_rule('/googlesheet', endpoint='googlesheet', view_func=googlesheet.index)
    app.add_url_rule('/oauth2', endpoint='oauth2', view_func=oauth2.index)
    app.add_url_rule('/oauth2/callback', endpoint='oauth2_callback', view_func=oauth2.callback)

    @app.before_request
    def check_oauth2_credentials():
        if ('oauth2_credentials' not in flask.session) and ('oauth2' not in flask.request.endpoint):
            flask.session['request_full_path'] = flask.request.full_path
            return flask.redirect(flask.url_for('oauth2'))

    return app