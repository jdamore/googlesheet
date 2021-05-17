SCRIPTPATH="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

python3 -m venv $SCRIPTPATH/.venv
chmod +x $SCRIPTPATH/.venv/bin/activate
. $SCRIPTPATH/.venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install django
python3 -m pip install google-api-python-client
python3 -m pip install google-auth-httplib2
python3 -m pip install google-auth-oauthlib

export GOOGLESHEET_OAUTH2_CLIENT="${SCRIPTPATH}/googlesheet-oauth2-client.json"
echo set GOOGLESHEET_OAUTH2_CLIENT to $GOOGLESHEET_OAUTH2_CLIENT
