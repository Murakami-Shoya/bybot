import logging

from pybit import spot

class HTTPClient(object):
    def __init__(self, api_key, api_secret, is_test) :
        self.api_key = api_key
        self.api_secret = api_secret
        if(is_test):
            self.endpoint = "https://api-testnet.bybit.com"
        else:
            self.endpoint = "https://api.bybit.com"
        
        self.session_auth = spot.HTTP(
            endpoint=self.endpoint,
            api_key=self.api_key,
            api_secret=self.api_secret
        )
    
    def get_wallet_balance(self):
        self.session_auth.get_wallet_balance()