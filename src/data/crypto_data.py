from matplotlib.axis import YAxis
from matplotlib.pyplot import figure, title
import requests
import pandas as pd
import pandas_ta as ta
import plotly.offline as py
import plotly.graph_objs as go
from plotly.graph_objects import Layout

class CryptoData:
    data = None
    symbol = None
    interval = None
    max_candles_list = None
    graph = None

    def __init__(self, symbol, interval, max_candles_list=None):
        self.candles_list = max_candles_list if max_candles_list is not None else 1000
        self.symbol = symbol
        self.interval = interval
        self.max_candles_list = max_candles_list

        request = requests.get('https://api.binance.com/api/v3/klines', params={
            'symbol': symbol,
            'interval': interval,
            'limit': max_candles_list,
        })

        raw_data_json = request.json()
        raw_data_columns = {'High': [], 'Low': [], 'Open': [], 'Close': []}

        for raw in raw_data_json:
            raw_data_columns['High'].append(float(raw[2]))
            raw_data_columns['Open'].append(float(raw[1]))
            raw_data_columns['Low'].append(float(raw[3]))
            raw_data_columns['Close'].append(float(raw[4]))

        self.data = pd.DataFrame(raw_data_columns).tail(max_candles_list)
        self.elaborateGraph()

    def elaborateGraph(self):
        layout = Layout(plot_bgcolor='rgba(0, 0, 0, 1)')

        candles = go.Candlestick(x=self.data.index, open=self.data.Open, high=self.data.High, low=self.data.Low, close=self.data.Close)

        self.graph = go.Figure(data=candles, layout=layout)
        self.graph.update_layout(
            showlegend=False,
            xaxis=dict(showgrid=False, rangeslider=dict(visible=False)),
            yaxis=dict(showgrid=False),
            title=str(self.symbol) + " " + str(self.interval)
        )

    def showGraph(self):
        self.graph.show()


