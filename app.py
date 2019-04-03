# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import math

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[

    html.Link(href='https://fonts.googleapis.com/css?family=Courgette',rel='stylesheet'),

    html.H1(children="Clarofónica", style={'text-align': 'center','font-family': 'Courgette', 'font-size':'80px','padding-top':'10px'}),

    html.Div([
        html.H3(children='Carácteristicas'),

        html.Div([
            html.P(children='¿El cliente tiene línea múltiple?',
                   style={'float': 'left', 'width': '80%', 'max-width': '420px'}),
            dcc.RadioItems(
                options=[
                    {'label': 'Sí', 'value': '1'},
                    {'label': 'No', 'value': '0'},
                ],
                labelStyle={'display': 'inline-block', 'margin-bottom': '0.75rem'},
                style={'float': 'left', 'width': '20%'},
                id="q1"
            ),
        ], style={'clear': 'left'}),

        html.Div([
            html.P(children='¿El cliente ha contratado soporte técnico de la empresa?',
                   style={'float': 'left', 'width': '80%', 'max-width': '420px'}),
            dcc.RadioItems(
                options=[
                    {'label': 'Sí', 'value': '1'},
                    {'label': 'No', 'value': '0'},
                ],
                labelStyle={'display': 'inline-block', 'margin-bottom': '0.75rem'},
                style={'float': 'left', 'width': '20%'},
                id="q2"
            ),
        ], style={'clear': 'left'}),

        html.Div([
            html.P(children='¿El cliente ha solicitado servicio de internet?',
                   style={'float': 'left', 'width': '80%', 'max-width': '420px'}),
            dcc.RadioItems(
                options=[
                    {'label': 'Sí', 'value': '1'},
                    {'label': 'No', 'value': '0'},
                ],
                labelStyle={'display': 'inline-block', 'margin-bottom': '0.75rem'},
                style={'float': 'left', 'width': '20%'},
                id="q3"
            ),
        ], style={'clear': 'left'}),

        html.Div([
            html.P(children='¿El cliente ha solicitado servicio de TV por cable?',
                   style={'float': 'left', 'width': '80%', 'max-width': '420px'}),
            dcc.RadioItems(
                options=[
                    {'label': 'Sí', 'value': '1'},
                    {'label': 'No', 'value': '0'},
                ],
                labelStyle={'display': 'inline-block', 'margin-bottom': '0.75rem'},
                style={'float': 'left', 'width': '20%'},
                id="q4"
            ),
        ], style={'clear': 'left'}),

        html.Div([
            html.P(children='¿El cliente ha solicitado un plan de seguridad informática?',
                   style={'float': 'left', 'width': '80%', 'max-width': '420px'}),
            dcc.RadioItems(
                options=[
                    {'label': 'Sí', 'value': '1'},
                    {'label': 'No', 'value': '0'},
                ],
                labelStyle={'display': 'inline-block', 'margin-bottom': '0.75rem'},
                style={'float': 'left', 'width': '20%'},
                id="q5"
            ),
        ], style={'clear': 'left'}),

        html.Div([
            html.P(children='¿El cliente tiene un servicio de streaming de películas?',
                   style={'float': 'left', 'width': '80%', 'max-width': '420px'}),
            dcc.RadioItems(
                options=[
                    {'label': 'Sí', 'value': '1'},
                    {'label': 'No', 'value': '0'},
                ],
                labelStyle={'display': 'inline-block', 'margin-bottom': '0.75rem'},
                style={'float': 'left', 'width': '20%'},
                id="q6"
            ),
        ], style={'clear': 'left'}),

        html.Div([
            html.P(children='¿El cliente es jubilado?',
                   style={'float': 'left', 'width': '80%', 'max-width': '420px'}),
            dcc.RadioItems(
                options=[
                    {'label': 'Sí', 'value': '1'},
                    {'label': 'No', 'value': '0'},
                ],
                labelStyle={'display': 'inline-block', 'margin-bottom': '0.75rem'},
                style={'float': 'left', 'width': '20%'},
                id="q7"
            ),
        ], style={'clear': 'left'}),

        html.Div([
            html.P(children='¿Cuál es el medio de pago que más usa?',
                   style={'float': 'left', 'width': '80%', 'max-width': '420px'}),
            dcc.Dropdown(
                options=[
                {'label': 'Cheque electrónico', 'value': '1'},
                {'label': 'Cheque enviado', 'value': '2'},
                {'label': 'Transferencia', 'value': '3'},
                {'label': 'Tarjeta de credito', 'value': '4'},
                ],
                style={'float': 'left', 'width': '150px'},
                id="q8"
            ),
        ], style={'clear': 'left'}),

        html.Div([
            html.P(children='¿Cuál es el tipo de facturación que prefiere?',
                   style={'float': 'left', 'width': '80%', 'max-width': '420px'}),
            dcc.Dropdown(
                options=[
                    {'label': 'Físico', 'value': '0'},
                    {'label': 'Electrónico', 'value': '1'},
                ],
                style={'float': 'left', 'width': '150px'},
                id="q9"
            ),
        ], style={'clear': 'left'}),

        html.Div([
            html.P(children='¿Cuántos años tiene el cliente con la empresa?',
                   style={'float': 'left', 'width': '80%', 'max-width': '420px'}),
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
                style={'float': 'left', 'width': '150px'},
                id="q10"
            ),
        ], style={'clear': 'left'}),

        html.Div([
            html.P(children='¿Qué tipo de contrato tiene?',
                   style={'float': 'left', 'width': '80%', 'max-width': '420px'}),
            dcc.Dropdown(
                options=[
                    {'label': 'Mensual', 'value': '1'},
                    {'label': 'Anual', 'value': '2'},
                    {'label': 'Bienal', 'value': '3'},
                ],
                style={'float': 'left','width': '150px'},
                id="q11"
            ),

        ], style={}),

    ], style={'float': 'left', 'width': '45%','padding-left':'5vw'}),

    html.Div([
        html.Div([
            html.H1(""),
            html.H1(""),
            html.Button('Consultar Cliente', id='button',
                        style={'clear': 'both', 'width': '100%', 'font-size': '15px'}),
            html.H1(""),
            html.H4(children="La puntuación del cliente es de:",style={'text-align': 'center','margin':'0px'}),

            html.Div(id='output-container-button', children='------', style={'font-size': '80px', 'text-align': 'center'}),
            html.Img(id='image',style={'width':'200px','display': 'block','margin-left':'auto','margin-right':'auto'})
        ], style={'width': '80%'}),

    ], style={'width': '49%','float': 'right'})
], style={'background-image':'url(http://www.lksur.com.uy/imagenes/t1.jpg)'})


