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
                            [ html.H6("Role Classification"),
                                dcc.Checklist(
                                    id = 'my_checklist_1',
                                    options = [{'label' : x , 'value' : x,'disabled':False}
                                    for x in qwl_df['Role Classification'].unique()],
                                    value = [b for b in sorted(qwl_df['Role Classification'].unique())]),

                                html.Br(),

                                html.H6("Country of Residence"),
                                dcc.Checklist(
                                    id = 'my_checklist_2',
                                    options = [{'label' : y , 'value' : y,'disabled':False}
                                    for y in qwl_df['Country of Residence '].unique()],
                                    value = [c for c in sorted(qwl_df['Country of Residence '].unique())]),
                                html.Iframe(
                                    id="lineplot",
                                    style={"border-width": "0", "width": "100%", "height": "450px"}
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
    Output("lineplot","srcDoc"),
    Output("vertical_barplot", "srcDoc"),
    Input('my_checklist_1', 'value'),
    Input('my_checklist_2', 'value'),
    Input('xcol-vbarplot-widget', 'value')
)

def vertical_barplot(my_checklist_1, my_checklist_2, xcol_vbarplot):
    df_sub = qwl_df[(qwl_df["Role Classification"].isin(my_checklist_1)) & 
                    (qwl_df["Country of Residence "].isin(my_checklist_2)) ]
    lineplot = alt.Chart(df_sub, title='How healthy are the employees feeling overall?').mark_area(
        color = "lightblue",
        interpolate = "step-after",
        line = True
    ).encode(
        alt.X("Total score"),
        alt.Y("count():Q",
              title="# of Employees",
    )).properties(width=600).interactive()

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