api_key = 'RWYGAC4N5248TJ54'
symbol = 'IBM'
base_url_sma ='https://www.alphavantage.co/query?function=SMA&symbol=IBM&interval=weekly&time_period=10&series_type=open&apikey=demo'

params_sma_hight= {
        'function': 'SMA',
        'symbol': symbol,
        'interval': 'monthly',
        'time_period': 2,
        'series_type':'hight',  #close, high, low
        'apikey': api_key
    }
params_sma_low= {
        'function': 'SMA',
        'symbol': symbol,
        'interval': 'monthly',
        'time_period': 2,
        'series_type':'low',  #close, high, low
        'apikey': api_key
    }
params_sma_close= {
        'function': 'SMA',
        'symbol': symbol,
        'interval': 'monthly',
        'time_period': 2,
        'series_type':'close',  #close, high, low
        'apikey': api_key
    }