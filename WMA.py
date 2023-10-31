
base_url_wma = "https://www.alphavantage.co/query?function=WMA&symbol=IBM&interval=weekly&time_period=10&series_type=open&apikey=demo"

api_key = 'RWYGAC4N5248TJ54'
symbol = 'IBM'


params_wma_hight = {
        'function': 'WMA',
        'symbol': symbol,
        'series_type':'hight',  #close, high, low
        'apikey': api_key
    }
params_wma_low = {
        'function': 'WMA',
        'symbol': symbol,
        'series_type':'low',  #close, high, low
        'apikey': api_key
    }
params_wma_close = {
        'function': 'WMA',
        'symbol': symbol,
        'series_type':'close',  #close, high, low
        'apikey': api_key
    }
