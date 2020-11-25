from typing import Dict, Text, Any
from oandapyV20 import API
import oandapyV20.endpoints.instruments as instruments
import oandapyV20.endpoints.accounts as accounts
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
import calendar
from backports.datetime_fromisoformat import MonkeyPatch
from tradingsignal.exchange.exchange import Exchange

MonkeyPatch.patch_fromisoformat()


class OANDA(Exchange):
    def __init__(self, exchange_config: Dict[Text, Any] = {}) -> None:
        super().__init__(exchange_config)
        self._account_id = exchange_config.get("account_id", "")
        self._access_token = exchange_config.get("access_token", "")
        self.instruments = exchange_config.get("instruments", "")
        self.api = API(access_token=self._access_token, environment="practice")

    def get_instruments(self):
        # AUD_USD,EUR_USD,GBP_USD,NZD_USD,USD_CAD,USD_CHF,USD_JPY,
        # params = { "instruments": "Gold" }
        #
        r = accounts.AccountInstruments(accountID=self._account_id)
        res = self.api.request(r)
        return res['instruments']

    def get_candle_data_from_oanda(self, instrument, date_from, date_to, granularity):
        params = {
            "from": date_from.isoformat(),
            "to": date_to.isoformat(),
            "granularity": granularity,
        }
        r = instruments.InstrumentsCandles(instrument=instrument, params=params)
        return self.api.request(r)

    @staticmethod
    def oanda_json_to_list(json_res):
        data = []
        for res in json_res['candles']:
            data.append([
                datetime.fromisoformat(res['time'][:19]),
                float(res['mid']['o']),
                float(res['mid']['h']),
                float(res['mid']['l']),
                float(res['mid']['c']),
                float(res['volume']),
            ])
        return data

    def get_market_data(self, instrument: Text, granularity="H1", count=1000):
        """ fetch candle data from oanda
        :param instrument: string (required) the instrument to fetch candle data for
        :param granularity: The granularity of the candlesticks to fetch
        :param count: The number of candlesticks to return in the response. [default=1000, maximum=5000]
        :return: A data-frame of historical OHCLV data
        """
        params = {
            "count": count,
            "granularity": granularity
        }
        r = instruments.InstrumentsCandles(instrument=instrument, params=params)
        res = self.api.request(r)
        market_data = self.oanda_json_to_list(res)
        df = pd.DataFrame(market_data)
        df.columns = ['datetime', 'open', 'high', 'low', 'close', 'volume']
        df = df.set_index('datetime')
        return df

