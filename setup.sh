# Setup Virtual Env
SCRIPTPATH="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
python3 -m venv $SCRIPTPATH/.venv
chmod +x $SCRIPTPATH/.venv/bin/activate
chmod +x $SCRIPTPATH/.venv/bin/pip3
source $SCRIPTPATH/.venv/bin/activate

# Install dependencies
$SCRIPTPATH/.venv/bin/pip3 install --upgrade pip
$SCRIPTPATH/.venv/bin/pip3 install django
$SCRIPTPATH/.venv/bin/pip3 install google-api-python-client
$SCRIPTPATH/.venv/bin/pip3 install google-auth-httplib2
$SCRIPTPATH/.venv/bin/pip3 install google-auth-oauthlib

# Set program environment variables
export GOOGLESHEET_OAUTH2_CLIENT="${SCRIPTPATH}/googlesheet-oauth2-client.json"
echo set GOOGLESHEET_OAUTH2_CLIENT to $GOOGLESHEET_OAUTH2_CLIENT
