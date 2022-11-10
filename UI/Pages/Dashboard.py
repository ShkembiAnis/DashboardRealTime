import dash_bootstrap_components as dbc
from PIL import Image
from dash import dcc, html
import streamlit as st
from PLOTLY.FigureCreator import pieChartCreater, pie2ChartCreater, lineChartCreater, get_total_rows, fig_searched

''''''
logo = Image.open("assets/logo.png")

pie = pieChartCreater()
pie2 = pie2ChartCreater()
fig_line = lineChartCreater()
fig_line2 = lineChartCreater()
figure = fig_searched("4407147")


@st.experimental_memo
def update_total_rows():
    updated_total_rows = get_total_rows()
    return updated_total_rows


total_rows = update_total_rows()

dash_page = html.Div([
    html.Div(dcc.Dropdown(id="dropdown",
                          options=[
                              {'label': '2012', 'value': '2012'},
                              {'label': '2013', 'value': '2013'},
                              {'label': '2014', 'value': '2014'},
                              {'label': '2015', 'value': '2015'},
                              {'label': '2016', 'value': '2016'},
                              {'label': '2017', 'value': '2017'},
                              {'label': '2018', 'value': '2018'},
                              {'label': '2019', 'value': '2019'},
                              {'label': '2020', 'value': '2020'},
                              {'label': '2021', 'value': '2021'},
                              {'label': '2022', 'value': '2022'},
                          ], value='2022', placeholder="Select Year to Filter Dataset",
                          className="dropdown-dash", style={"background-color": "#fdfff5"}
                          ),
             className="dropdown-div"),

    html.Div([
        dbc.Row([dbc.Col(dcc.Graph(id="linechart", figure=fig_line,
                                   style={'height': '350px', 'background-color': '#fdfff5'}),
                         style={'border': 'solid', 'border-color': '#62DFC7', 'background-color': '#fdfff5',
                                'padding': '5px'}, width=6),
                 dbc.Col(dcc.Graph(id="linechart2", figure=pie,
                                   style={'height': '350px', 'background-color': '#fdfff5'}),
                         style={'border': 'solid', 'border-color': '#62DFC7', 'background-color': '#fdfff5',
                                'padding': '10px'}, width=3),
                 dbc.Col(dcc.Graph(id="linechart3", figure=pie2,
                                   style={'height': '350px', 'background-color': '#fdfff5'}),
                         style={'border': 'solid', 'border-color': '#62DFC7', 'background-color': '#fdfff5'}, width=3)
                 ],
                style={'background-color': '#fdfff5', 'height': '400px', 'margin-left': '190px',
                       'margin-right': '190px', 'margin-bottom': '50px'
                       }),

        dbc.Row(dcc.Graph(id="graph-2"),
                style={'background-color': '#fdfff5', 'border': 'solid', 'border-color': '#62DFC7', 'height': '420px',
                       'margin-left': '200px',
                       'margin-right': '200px', 'margin-bottom': '50px'}),

        dbc.Row([
            dcc.Graph(id="graph", className="map"),
            dcc.Checklist(options=[
                    {'label': 'All Collisions ', 'value': 'All Collisions'},
                    {'label': 'Fatal', 'value ': 'Fatal'},
                    {'label': 'Not Fatal', 'value': 'Not Fatal'}
                ],
                    value=['All Collisions'],
                    inline=True,
                    style={'margin-right': '500px', 'margin-left': '200px', 'margin-bottom': '50px'}
                )
        ],
            style={'border': 'solid', 'border-color': '#62DFC7', 'background-color': '#fdfff5', 'height': '730px',
                   'margin-left': '200px',
                   'margin-right': '200px',
                   'margin-bottom': '50px',
                   'text=align': 'centre'}
        ),

        dbc.Row([
            dbc.Col(html.Div(id='textarea-state-example-output',
                             style={'height': '350px',
                                    'whiteSpace': 'pre-line', 'text-align': 'center', 'color': '#62DFC7',
                                    'font-size': '30px', 'margin-top': '100px'}),
                    style={'background-color': '#fdfff5'}, width=8),

            dbc.Col(html.Button(id='textarea-state-example-button',
                                children=[html.Img(src=logo,
                                                   style={'height': '350px', 'width': '350px', 'margin-left': '100px'},
                                                   className="fit-picture")],
                                style={'height': '350px', 'background-color': '#fdfff5', 'border': 'none'}, n_clicks=0),
                    style={'background-color': '#fdfff5'}, width=4), ],

            style={'background-color': '#fdfff5', 'height': '400px', 'margin-left': '190px',
                   'margin-right': '190px',
                   'margin-bottom': '50px'}),

        dbc.Row(html.H2('Collisions Info by ID', className='export_title'), ),
        dbc.Row(
            html.Div(dbc.Input(id="input", placeholder="Type the collisions ID, that you looking for....", type="text",
                               className="export_input_field", value='4407147', style={'background-color': '#fdfff5'}),
                     ), className="export_input_field_div", style={'background-color': '#fdfff5'}),
        dbc.Row(dcc.Graph(id='searched-value', figure=figure, className="searched_value", style={'background-color': '#fdfff5'})),
        dbc.Row(html.H1("drive safe.", className="drive_safe")),

    ])
],
style={'background-color': '#fdfff5'}
)


def get_dashpage(): return dash_page
