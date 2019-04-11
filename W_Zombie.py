# -*- coding: utf-8 -*-
import dash
import dash_auth
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import math

VALID_USERNAME_PASSWORD_PAIRS = [
    ['WorkshopIngInfo', 'PaCiFiCo2019']
]

external_stylesheets = ['']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

app.layout = html.Div(children=[

    html.Link(href='https://fonts.googleapis.com/css?family=Fredericka+the+Great', rel='stylesheet'),

    html.H1(children="The Next Survivor",
            style={'text-align': 'center', 'font-family': 'Courgette', 'font-size': '80px',
                   'margin': '10px 0px 30px 0px', 'font-weight': 'normal'}),

    html.Div([
        html.H3(children='Características',
                style={'font-size': '40px', 'margin': '0px 0px 30px 0px', 'font-family': 'Open Sans',
                       'font-weight': 'normal'}),

        html.Div([
            html.P(children='¿Qué edad tiene?',
                   style={'float': 'left', 'width': '65%', 'max-width': '420px', 'margin': '0px'}),
            dcc.Dropdown(
                options=[
                    {'label': '[-26] años', 'value': '1'},
                    {'label': '[27-37] años', 'value': '2'},
                    {'label': '[38-48] años', 'value': '3'},
                    {'label': '[+48] años', 'value': '4'},
                ],
                style={'float': 'left', 'width': '15vw', 'max-width': '150px'},
                id="q1"
            ),

        ], style={}),

        html.Div([
            html.P(children='¿Sexo asignado al nacer?',
                   style={'float': 'left', 'width': '80%', 'max-width': '420px', 'margin': '0px'}),
            dcc.RadioItems(
                options=[
                    {'label': 'Hombre', 'value': '0'},
                    {'label': 'Mujer', 'value': '1'},
                ],
                labelStyle={'display': 'inline-block', 'margin-bottom': '0.75rem'},
                style={'float': 'left', 'width': '20%', 'min-width': '80px'},
                id="q2"
            ),
        ], style={'clear': 'left'}),

        html.Div([
            html.P(children='¿Tiene hijos menores de edad?',
                   style={'float': 'left', 'width': '80%', 'max-width': '420px', 'margin': '0px'}),
            dcc.RadioItems(
                options=[
                    {'label': 'Sí', 'value': '1'},
                    {'label': 'No', 'value': '0'},
                ],
                labelStyle={'display': 'inline-block', 'margin-bottom': '0.75rem'},
                style={'float': 'left', 'width': '20%', 'min-width': '80px'},
                id="q3"
            ),
        ], style={'clear': 'left'}),

        html.Div([
            html.P(children='¿Conoce sobre agricultura básica?',
                   style={'float': 'left', 'width': '80%', 'max-width': '420px', 'margin': '0px'}),
            dcc.RadioItems(
                options=[
                    {'label': 'Sí', 'value': '1'},
                    {'label': 'No', 'value': '0'},
                ],
                labelStyle={'display': 'inline-block', 'margin-bottom': '0.75rem'},
                style={'float': 'left', 'width': '20%', 'min-width': '80px'},
                id="q4"
            ),
        ], style={'clear': 'left'}),

        html.Div([
            html.P(children='¿Posee un buen sentido de ubicación?',
                   style={'float': 'left', 'width': '80%', 'max-width': '420px', 'margin': '0px'}),
            dcc.RadioItems(
                options=[
                    {'label': 'Sí', 'value': '1'},
                    {'label': 'No', 'value': '0'},
                ],
                labelStyle={'display': 'inline-block', 'margin-bottom': '0.75rem'},
                style={'float': 'left', 'width': '20%', 'min-width': '80px'},
                id="q5"
            ),
        ], style={'clear': 'left'}),

        html.Div([
            html.P(children='¿Tiene acceso a diversa comida?',
                   style={'float': 'left', 'width': '80%', 'max-width': '420px', 'margin': '0px'}),
            dcc.RadioItems(
                options=[
                    {'label': 'Sí', 'value': '1'},
                    {'label': 'No', 'value': '0'},
                ],
                labelStyle={'display': 'inline-block', 'margin-bottom': '0.75rem'},
                style={'float': 'left', 'width': '20%', 'min-width': '80px'},
                id="q6"
            ),
        ], style={'clear': 'left'}),

        html.Div([
            html.P(children='¿Domina mecánica básica?',
                   style={'float': 'left', 'width': '80%', 'max-width': '420px', 'margin': '0px'}),
            dcc.RadioItems(
                options=[
                    {'label': 'Sí', 'value': '1'},
                    {'label': 'No', 'value': '0'},
                ],
                labelStyle={'display': 'inline-block', 'margin-bottom': '0.75rem'},
                style={'float': 'left', 'width': '20%', 'min-width': '80px'},
                id="q7"
            ),
        ], style={'clear': 'left'}),

        html.Div([
            html.P(children='¿Puede usar algún tipo de arma de fuego?',
                   style={'float': 'left', 'width': '80%', 'max-width': '420px', 'margin': '0px'}),
            dcc.RadioItems(
                options=[
                    {'label': 'Sí', 'value': '1'},
                    {'label': 'No', 'value': '0'},
                ],
                labelStyle={'display': 'inline-block', 'margin-bottom': '0.75rem'},
                style={'float': 'left', 'width': '20%', 'min-width': '80px'},
                id="q8"
            ),
        ], style={'clear': 'left'}),

        html.Div([
            html.P(children='¿Sabe aplicar primeros auxilios?',
                   style={'float': 'left', 'width': '80%', 'max-width': '420px', 'margin': '0px'}),
            dcc.RadioItems(
                options=[
                    {'label': 'Sí', 'value': '1'},
                    {'label': 'No', 'value': '0'},
                ],
                labelStyle={'display': 'inline-block', 'margin-bottom': '0.75rem'},
                style={'float': 'left', 'width': '20%', 'min-width': '80px'},
                id="q9"
            ),
        ], style={'clear': 'left'}),

        html.Div([
            html.P(children='¿Posee habilidaddes de defensa personal?',
                   style={'float': 'left', 'width': '80%', 'max-width': '420px', 'margin': '0px'}),
            dcc.RadioItems(
                options=[
                    {'label': 'Sí', 'value': '1'},
                    {'label': 'No', 'value': '0'},
                ],
                labelStyle={'display': 'inline-block', 'margin-bottom': '0.75rem'},
                style={'float': 'left', 'width': '20%', 'min-width': '80px'},
                id="q10"
            ),
        ], style={'clear': 'left'}),

        html.Div([
            html.P(children='¿Vive con mucha gente a su alrededor?',
                   style={'float': 'left', 'width': '80%', 'max-width': '420px', 'margin': '0px'}),
            dcc.RadioItems(
                options=[
                    {'label': 'Sí', 'value': '1'},
                    {'label': 'No', 'value': '0'},
                ],
                labelStyle={'display': 'inline-block', 'margin-bottom': '0.75rem'},
                style={'float': 'left', 'width': '20%', 'min-width': '80px'},
                id="q11"
            ),
        ], style={'clear': 'left'}),

    ], style={'float': 'left', 'width': '45%', 'padding-left': '5vw'}),

    html.Div([
        html.Div([
            html.Button('Consultar sobreviviente', id='button',
                        style={'clear': 'both', 'width': '100%', 'font-size': '20px', 'height': '40px',
                               'margin-top': '10px', 'border-radius': '20px', 'font-family': 'Open Sans',
                               'margin': '20px 0px 0px 0px'}),
            html.H1(""),
            html.H4(children="La puntuación del sobreviviente es de:",
                    style={'text-align': 'center', 'margin': '0px', 'font-family': 'Open Sans', 'font-size': '30px',
                           'font-weight': 'normal'}),

            html.Div(id='output-container-button', children='------',
                     style={'font-size': '80px', 'text-align': 'center'}),
            html.Img(id='image',
                     style={'width': '50%', 'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'})
        ], style={'width': '85%'}),

    ], style={'width': '49%', 'float': 'right'})
], style={'background-image': 'url(https://png.pngtree.com/thumb_back/fw800/back_pic/03/59/79/0557a49d0f32599.jpg)'})


