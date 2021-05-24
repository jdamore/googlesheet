# Setup Virtual Env
PROJECT_PATH="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
python3 -m venv $PROJECT_PATH/.venv
chmod +x $PROJECT_PATH/.venv/bin/activate
chmod +x $PROJECT_PATH/.venv/bin/pip3
source $PROJECT_PATH/.venv/bin/activate

$PROJECT_PATH/.venv/bin/pip3 install --upgrade pip

# Install runtime dependencies
$PROJECT_PATH/.venv/bin/pip3 install 'flask==2.0.1'
$PROJECT_PATH/.venv/bin/pip3 install 'google-api-python-client==2.5.0'
$PROJECT_PATH/.venv/bin/pip3 install 'google-auth-oauthlib==0.4.4'

# Set program environment variables
export GOOGLESHEET_OAUTH2_CLIENT="${PROJECT_PATH}/googlesheet-oauth2-client.json"
echo set GOOGLESHEET_OAUTH2_CLIENT to $GOOGLESHEET_OAUTH2_CLIENT