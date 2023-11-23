import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Criar subplots usando make_subplots
fig = make_subplots(rows=1, cols=2, subplot_titles=('Subplot 1', 'Subplot 2'))

# Adicionar gráfico de dispersão no Subplot 1
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 1, 2], mode='markers'), row=1, col=1)

# Adicionar gráfico de barras no Subplot 2
fig.add_trace(go.Bar(x=[1, 2, 3], y=[2, 5, 3]), row=1, col=2)

# Layout da aplicação Dash
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Dash com Subplots do Plotly"),
    dcc.Graph(figure=fig, id='subplot-fig')
])

if __name__ == '__main__':
    fig.write_html("subplotssss.html")
    app.run_server(debug=True)


