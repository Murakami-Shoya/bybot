import logging
import sys

import settings

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

if __name__ == "__main__":
    print(settings.api_key)
    print(settings.api_secret)
    