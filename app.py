#Dependencies
import dash
import dash_table
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import dash_dangerously_set_inner_html

import pandas as pd
import pandas_profiling as pd_profiling
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split

# Read data
data = pd.read_csv('data/WA_Fn-UseC_-Telco-Customer-Churn.csv')

# Translate variable names to spanish
data.columns = ['ID_Cliente', 'Genero', 'Jubilado', 'Pareja', 'Hijos', 'Mes_Plan',
                'Servicio_Celular', 'Línea_Multiple', 'Internet', 'Seguridad_Linea',
                'Respaldo_Linea', 'Proteccion_Disp', 'Soporte_Tecnico', 'TV',
                'Peliculas', 'Tipo_Contrato', 'Factura_Elect', 'Metodo_Pago',
                'Monto_Mens', 'Monto_Total', 'Migracion']

# Encode categorical variables
enc = OrdinalEncoder()
cat_vars = data[['Genero','Jubilado','Pareja','Hijos','Servicio_Celular','Línea_Multiple',
                  'Internet','Seguridad_Linea','Respaldo_Linea','Proteccion_Disp',
                  'Soporte_Tecnico','TV','Peliculas','Tipo_Contrato','Factura_Elect',
                  'Metodo_Pago','Migracion']].values
data[['Genero','Jubilado','Pareja','Hijos','Servicio_Celular','Línea_Multiple',
                  'Internet','Seguridad_Linea','Respaldo_Linea','Proteccion_Disp',
                  'Soporte_Tecnico','TV','Peliculas','Tipo_Contrato','Factura_Elect',
                  'Metodo_Pago','Migracion']] = enc.fit_transform(cat_vars)

# Fix Monto_Total variable type
data.Monto_Total = data.Monto_Total.replace(' ', '0')
data.Monto_Total = data.Monto_Total.astype('float')

# Create data profiles
data_profile = pd_profiling.ProfileReport(data).to_html()
data_profile_0 = pd_profiling.ProfileReport(data[data.Migracion == 0]).to_html()
data_profile_1 = pd_profiling.ProfileReport(data[data.Migracion == 1]).to_html()
variables = data.columns.values.tolist()

# Create dict for checklist options
variables_dict = [{'label':var_name, 'value':var_name} for var_name in variables]
variables_dict.pop(0) # Delete ID_Cliente from options
variables_dict.pop(-1) # Delete Migracion from options

# Dash app config
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.config['suppress_callback_exceptions']=True

# Dash app layout
app.layout = html.Div([
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Tab one', value='tab-1'),
        dcc.Tab(label='Tab two', value='tab-2'),
        dcc.Tab(label='Tab three', value='tab-3'),
    ]),
    html.Div(id='tabs-content')
])

# Dash app interactive funcionatilities
@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
    dash_dangerously_set_inner_html.DangerouslySetInnerHTML(data_profile_1),
])
    elif tab == 'tab-2':
        return html.Div([
    dash_dangerously_set_inner_html.DangerouslySetInnerHTML(data_profile_0),
])
    elif tab == 'tab-3':
        return dcc.Checklist(
    options=variables_dict,
    values=['Genero'],
    id='checklist'
), dcc.ConfirmDialogProvider(
children=html.Button(
    'Genera el modelo',
),
id='generate-model',
message='Si continuas generaras un modelo'
), html.Div(id='output_provider')

@app.callback(Output('output_provider', 'children'),
              [Input('generate-model', 'submit_n_clicks'),
               Input('checklist','values')])
def update_output(submit_n_clicks,values):
    if not submit_n_clicks:
        return ''

    X = data[values].values # variables
    y = data['Migracion'].values # target
    X_train, X_test, y_train, y_test = train_test_split(X, y) # generate train and test sets
    clf = LogisticRegression(random_state=0, solver='lbfgs').fit(X_train, y_train) # define and fit model
    score = clf.score(X_test, y_test) # calculate test score
    return """
        El score de tu modelo es {}
    """.format(round(score,4))

# Run Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
