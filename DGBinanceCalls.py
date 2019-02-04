'''
Created on Feb 3, 2019

@author: David Goyea
Class to manage client and calls to Binance.
This class utilizes the binance wrapper from https://github.com/sammchardy/python-binance
'''
from binance.client import Client

class DGBinanceCaller:
    '''
    classdocs
    '''


    def __init__(self, api_key, api_secret):
        '''
        Constructor
        '''
        self.api_key = api_key
        self.api_secret = api_secret
        
        # Create a Binance client using the Binance wrapper
        # client = Client()
    
    # get ticker data
#     symbol1 = config['SymbolsOfInterest']['Symbol1']
#     eos_info = client.get_symbol_info(symbol1)
#     eos_depth = client.get_order_book(symbol=symbol1)
#     eos_candles = client.get_klines(symbol=symbol1, interval=Client.KLINE_INTERVAL_30MINUTE)
#     eos_ticker = client.get_ticker(symbol=symbol1)
# 
#     
#     print(eos_info)
#     print(eos_depth)
#     print(eos_candles)
#     print(eos_ticker)
#     print(eos_ticker['lastPrice'])