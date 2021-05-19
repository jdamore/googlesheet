set -e

SCRIPTPATH="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
chmod +x $SCRIPTPATH/.venv/bin/flask

export FLASK_APP=googlesheet
export FLASK_ENV=development
export FLASK_RUN_PORT=8000
$SCRIPTPATH/.venv/bin/flask run


echo
