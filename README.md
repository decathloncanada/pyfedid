## Version

* 2019-04-06 : 1.0.0

## Authors

* __Sylvain Lemoine__ sylvain.lemoine@decathlon.com

## Services used

* [Python 3](https://www.python.org/)
* [Pip](https://pypi.org/project/pip/)

## Introduction

This Python library is used for the interaction with the Decathlon FEDID.

## Setup your system

* __Add environment variables__

```bash
echo "export DECA_FEDID_ENDPOINT=$VALUE" >> ~/.bashrc
echo "export DECA_FEDID_AUTHORIZATION_URL=$VALUE" >> ~/.bashrc
echo "export DECA_FEDID_TOKEN_URL=$VALUE" >> ~/.bashrc
echo "export DECA_FEDID_USERINFO_URL=$VALUE" >> ~/.bashrc
echo "export DECA_FEDID_CLIENT_ID=$VALUE" >> ~/.bashrc
echo "export DECA_FEDID_SECRET=$VALUE" >> ~/.bashrc
echo "export DECA_FEDID_LOGIN=$VALUE" >> ~/.bashrc
echo "export DECA_FEDID_PASSWORD=$VALUE" >> ~/.bashrc
source ~/.bashrc
```

## Installation

```bash
pip install -e git+https://github.com/decathloncanada/pyfedid.git#egg=pyfedid
```
