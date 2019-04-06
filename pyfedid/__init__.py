#!/usr/bin/env python

import os


class FedidConfig:
    """
    FEDID settings initialization
    """

    def __init__(self):
        self._warnings = list()
        self._fields_config = {
            'DECA_FEDID_ENDPOINT': os.getenv('DECA_FEDID_ENDPOINT'),
            'DECA_FEDID_AUTHORIZATION_URL': os.getenv('DECA_FEDID_AUTHORIZATION_URL'),
            'DECA_FEDID_TOKEN_URL': os.getenv('DECA_FEDID_TOKEN_URL'),
            'DECA_FEDID_USERINFO_URL': os.getenv('DECA_FEDID_USERINFO_URL'),
            'DECA_FEDID_CLIENT_ID': os.getenv('DECA_FEDID_CLIENT_ID'),
            'DECA_FEDID_SECRET': os.getenv('DECA_FEDID_SECRET'),
            'DECA_FEDID_LOGIN': os.getenv('DECA_FEDID_LOGIN'),
            'DECA_FEDID_PASSWORD': os.getenv('DECA_FEDID_PASSWORD'),
        }

        self._mandatory_config = {
            'DECA_FEDID_ENDPOINT': {
                'label': 'DECA_FEDID_ENDPOINT',
                'type': 'text',
                'size': '200',
                'required': True,
                'warning': 'No endpoint provided.',
                'desc': 'Never finish by a /. Endpoint of Fedid : {}'.format(
                    self._fields_config.get('DECA_FEDID_ENDPOINT')),
            },
            'DECA_FEDID_AUTHORIZATION_URL': {
                'label': 'DECA_FEDID_AUTHORIZATION_URL',
                'type': 'text',
                'size': '200',
                'required': True,
                'warning': 'No authorization url provided.',
                'desc': 'Start with a /. Default : /as/authorization.oauth2',
            },
            'DECA_FEDID_TOKEN_URL': {
                'label': 'DECA_FEDID_TOKEN_URL',
                'type': 'text',
                'size': '200',
                'required': True,
                'warning': 'No token url provided.',
                'desc': 'Start with a /. Default : /as/token.oauth2',
            },
            'DECA_FEDID_USERINFO_URL': {
                'label': 'DECA_FEDID_USERINFO_URL',
                'type': 'text',
                'size': '200',
                'required': True,
                'warning': 'No userinfo url provided.',
                'desc': 'Start with a /. Default : /idp/userinfo.openid',
            },
            'DECA_FEDID_CLIENT_ID': {
                'label': 'DECA_FEDID_CLIENT_ID',
                'type': 'text',
                'size': '200',
                'required': True,
                'warning': 'No client_id provided.',
                'desc': 'Client_id is created by MyDecathlon Team.',
            },
            'DECA_FEDID_SECRET': {
                'label': 'DECA_FEDID_SECRET',
                'type': 'text',
                'size': '200',
                'required': True,
                'warning': 'No secret provided.',
                'desc': 'Secret is created by MyDecathlon Team.',
            },
            'DECA_FEDID_LOGIN': {
                'label': 'DECA_FEDID_LOGIN',
                'type': 'text',
                'size': '200',
                'required': True,
                'warning': 'No login provided.',
                'desc': 'Login is created by IAM Team.',
            },
            'DECA_FEDID_PASSWORD': {
                'label': 'DECA_FEDID_PASSWORD',
                'type': 'text',
                'size': '200',
                'required': True,
                'warning': 'No password provided.',
                'desc': 'Password is created by IAM Team.',
            }
        }
        self._config_is_valid = False
        self.init()

    def init(self):
        """
        Initialize the configuration settings
        """
        for value in self._mandatory_config:
            if not self._fields_config.get(value) or self._fields_config.get(value) is None:
                self._warnings.append(self._mandatory_config.get(value).get('warning'))
        self._config_is_valid = len(self._warnings) == 0
