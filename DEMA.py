base_url_dema ="https://www.alphavantage.co/query?function=DEMA&symbol=IBM&interval=weekly&time_period=10&series_type=open&apikey=demo"
api_key = 'RWYGAC4N5248TJ54'
symbol = 'IBM'

params_dema_hight = {
        'function': 'DEMA',
        'interval':'monthly',
        'symbol': symbol,
        'series_type':'hight',  #close, high, low
        'apikey': api_key
    }
params_dema_low = {
        'function': 'DEMA',
        'interval':'monthly',
        'symbol': symbol,
        'series_type':'low',  #close, high, low
        'apikey': api_key
    }
params_dema_close = {
        'function': 'DEMA',
        'interval':'monthly',
        'symbol': symbol,
        'series_type':'close',  #close, high, low
        'apikey': api_key
    }