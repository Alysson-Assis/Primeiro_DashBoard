# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)


df = pd.read_excel('Vendas.xlsx')

fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
opcoes = list(df['ID Loja'].unique())
opcoes.append('Todas as Lojas')

# layout para o HTML
app.layout = html.Div(children=[       ## Por ser uma lista de itens é necessário colocar a virgula no final do comando
    
    html.H1(children='Faturamento das lojas'),
    html.H2(children='Gráfico com o Faturamento de Todos os Produtos separados por Lojas'),

    html.Div(children='''
        Obs: Esse gráfico mostra a quantidade de produtos vendidos, não o faturamento.
    '''),
    html.Div(id='texto'),

# Layout para os graficos
    dcc.Dropdown(opcoes, value='Todas as Lojas', id='lista_loja'),
    dcc.Graph(
        id='grafico_quantidade_vendas',
        figure=fig
    )
])

@app.callback(
    Output('grafico_quantidade_vendas', 'figure'),
    Input('lista_loja', 'value')
)
def update_output(value):
    if value == 'Todas as Lojas':
        fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    else:
        tabela_filtrada = df.loc[df['ID Loja']==value, :]
        fig = px.bar(tabela_filtrada, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    return fig

if __name__ == '__main__':
    app.run(debug=True)