@app.callback([
    dash.dependencies.Output('output-container-button', 'children'),
    dash.dependencies.Output('image', 'src')],
    [dash.dependencies.Input('button', 'n_clicks')],
    [dash.dependencies.State('q1', 'value'),
     dash.dependencies.State('q2', 'value'),
     dash.dependencies.State('q3', 'value'),
     dash.dependencies.State('q4', 'value'),
     dash.dependencies.State('q5', 'value'),
     dash.dependencies.State('q6', 'value'),
     dash.dependencies.State('q7', 'value'),
     dash.dependencies.State('q8', 'value'),
     dash.dependencies.State('q9', 'value'),
     dash.dependencies.State('q10', 'value'),
     dash.dependencies.State('q11', 'value')])
def update_output(n_clicks, value1, value2, value3, value4, value5, value6, value7, value8, value9, value10, value11):
    sumaProducto=-0.457+float(value1)*0.1735+float(value2)*-0.3614+float(value3)*0.8379+float(value4)*0.2526+float(value5)*-0.407+float(value6)*0.2809+float(value7)*0.2522+float(value8)*-0.1561+float(value9)*0.3443+float(value10)*-0.3728+float(value11)*-0.7783
    probabilidad= math.exp(sumaProducto)/(1+math.exp(sumaProducto))
    if probabilidad>0.2:
        return str(round(probabilidad * 100,2)), 'https://www.somosmamas.com.ar/wp-content/uploads/2017/11/emoji-carita-triste.png'
    elif probabilidad>0.1:
        return str(round(probabilidad * 100,2)), 'https://cdn.shopify.com/s/files/1/1061/1924/files/Face_With_Rolling_Eyes_Emoji.png?6135488989279264585'
    else:
        return str(round(probabilidad * 100, 2)), 'http://www.stickpng.com/assets/images/580b57fcd9996e24bc43c4bd.png'

if __name__ == '__main__':
    app.run_server(debug=True)
