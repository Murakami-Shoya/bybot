import configparser

conf = configparser.ConfigParser()
conf.read('settings.ini')

# テストアカウントでの取引
api_key = conf['bybit']['api_key_test']
api_secret = conf['bybit']['api_secret_test']
is_test = True
# メインアカウントでの取引
# api_key = conf['bybit']['api_key_prod']
# api_secret = conf['bybit']['api_secret_prod']
# is_test = False
