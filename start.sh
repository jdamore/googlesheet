set -e

PROJECT_PATH="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
chmod +x $PROJECT_PATH/.venv/bin/flask

export FLASK_APP=src
export FLASK_ENV=development
export FLASK_RUN_PORT=8000
$PROJECT_PATH/.venv/bin/flask run