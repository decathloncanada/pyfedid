#!/usr/bin/python

from .module import FedidMod


class FedidHelper:

    @staticmethod
    def create_fedid_token():
        """
        Create and return the new FEDID access token
        :return: str
        """
        fedid = FedidMod()
        fedid.set_token()
        return fedid.get_token()
