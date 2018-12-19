# awm_backend_flask

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)

## Requirements

python 3 or newer

Mysql

## Installation

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

Config your database address in

```sh
app/main/config
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
