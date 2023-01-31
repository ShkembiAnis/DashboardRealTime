from dash import Dash, dcc, html, Input, Output, callback

import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input, State

from DAL.DataGetter import read_data_from_database
from PLOTLY.FigureCreator import mapCreaterByYear, figureCreaterByYear, fig_searched, randomInfoCreater, get_total_rows, mapCreaterBySearchedValue, grouper
from INNOLAB.UI.Pages.Dash import get_dash_page
from UI.Pages.About import get_about_page

import dash
import numpy as np
from random import randint
from flask.helpers import get_root_path
from PIL import Image
import time
from UI.Pages.Export import get_export_page
from INNOLAB.UI.Pages.Dashboard import get_dash_page
from PLOTLY.FigureCreator import tableCreaterByYear

info_0 = get_total_rows()
logo = Image.open("assets/logo.png")
leemon_logo = Image.open("assets/leemon_logo.png")
nyc_openDash_logo = Image.open("assets/nyc_logo.png")


Start = time.time()
df = read_data_from_database(Start)
df_excel = grouper("2022")


navbar = html.Div(dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("DASHBOARD", active=True, href="/page-0", className="nav_1")),
        dbc.NavItem(dbc.NavLink("ABOUT", active=True, href="/page-1", className="nav_2")),
        dbc.NavItem(dbc.NavLink("EXPORT", active=True, href="/page-2", className="nav_3")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("ENG"),
                dbc.DropdownMenuItem("DE"),
            ],
            nav=True,
            label="LANG",
            className="bar_dropdown",
            toggle_style={
                "textTransform": "uppercase",
                "margin-top": "10px",
                "color": "#808080",
                "margin-right": "150px",
                "font-size": "20px",
            },
        ),

    ],
    brand="NYC",
    brand_style={'margin-top': '10px', 'color': '#808080', 'margin-right': '250px', 'font-size': '40px'},
    brand_href="/page-0",

), className="navbar"
)

fh_logo = Image.open("assets/fh_logo.png")
page_1_layout = get_dash_page()
page_2_layout = get_about_page()
page_3_layout = get_export_page()



footer = html.Div([
    html.Div(dbc.Row([
        dbc.Col(html.Div(html.Img(src=nyc_openDash_logo, className="logo_1"))),
        dbc.Col(html.Div(html.Img(src=fh_logo), className="logo_2")),
        dbc.Col(html.Div(html.Img(src=leemon_logo, className="logo_3")), )])),
    html.Div("@Copyright | FH Technikum Wien ", className="copyright"),
], className="footer")


def start_app():
    app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], assets_folder='../assets')
    print(get_root_path(__name__))
    app.layout = html.Div([
        dcc.Location(id='url', refresh=False),
        navbar,
        html.Div(id='page-content'),
        footer
    ], style={'background-color': '#1a2245'})

    # -------------------------------------------------Update Map-------------------------------------------------------
    @app.callback(
        Output("graph", "figure"),
        Input("dropdown", "value"))
    def update_figure(value):
        fig = mapCreaterByYear(str(value))
        return fig

    # ------------------------------------------Update Map on Export Page-----------------------------------------------
    @app.callback(
        Output("graph-searched", "figure"),
        Input("input", "value"))
    def update_figure(value):
        fig = mapCreaterBySearchedValue(str(value))
        return fig

    # ------------------------------------------------Update Table------------------------------------------------------
    @app.callback(
            Output("graph-table", "figure"),
        Input("dropdown", "value"))
    def update_figure(value):
        fig = tableCreaterByYear(str(value))
        return fig

    # ------------------------------------------------Update Bar Box----------------------------------------------------
    @app.callback(
        Output("graph-2", "figure"),
        Input("dropdown", "value"))
    def update_figure(value):
        fig = figureCreaterByYear(str(value))
        return fig

    # -------------------------------------------Update Searched item Table---------------------------------------------
    @app.callback(
        Output("searched-value", "figure"),
        Input("input", "value"))
    def update_figure(value):
        fig = fig_searched(str(value))
        return fig

    # ----------------------------------------------Update Info Box-----------------------------------------------------
    @app.callback(
        Output('container-button-basic', 'children'),
        Input('submit-val', 'n_clicks'),
        State('input-on-submit', 'value')
    )
    def update_output(n_clicks, value):
        info = randomInfoCreater()
        return info

    @app.callback(
        Output('textarea-state-example-output', 'children'),
        Input('textarea-state-example-button', 'n_clicks'),
    )
    def update_output(n_clicks):
        value = randomInfoCreater()
        if n_clicks == 0:
            return info_0
        if n_clicks > 0:
            return '{}'.format(value)

    # ------------------------------------------------Export CSV Button------------------------------------------------------

    @callback(Output("download-component", "data"),
              Input('export-button-csv', 'n_clicks'))
    def export_data(n_clicks):
        if n_clicks > 0:
            return dcc.send_data_frame(df.to_csv, "nyc_collisions.csv")

    # ------------------------------------------------Export Excel Button------------------------------------------------------

    @callback(Output("download-component-2", "data"),
              Input('export-button-excel', 'n_clicks'))
    def export_data_excel(n_clicks):
        if n_clicks > 0:
            print("YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY-----------------------------------")
            return dcc.send_data_frame(df_excel.to_excel, "nyc_collisions.xlsx", sheet_name="Sheet_name_1")

    # -------------------------------------------------Update Page form Navbar---31--------------------------------------
    @callback(Output('page-2-content', 'children'),
              Input('page-2-radios', 'value'))
    def page_2_radios(value):
        return f'You have selected {value}'

    # Update the index
    @callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
    def display_page(pathname):
        if pathname == '/page-0':
            return page_1_layout
        elif pathname == '/page-1':
            return page_2_layout
        elif pathname == '/page-2':
            return page_3_layout
        else:
            return page_1_layout

    app.run_server(debug=False)
