import dash_bootstrap_components as dbc
from PIL import Image
from dash import dcc, html



export = html.Div([
    html.Div(dcc.Dropdown(id="dropdown-2",
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

    dbc.Row(html.H2('Export Dataset', className='export_title', style={'background-color': '#fdfff5'}),
            style={'background-color': '#fdfff5'}),
    dbc.Row(dcc.Graph(id='graph-table', className="export_table", style={'background-color': '#fdfff5'})),
    dbc.Row(html.Div(html.H3(
        'You can export this page by clicking the Export button. This information has been taken from NYC Open Data website. This datas based on Newyork Police Departments report. But this is not an official file..',
        className='export_explain_text'),
            ), className="export_explain_text_div", style={'background-color': '#fdfff5'}),
    dbc.Row([dbc.Col(html.Div(html.Div(html.Button("Export CSV", id='export-button-csv', className="export_button",
                    style={'background-color': '#fdfff5'}),
                    className="export_button_div", style={'background-color': '#fdfff5'})), width=6, style={'background-color': '#fdfff5'}),
             dbc.Col(html.Div(html.Div(html.Button("Export EXCEL", id='export-button-excel', className="export_button",
                    style={'background-color': '#fdfff5'}),
                    className="export_button_div", style={'background-color': '#fdfff5'})), width=6, style={'background-color': '#fdfff5'})]),
    dcc.Download(id="download-component"),
    dcc.Download(id="download-component-2")

], className="export_body", style={'background-color': '#fdfff5'})


def get_export_page(): return export
