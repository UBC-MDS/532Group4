from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import altair as alt
import pandas as pd

# disable Altair limits
qwl_df = pd.read_csv("./data/bei_vita_qwl_assessment.csv")

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP, "https://codepen.io/chriddyp/pen/bWLwgP.css"]
)
server = app.server

app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Br(),
                        html.H2("Bei Vita"),
                        html.P(
                            dcc.Markdown(
                                """
                                Visualization to represent how scores for quality of
                                work life are distributed
                                """
                            )
                        )
                    ],
                    width=3
                ),
                dbc.Col(
                    [
                        html.H1("Quality of Work Life"),
                        html.H2("Client Name")
                    ],
                    width=6
                ),
                dbc.Col(
                    [
                    ],
                    width=3
                )
            ],
            align="center"
        ),
        html.Br(),

        dbc.Row(
            [
                
                dbc.Col(
                    [
                        html.Div(
                            [
                                html.Iframe(
                                    id="lineplot",
                                    style={"border-width": "0", "width": "100%", "height": "450px"}
                                ),
                                dcc.Dropdown(
                                    id='xcol-lineplot-widget',
                                    value='Total score',
                                    options=[{'label': col, 'value': col} for col in ["Total score"]]
                                )
                            ]
                        )
                    ],
                    width=9
                ),
                dbc.Col(
                    [
                   
                    ],
                    width=3
                ),
            ],
        ),
        html.Br(),

        dbc.Row(
            [
                dbc.Col(
                    [
                        
                    ],
                ),
                dbc.Col(
                    [
                        html.Div(
                            [
                                html.Iframe(
                                    id="vertical_barplot",
                                    # value="Total score",
                                    style={"border-width": "0", "width": "100%", "height": "450px"}
                                ),
                                dcc.Dropdown(
                                    id='xcol-vbarplot-widget',
                                    value='Total score',
                                    options=[{'label': col, 'value': col} for col in ["Total score"]]
                                )
                            ]
                        )
                    ]
                ),
            ],
        )
    ]
)

@app.callback(
    Output("lineplot", "srcDoc"),
    Output("vertical_barplot", "srcDoc"),
    Input('xcol-lineplot-widget', 'value'),
    Input('xcol-vbarplot-widget', 'value')
)
def vertical_barplot(xcol_lineplot, xcol_vbarplot):
    lineplot = alt.Chart(qwl_df).mark_line().encode(
        x=xcol_lineplot,
        y="count()",
    ).properties(width=600).interactive()

    vertical_barplot = alt.Chart(qwl_df).mark_bar().encode(
        x=alt.X(
            xcol_vbarplot,
            bin=alt.Bin(maxbins=5)
        ),
        y="count()",
    )

    return lineplot.to_html(), vertical_barplot.to_html(), 

if __name__ == "__main__":
    app.run_server(debug=False)