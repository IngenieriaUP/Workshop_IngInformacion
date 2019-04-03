# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[

html.H1(children='Pacifico Telcom', style={'text-align': 'center'}),



html.Div([
    html.P('¿El cliente tiene línea múltiple?'),
    html.P('¿El cliente ha contratado soporte técnico de la empresa?'),
    html.P('¿El cliente ha solicitado servicio de internet?'),
    html.P('¿El cliente ha solicitado servicio de TV por cable?'),
    html.P('¿El cliente ha solicitado un plan de seguridad informática?'),
    html.P('¿El cliente tiene un servicio de streaming de películas?'),
    html.P('¿El cliente es jubilado?'),
    html.P('¿Cuál es el medio de pago que más usa?'),
    html.P('¿Cuál es el tipo de facturación que prefiere?'),
    html.P('¿Cuántos años tiene el cliente con la empresa?'),
    html.P('¿Qué tipo de contrato tiene?')
], style={'float': 'left', 'width':'40%'}),

html.Div([
    dcc.RadioItems(
        options=[
            {'label': 'Yes', 'value': 'NYC'},
            {'label': 'No', 'value': '0'},
        ],
        value='MTL',
        labelStyle={'display': 'inline-block','margin-bottom': '0.75rem'}
    ),
    dcc.RadioItems(
        options=[
            {'label': 'Yes', 'value': 'NYC'},
            {'label': 'No', 'value': 'MTL'},
        ],
        value='MTL',
        labelStyle={'display': 'inline-block','margin-bottom': '0.75rem'}
    ),
    dcc.RadioItems(
        options=[
            {'label': 'Yes', 'value': 'NYC'},
            {'label': 'No', 'value': 'MTL'},
        ],
        value='MTL',
        labelStyle={'display': 'inline-block','margin-bottom': '0.75rem'}
    ),
    dcc.RadioItems(
        options=[
            {'label': 'Yes', 'value': 'NYC'},
            {'label': 'No', 'value': 'MTL'},
        ],
        value='MTL',
        labelStyle={'display': 'inline-block','margin-bottom': '0.75rem'}
    ),
    dcc.RadioItems(
        options=[
            {'label': 'Yes', 'value': 'NYC'},
            {'label': 'No', 'value': 'MTL'},
        ],
        value='MTL',
        labelStyle={'display': 'inline-block','margin-bottom': '0.75rem'}
    ),
    dcc.RadioItems(
        options=[
            {'label': 'Yes', 'value': 'NYC'},
            {'label': 'No', 'value': 'MTL'},
        ],
        value='MTL',
        labelStyle={'display': 'inline-block','margin-bottom': '0.75rem'}
    ),
    dcc.RadioItems(
        options=[
            {'label': 'Yes', 'value': 'NYC'},
            {'label': 'No', 'value': 'MTL'},
        ],
        value='MTL',
        labelStyle={'display': 'inline-block','margin-bottom': '0.75rem'}
    ),
    dcc.Dropdown(
        options=[
            {'label': 'Cheque electrónico', 'value': '0'},
            {'label': 'Cheque enviado', 'value': '1'},
            {'label': 'Transferencia', 'value': '2'},
            {'label': 'Tarjeta de credito', 'value': '3'},
        ],
        value='MTL'
    ),
    dcc.Dropdown(
        options=[
            {'label': 'Mensual', 'value': 'NYC'},
            {'label': 'Anual', 'value': 'MTL'},
            {'label': 'Bienal', 'value': 'SF'},
        ],
        value='MTL'
    ),
    dcc.Dropdown(
        options=[
            {'label': '0', 'value': '0'},
            {'label': '1', 'value': '1'},
            {'label': '2', 'value': '2'},
            {'label': '3', 'value': '3'},
            {'label': '4', 'value': '4'},
            {'label': '5', 'value': '5'},
            {'label': '6', 'value': '6'},
        ],
        value='MTL'
    ),


], style={'float': 'left', 'width':'15%'}),

html.H1(children='',style={'clear':'left'}),

html.Button('Submit', id='button',  style={'clear': 'both'})

])

if __name__ == '__main__':
    app.run_server(debug=True)