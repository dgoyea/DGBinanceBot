import os
import time
import datetime
import configparser
import DGBinanceInterface
import DGBinanceCalls


def ts():
    '''
    Timestamp function
    '''   
    d = datetime.datetime.now()
    return datetime.datetime.strftime(d, "%Y-%m-%d %H:%M:%S")


def getConfig():
    '''
    Retreive configuration from config file.
    '''    
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
    
    return(config)

def main():
    '''
    Main function to control flow of Bot
    '''       
    config = getConfig()

    # Get keys from config file. Keys are generated from poloniex for API connection.
    api_key = config['Binance']['APIKey']
    api_secret = config['Binance']['Secret']
    
    DGBinanceCall = DGBinanceCalls.DGBinanceCaller(api_key, api_secret)

    DGBB_Interface = DGBinanceInterface.DGBinanceMain()
    
    print('end addfdadssf')
    
    
if __name__ == "__main__":
    main()