@app.callback(
    dash.dependencies.Output('image', 'src'),
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
    Madi = [3, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0]
    Gabi = [1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1]
    Jose = [2, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1]
    Irpiri = [4, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0]
    trampa = 0
    personajes = [Madi, Gabi, Jose, Irpiri]
    for sobreviviente in personajes:
        if [int(value1), int(value2), int(value3), int(value4), int(value5), int(value6), int(value7), int(value8), int(value9), int(value10), int(value11)] == sobreviviente:
            trampa = 1
        if value1==1:
            trampa=1
    if (trampa == 1):
        return "https://t4.ftcdn.net/jpg/01/70/28/23/240_F_170282328_31qaGRFFKAuAWgWpJsqFtO8UpstN2Bhw.jpg"
    if n_clicks != None:
        sumaProducto = -3.186 + float(value1) * 0.1993 + float(value2) * 0.1574 + float(value3) * -1.0707 + float(
            value4) * 0.2342 + float(value5) * 0.6037 + float(value6) * 0.2444 + float(value7) * 0.6707 + float(
            value8) * 0.4907 + float(value9) * 0.239 + float(value10) * 1.428 + float(value11) * -0.4088
        probabilidad = math.exp(sumaProducto) / (1 + math.exp(sumaProducto))
        if probabilidad > 0.2:
            return 'https://www.somosmamas.com.ar/wp-content/uploads/2017/11/emoji-cool.png'
        elif probabilidad > 0.1:
            return 'https://cdn.shopify.com/s/files/1/1061/1924/files/Face_With_Rolling_Eyes_Emoji.png?6135488989279264585'
        else:
            return 'https://cdn4.iconfinder.com/data/icons/aami-flat-smileys/64/smile-61-512.png'
    else:
        pass


@app.callback(
    dash.dependencies.Output('output-container-button', 'children'),
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
    Madi=   [3,1,0,0,0,0,0,1,1,1,0]
    Gabi=   [1,1,0,0,1,0,0,1,0,1,1]
    Jose=   [2,0,0,0,0,1,1,0,1,0,1]
    Irpiri= [4,0,1,1,1,0,1,0,0,0,0]
    trampa=0
    personajes=[Madi,Gabi,Jose,Irpiri]
    for sobreviviente in personajes:
        if [int(value1), int(value2), int(value3), int(value4), int(value5), int(value6), int(value7), int(value8), int(value9), int(value10), int(value11)] == sobreviviente:
            trampa = 1
    if (trampa==1):
        return "No válido"
    elif n_clicks != None:
        sumaProducto = -3.186 + float(value1) * 0.1993 + float(value2) * 0.1574 + float(value3) * -1.0707 + float(
            value4) * 0.2342 + float(value5) * 0.6037 + float(value6) * 0.2444 + float(value7) * 0.6707 + float(
            value8) * 0.4907 + float(value9) * 0.239 + float(value10) * 1.428 + float(value11) * -0.4088
        probabilidad = math.exp(sumaProducto) / (1 + math.exp(sumaProducto))
        return str(round(probabilidad * 100, 2))
    else:
        pass


if __name__ == '__main__':
    app.run_server(debug=True)
