import logging
import sys

import settings
from pybit import spot

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

if __name__ == "__main__":
    session = spot.HTTP(
        endpoint="https://api-testnet.bybit.com",
        api_key=settings.api_key,
        api_secret=settings.api_secret
    )

    print(session.get_wallet_balance())