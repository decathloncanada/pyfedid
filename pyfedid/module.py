#!/usr/bin/env python

import os
import requests

from . import FedidConfig


class FedidMod(FedidConfig):
    """
    FEDID access token process
    """

    def __init__(self):
        super().__init__()
        self._access_token = None
        self._issuer = self._fields_config.get('DECA_FEDID_ENDPOINT')
        self._authorization_endpoint_url = '{}{}'.format(self._issuer,
                                                         self._fields_config.get('DECA_FEDID_AUTHORIZATION_URL'))
        self._token_endpoint_url = '{}{}'.format(self._issuer,
                                                 self._fields_config.get('DECA_FEDID_TOKEN_URL'))
        self._user_info_endpoint = '{}{}'.format(self._issuer,
                                                 self._fields_config.get('DECA_FEDID_USERINFO_URL'))
        self._client_id = self._fields_config.get('DECA_FEDID_CLIENT_ID')
        self._secret = self._fields_config.get('DECA_FEDID_SECRET')
        self._username = self._fields_config.get('DECA_FEDID_LOGIN')
        self._password = self._fields_config.get('DECA_FEDID_PASSWORD')
        self._proxies = {'http': os.getenv('DECATHLON_PROXY_HTTP'),
                         'https': os.getenv('DECATHLON_PROXY_HTTPS')}

    def set_token(self):
        """
        Create the FEDID access token
        """
        if not self._config_is_valid:
            raise Exception('FEDID module not configured')

        response = requests.post(url=self._token_endpoint_url,
                                 proxies=self._proxies,
                                 headers={'Accept-Encoding': 'gzip'},
                                 auth=requests.auth.HTTPBasicAuth(self._client_id, self._secret),
                                 data={'grant_type': 'password',
                                       'username': self._username,
                                       'password': self._password,
                                       'scope': 'openid profile'},
                                 verify=True)
        if response:
            if response.status_code == 200:
                data = response.json()
                if data.get('access_token') and data.get('token_type') and data.get('token_type') == 'Bearer':
                    self._access_token = data.get('access_token')
                else:
                    raise Exception('Error getting Bearer - no token found')
            else:
                raise Exception('Error getting Bearer - HTTP {}'.format(response.status_code))
        else:
            raise Exception('Error reaching FEDID')

    def get_token(self):
        """
        Get the FEDID access token
        :return: str
        """
        return self._access_token
