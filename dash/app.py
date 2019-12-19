import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from properties_utils import test
from utils.figures import sunburst_plot


# App initialization
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

style_selectors = {'padding': '15px'}

# App layout
app.layout = html.Div(
    [
        dbc.Navbar(
            [
                html.Img(src='static/logo.jpg'),
                dbc.Row(
                    [
                        dbc.Col(dbc.NavbarBrand("Dashboard", className="ml-2")),
                    ],
                    align="center",
                    no_gutters=True,
                ),
            ],
            color="white",
            dark=True,
        ),
        dbc.Row(
            [
                html.Div(html.H2('Price of energy in Colombia'))
            ],
            style={
                'padding-left': '45px',
                'font-family': "Comic Sans MS"
            }
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        dbc.Row(
                                            [
                                                dbc.Col(
                                                    [
                                                        html.H6('Explain by:')
                                                    ],
                                                    width=4
                                                ),
                                                dbc.Col(
                                                    [
                                                        dcc.Dropdown(
                                                            id='id-explain',
                                                            options=[
                                                                {'label': 'Region', 'value': 'region'},
                                                                {'label': 'Dataset', 'value': 'dataset'},
                                                            ],
                                                            value='region'
                                                        ),
                                                    ],
                                                    width=6),
                                            ],
                                            style=style_selectors),
                                    ]
                                ),
                            ]
                        ),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        dcc.Graph(
                                            id='id-sunburst-plot',
                                            # figure=update_sunburst_plot()

                                        )
                                    ],
                                    width=12
                                )
                            ]
                        )
                    ],
                    width=6
                ),
                dbc.Col(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        dbc.Row(
                                            [],
                                            style=style_selectors),
                                    ]
                                ),
                            ]
                        ),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        dcc.Graph(
                                            id='id-bar-plot',
                                            # figure=update_bar_plot(),
                                            style={'height': 300},
                                        ),
                                        dcc.Graph(
                                            id='id-scatter-plot',
                                            # figure=update_scatter_plot(),
                                            style={'height': 300},
                                        )
                                    ],
                                    width=12
                                )
                            ]
                        ),
                    ],
                    width=6
                ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(
                            [
                                dbc.Button("Help!", id="open"),
                                dbc.Modal(
                                    [
                                        dbc.ModalHeader("Help"),
                                        dbc.ModalBody("Welcome to the dashboard for energy analysis"),
                                        dbc.ModalFooter(
                                            dbc.Button("Close", id="close", className="ml-auto")
                                        ),
                                    ],
                                    id="modal",
                                ),
                            ]
                        )
                    ]
                )
            ]
        ),
    ]
)


@app.callback(
    Output('id-sunburst-plot', 'figure'),
    [Input('id-explain', 'value')]
)
def update_sunburst_plot(labels):
    df_data = test()

    if labels == 'region':
        figure = sunburst_plot(data=df_data, labels='region', parents='dataset', values='gain')
    else:
        figure = sunburst_plot(data=df_data, labels='dataset', parents='region', values='gain')

    return figure

#
# @app.callback(
#     Output("modal", "is_open"),
#     [Input("open", "n_clicks"), Input("close", "n_clicks")],
#     [State("modal", "is_open")],
# )
# def toggle_modal(n1, n2, is_open):
#     if n1 or n2:
#         return not is_open
#     return is_open
#
#
# app.layout = layout

# @app.callback(
#     [Output('id-type-area','options'),
#     Output('id-type-area','value'),
#     Output('id-slider-level','marks'),
#     Output('id-slider-level','max'),
#     Output('id-slider-level','value')
#     ],
#     [Input('id-variable-y','value')]
# )
# def update_area_selector(variable_y):
#     pass
#
# @app.callback(
#     Output('id-sankey-plot','figure'),
#     [Input('id-type-global','value'),
#     Input('id-variable-y','value'),
#     Input('id-type-area','value'),
#     Input('id-slider-level','value')
#     ])
# def update_sankey_plot(type_global,variable_y,area,level):
#

# @app.callback(
#     Output('id-sunburst-plot','figure'),
#     [Input('id-type-global','value'),
#     Input('id-variable-y','value'),
#     Input('id-slider-level','value')
#     ])
# def update_sunburst_plot(type_global,variable_y,level):

# @app.callback(
#     [Output('id-variable-x','options'),
#     Output('id-variable-x','value'),
#     ],
#     [Input('id-variable-y','value'),
#     Input('id-type-area','value')]
# )
# def update_area_variable_x(variable_y,area):

# @app.callback(
#     Output('id-scatterbox-plot','figure'),
#     [Input('id-variable-y','value'),
#     Input('id-variable-x','value'),
#     Input('id-type-area','value')]
# )
# def update_boxscatter_plot(variable_y,variable_x,area):
#
# @app.callback(
#     Output('id-parallel-plot','figure'),
#     [Input('id-variable-y','value'),
#     Input('id-type-area','value')]
# )
# def update_parallel_plot(variable_y,area):


# Run app
if __name__ == "__main__":
    app.run_server(debug=True, host='0.0.0.0')
