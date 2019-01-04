# awm_backend_flask

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)

## Requirements

python 3 or newer

Mysql

## Installation

You can use docker to install backend service or just install on your computer

Build with docker

```sh
docker build -t backend .
docker run -p 5000:5000 backend
```

Download and install Python3

cd to your project directory

Install virtualenv

```sh
[pip or pip3] install virtualenv
```

After finish install

```sh
virtualenv venv
```

This will create a folder holds your environment.

Then, input

```sh
source venv/bin/activate
pip install -r requirements.txt
```

To leave virtual environment

```sh
deactivate
```

Config your database address from conf_example.py to conf.py

```sh
config/conf_example.py
```

Init Database

```sh
make init
```

## Usage

When ever you reboot or leave virtual environment,\
you need to activate virtual environment again:

```sh
source venv/bin/activate
```

To start dev server

```sh
make dev
```

To test your server

```sh
make test
```

To clean up pycache

```sh
make clean-pyc
```
