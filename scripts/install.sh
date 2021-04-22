#! /usr/bin/env bash

pyenv_loader='\nexport PATH="$HOME/.pyenv/bin:$PATH"\neval "$(pyenv init -)"\neval "$(pyenv virtualenv-init -)"\n'

type pyenv >/dev/null 2>&1
if [[ $? -ne 0 ]]; then
        sudo apt-get update \
        sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
        libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
        libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl &&
        curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash &&
                echo -e ${pyenv_loader} >>~/.bashrc &&
                source ~/.bashrc
fi

if [[ $? -eq 0 ]]; then
        pyenv install 3.8.0 -s &&
        pyenv local 3.8.0 &&
        python -m pip install -r requirements.txt -q &&
        echo "Success"
fi
