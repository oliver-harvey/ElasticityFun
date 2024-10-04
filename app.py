import dash
from dash import dcc, html
import plotly.graph_objects as go

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                go.Scatter(x=[1, 2, 3, 4], y=[10, 11, 12, 13], mode='lines', name='Buy Units'),
                go.Scatter(x=[1, 2, 3, 4], y=[15, 14, 13, 12], mode='lines', name='Sell Units')
            ],
            'layout': go.Layout(title='Units Sold and Bought vs Price', xaxis={'title': 'Price'}, yaxis={'title': 'Units'})
        }
    )
])

    if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050, debug=False)

