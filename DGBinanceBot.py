import os
import time
import datetime
import configparser
from binance.client import Client

def ts():
    d = datetime.datetime.now()
    return datetime.datetime.strftime(d, "%Y-%m-%d %H:%M:%S")


def main():
    print('hi')
  
    # Get configuration from ini file.
    cfgfile = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..\DGBinanceBotConfig\DGBinanceBotConfig.ini')
    config = configparser.ConfigParser()
    
    if os.path.isfile(cfgfile):
        print(ts() + ': Using ini file: ' + cfgfile)
    else:
        print(ts() + ': No ini file found.')
        quit()
                
    try:
        print(ts() + ': Reading config file.')
        config.read(cfgfile)
        
    except:
        print(ts() + ': Could not read config file.')
    
    # Get keys from config file. Keys are generated from poloniex for API connection.
    api_key = config['Binance']['APIKey']
    api_secret = config['Binance']['Secret']

    # Create a Binance client using the Binance wrapper
    client = Client(api_key, api_secret)
    
    # get ticker data
    symbol1 = config['SymbolsOfInterest']['Symbol1']
    eos_info = client.get_symbol_info(symbol1)
    eos_depth = client.get_order_book(symbol=symbol1)
    eos_candles = client.get_klines(symbol=symbol1, interval=Client.KLINE_INTERVAL_30MINUTE)
    eos_ticker = client.get_ticker(symbol=symbol1)

    
    print(eos_info)
    print(eos_depth)
    print(eos_candles)
    print(eos_ticker)
    print(eos_ticker['lastPrice'])
    
    print('end addfdadssf')
    
    
if __name__ == "__main__":
    main()