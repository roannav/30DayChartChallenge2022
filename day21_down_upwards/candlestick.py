# candlestick financial chart
# A candlestick shows the open, high, low, and close of a stock
# for a given timeframe.  Increasing candles, where the close is
# higher than the open, are drawn in green.  Decreasing candles
# are drawn in red.

# requires kaleido to save the image to a file:
# pip install -U kaleido

import plotly
from plotly import graph_objs as go

import pandas as pd
from datetime import datetime

# Read in the data
# .csv file has a header.
# index_col default is None.
df = pd.read_csv('yahoo_sp_data_cleaned.csv')
print(df.head(2))
print(df.describe())

fig = go.Figure(data=[go.Candlestick(
    x=df['Date'],
    open=df['Open'],
    high=df['High'],
    low=df['Low'],
    close=df['Close*']
)])

txt = [
    dict( x='2018-04-04', y=0.05, xref='x', yref='paper',
          bgcolor='darkgreen', font=dict(color='white', size=16),
          showarrow=False, xanchor='left', text='up ⬆️'),
    dict( x='2019-04-04', y=0.05, xref='x', yref='paper',
          bgcolor='darkgreen', font=dict(color='white', size=32),
          showarrow=False, xanchor='left', text='up ⬆️'),
    dict( x='2020-07-04', y=0.05, xref='x', yref='paper',
          bgcolor='darkgreen', font=dict(color='white', size=64),
          showarrow=False, xanchor='left', text='up ⬆️'),
    dict( x='2021-12-01', y=0.65, xref='x', yref='paper',
          bgcolor='maroon', font=dict(color='white', size=16),
          showarrow=False, xanchor='left', text='down ⬇️')
]

fig.update_layout(
    # This is the white box outside the chart 
    margin = dict(t=50, l=80, r=50, b=60),
    title={
        'text': 'S&P 500',
        'x': 0.5,
        'xanchor': 'center',
        'y': 0.97,
        'yanchor': 'top',
        'font': { 
            'family': 'Times New Roman',
            #'color': 'blue',
            'size': 28
        }
    },
    yaxis_title='Price (Currency in USD)',
    annotations=txt
)

fig.add_annotation(text="Data: Yahoo Finance  Viz: @roannav",
                   xref='paper', yref='paper',
                   yanchor="top",
                   x=0,
                   y = -0.4,
                   showarrow=False)

fig.write_image("candlestick.png")
#fig.show()
