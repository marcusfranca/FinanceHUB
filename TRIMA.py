base_url_trima = 'https://www.alphavantage.co/query?function=TRIMA&symbol=IBM&interval=weekly&time_period=10&series_type=open&apikey=demo'

api_key = 'RWYGAC4N5248TJ54'
symbol = 'IBM'

params_trima_hight = {
        'function': 'TRIMA',
        'interval':'monthly',
        'symbol': symbol,
        'series_type':'hight',  #close, high, low
        'apikey': api_key
    }
params_trima_low = {
        'function': 'TRIMA',
        'interval':'monthly',
        'symbol': symbol,
        'series_type':'low',  #close, high, low
        'apikey': api_key
    }
params_trima_close = {
        'function': 'TRIMA',
        'interval':'monthly',
        'symbol': symbol,
        'series_type':'close',  #close, high, low
        'apikey': api_key
    }