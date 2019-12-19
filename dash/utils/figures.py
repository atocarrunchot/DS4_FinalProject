import plotly.graph_objects as go
import plotly.express as px
from properties_utils import set_properties
import numpy as np

def update_sankey_plot(data):
    fig = go.Figure(data=[go.Sankey(
        valueformat = ".0f",
        valuesuffix = "TWh",
        # Define nodes
        node = dict(
          pad = 15,
          thickness = 15,
          line = dict(color = "black", width = 0.5),
          label =  data['data'][0]['node']['label'],
          color =  data['data'][0]['node']['color']
        ),
        # Add links
        link = dict(
          source =  data['data'][0]['link']['source'],
          target =  data['data'][0]['link']['target'],
          value =  data['data'][0]['link']['value'],
          label =  data['data'][0]['link']['label']
      ))])

    fig.update_layout(title_text="Energy forecast for 2050<br>Source: Department of Energy & Climate Change, Tom Counsell via <a href='https://bost.ocks.org/mike/sankey/'>Mike Bostock</a>",
                      font_size=10)
    return fig


def sunburst_plot(data, labels, parents, values):
    labels = data[labels].values
    parents = data[parents].values
    values = data[values].values

    # Get data
    lab = ['Energy Price']
    par = ['']
    gain = [0]

    for val2 in data.dataset.unique():
        for val1 in data.region.unique():
            val_zero = data[(data['dataset'] == val2) & (data['region'] == val1)]['gain'].sum()
            if val_zero > 0:
                lab.append(val1)
                par.append(val2)
                gain.append(val_zero)

        lab.append(val2)
        par.append('Energy Price')
        gain.append(data[data['dataset'] == val2]['gain'].sum())

    [print(x) for x in zip(par,lab,gain)]


    fig = go.Figure(
        go.Sunburst(
            # labels=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
            # parents=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve"],
            # values=[10, 14, 12, 10, 2, 6, 6, 4, 4],
             labels=lab,
             parents=par,
             values=gain,

        )
    )

    fig.update_layout(margin=dict(t=0, l=0, r=0, b=0))

    return fig


def update_bar_plot():

    animals=['giraffes', 'orangutans', 'monkeys']
    fig = go.Figure([go.Bar(x=animals, y=[20, 14, 23])])
    return fig

def update_candlestick_plot(data):

    fig = go.Figure(data=[go.Candlestick(x=data['fecha'],
                    open=data['open'], high=data['high'],
                    low=data['low'], close=data['close'])
                         ])

    fig.update_layout(xaxis_rangeslider_visible=False,margin = dict(t=0, l=55, r=50, b=30),template='plotly_white',height=400)
    return fig

def update_scatter_plot():
    tips = px.data.tips()
    fig = px.scatter(tips, x="total_bill", y="tip", trendline="ols")
    return fig
