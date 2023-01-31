import dash_bootstrap_components as dbc
from PIL import Image
from dash import dcc, html
from INNOLAB.PLOTLY.FigureCreator import pieChartCreater, pie2ChartCreater, lineChartCreater, get_total_rows, \
    fig_searched

logo = Image.open("assets/logo.png")
pie = pieChartCreater()
pie2 = pie2ChartCreater()
fig_line = lineChartCreater()
fig_line2 = lineChartCreater()
figure = fig_searched("4407147")

dash_page = html.Div([

    html.Div([
        dbc.Row(
            [
                dbc.Col(html.Div([html.P("Total Cases",
                                         style={'text-align': 'center', 'color': 'white',
                                                'font-size': '18px'}),
                                  html.P("7,110,120", style={'text-align': 'center', 'color': '#ffa703',
                                                             'font-size': '28px'}),
                                  html.P("new 10,201(0.81%)", style={'text-align': 'center', 'color': '#ffa703',
                                                                     'font-size': '13px',
                                                                     'padding-bottom': '10px'}), ],
                                 style={'border': 'solid, #1f2d58, 1px', 'border-radius': '10px',
                                        'background-color': '#1f2d58'}), width=6, lg=3),
                dbc.Col(html.Div([html.P("Total Deaths",
                                         style={'text-align': 'center', 'color': 'white',
                                                'font-size': '18px'}),
                                  html.P("7,110,120", style={'text-align': 'center', 'color': '#a8294b',
                                                             'font-size': '28px'}),
                                  html.P("new 10,201(0.81%", style={'text-align': 'center', 'color': '#a8294b',
                                                                    'font-size': '13px',
                                                                    'padding-bottom': '10px'}), ],
                                 style={'border': 'solid, #1f2d58, 1px', 'border-radius': '10px',
                                        'background-color': '#1f2d58'}), width=6, lg=3),
                dbc.Col(html.Div([html.P("Total Injured",
                                         style={'text-align': 'center', 'color': 'white',
                                                'font-size': '18px'}),
                                  html.P("7,110,120", style={'text-align': 'center', 'color': '#0a7715',
                                                             'font-size': '28px'}),
                                  html.P("new 10,201(0.81%", style={'text-align': 'center', 'color': '#0a7715',
                                                                    'font-size': '13px',
                                                                    'padding-bottom': '10px'}), ],
                                 style={'border': 'solid, #1f2d58, 1px', 'border-radius': '10px',
                                        'background-color': '#1f2d58'}), width=6, lg=3),
                dbc.Col(html.Div([html.P("Total Injured",
                                         style={'text-align': 'center', 'color': 'white',
                                                'font-size': '18px'}),
                                  html.P("7,110,120", style={'text-align': 'center', 'color': '#d74f67',
                                                             'font-size': '28px'}),
                                  html.P("new 10,201(0.81%", style={'text-align': 'center', 'color': '#d74f67',
                                                                    'font-size': '13px',
                                                                    'padding-bottom': '10px'}), ],
                                 style={'border': 'solid, #1f2d58, 1px', 'border-radius': '10px',
                                        'background-color': '#1f2d58'}), width=6, lg=3),
            ], style={'margin-left': '190px',
                      'margin-right': '190px', 'margin-top': '120px', 'margin-bottom': '20px'}
        ),
        dbc.Row(
            [
                dbc.Col(html.Div([
                    html.P('Select Year', className='export_title', style={'margin-top': '30px'}),
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
                                          className="dropdown-dash",
                                          ), className="dropdown-div"),

                    html.P('Select Status', className='export_title'),
                    html.Div(dcc.Dropdown(id="dropdown2",
                                          options=[
                                              {'label': 'All', 'value': '0'},
                                              {'label': 'Killed', 'value': '1'},
                                              {'label': 'Injured', 'value': '2'},
                                          ], value='0', placeholder="Select Status to Filter Dataset",
                                          className="dropdown-dash",
                                          ), className="dropdown-div"),

                    html.P('Select Gender', className='export_title'),
                    html.Div(dcc.Dropdown(id="dropdown3",
                                          options=[
                                              {'label': 'All', 'value': '0'},
                                              {'label': 'Male', 'value': '1'},
                                              {'label': 'Female', 'value': '2'},
                                          ], value='0', placeholder="Select Gender to Filter Dataset",
                                          className="dropdown-dash",
                                          ), className="dropdown-div"),
                ]), style={'border': 'solid, #1f2d58, 1px', 'border-radius': '10px', 'height': '350px',
                           'background-color': '#1f2d58'}, className="dropdown-div_main", width=6, lg=3),




                dbc.Col(html.Div(dcc.Graph(id="linechart3", figure=pie2,
                                           style={'height': '350px', 'background-color': '#1f2d58', }),
                                 style={'background-color': '#191a1a'}), className="dropdown-div_main_2", width=6, lg=3),

                dbc.Col(html.Div(dcc.Graph(id="graph-2", style={'padding': '5px'}),

                                 ), style={'height': '350px', 'background-color': '#1f2d58',
                                        'border': 'solid, #1f2d58, 1px', 'border-radius': '10px'}, className="dropdown-div_main_3", width=6, lg=6),

            ],
            style={'height': '350px', 'margin-left': '200px',
                   'margin-right': '200px',
                   }),
        dbc.Row(
            dcc.Graph(id="graph", className="map"),
            style={'background-color': '#1f2d58', 'border': 'solid, 1px, #1f2d58', 'border-radius': '10px', 'height': '490px', 'margin-left': '200px',
                   'margin-right': '200px',
                   'margin-bottom': '50px', 'margin-top': '30px'}),

        dbc.Row(html.H1("drive safe.", className="drive_safe")),

    ], className="dash_page_test")
])


def get_dash_page(): return dash_page
