#!/usr/bin/env bash

#!/usr/bin/env bash

#Usa o Python3 se este existir
shopt -s expand_aliases
command -v python3 >/dev/null 2>&1 && alias python="python3"

python -m venv .venv

source .venv/bin/activate

python -m pip install --upgrade pip
pip install autopep8
pip install pytest

./run_tests.sh
