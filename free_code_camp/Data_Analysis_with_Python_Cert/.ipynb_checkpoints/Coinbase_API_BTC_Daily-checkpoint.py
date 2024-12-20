# this is from cyptodatadownload.com
# https://docs.cloud.coinbase.com/exchange/docs/requests
# https://algotrading101.com/learn/coinbase-pro-api-guide/#:~:text='%3A%20'197711129.46'%7D-,How%20to%20get%20historical%20data%20with%20Coinbase%20Pro%20API%3F,parameters%20of%20the%20API%20request.
# Coinbase_BTCUSD_dailydata.csv
import pandas as pd
import requests
import json

def fetch_daily_data(symbol):
    pair_split = symbol.split('/')  # symbol must be in format XXX/XXX ie. BTC/EUR
    symbol = pair_split[0] + '-' + pair_split[1]
    url = f'https://api.pro.coinbase.com/products/{symbol}/candles?granularity=86400'
    response = requests.get(url)
    if response.status_code == 200:  # check to make sure the response from server is good
        data = pd.DataFrame(json.loads(response.text), columns=['unix', 'low', 'high', 'open', 'close', 'volume'])
        data['date'] = pd.to_datetime(data['unix'], unit='s')  # convert to a readable date
        data['vol_fiat'] = data['volume'] * data['close']      # multiply the BTC volume by closing price to approximate fiat volume
        if data is None:     # if we failed to get any data, print an error...otherwise write the fil
            print("Did not return any data from Coinbase for this symbol")
        else:
            data.to_csv(f'Coinbase_{pair_split[0] + pair_split[1]}_dailydata.csv', index=False)
    else:
        print("Did not receieve OK response from Coinbase API")


if __name__ == "__main__":
# we set which pair we want to retrieve data for
    pair = "BTC/USD"
    fetch_daily_data(symbol=pair)