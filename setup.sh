#set -e
conda create -y -n googlesheet python=3.6.3
conda install -n googlesheet pip
conda activate googlesheet
python3 -m pip install --upgrade pip
python3 -m pip install Django
echo
