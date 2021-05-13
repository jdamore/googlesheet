set -e
python3 -m pip install --upgrade pip
python3 -m pip install django
python3 -m pip install google-api-python-client
python3 -m pip install google-auth-httplib2
python3 -m pip install google-auth-oauthlib
export GOOGLESHEET_SERVICE_ACCOUNT="/Users/jdamore/dev/projects/googlesheet/googlesheet-service-account.json"

