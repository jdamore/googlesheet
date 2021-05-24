set -e
export PROJECT_PATH="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
$PROJECT_PATH/.venv/bin/python3 -m unittest discover -s $PROJECT_PATH/testrc -p "*test.py" -vvv