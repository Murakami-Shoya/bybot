from pybit import spot
import settings


session_auth = spot.HTTP(
    settings.api_key,
    settings.api_secret,
    settings.is_test
)

# print(session_auth.get_wallet_balance())
print(type(settings.api_key))
print(type(settings.api_secret))
print(type(settings.is_test))