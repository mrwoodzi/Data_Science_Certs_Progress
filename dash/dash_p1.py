from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)


colors = {
    'background': '#4B0082',
    'text': '#FF0000',
}

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
    })

fig = px.bar(df, 
             x="Fruit", 
             y="Amount", 
             color="City", 
             barmode="group")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
    )

app.layout = html.Div(
        children=[html.H1(children='Hello Dash',
                          style={
                              'textAlign': 'center',
                              # 'color': colors['text']
                              }),
                  html.Div(children=''' Dash: A web appliation framework for your data. ''',
                           style={
                               'textAlign': 'center',
                               # 'color': colors['text']
                               }),
                  dcc.Graph(id='example-graph',
                            figure=fig),
                            ])

if __name__ == '__main__':
    app.run(debug=True)