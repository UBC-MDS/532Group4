from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import altair as alt
import pandas as pd

# disable Altair limits
qwl_df = pd.read_csv("../data/bei_vita_qwl_assessment.csv")

# NEW Data wrangling for vertical bar graph
workshop_topics = ['Stress Optimization',
              'Mindset Coaching',
              'Sleep Strategies',
              'Social Wellbeing',
              'Leadership and Teamwork',
              'Physical Health & Fitness',
              'Nutrition & Gut Health']

temp = qwl_df.iloc[:,55:62]
temp = temp.set_axis(workshop_topics, axis=1)
temp['Country'] = qwl_df.iloc[:,4]
temp = temp.set_index('Country')

vg_df = temp.melt(var_name = "Workshop_Topic", value_name = "Preference", ignore_index = False)
vg_df = vg_df.reset_index(level=0)

#Dash app
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
                                html.H6("Country of Residence"),
                                dcc.Dropdown(
                                    id="my_checklist",
                                    options = [{'label' : y , 'value' : y,'disabled':False}
                                    for y in qwl_df['Country of Residence '].unique()],
                                    value = [c for c in sorted(qwl_df['Country of Residence '].unique())]),
                                html.Iframe(
                                    id="lineplot",
                                    style={"border-width": "0", "width": "100%", "height": "340px"}
                                )
                            ]
                        )
                    ],
                    width=12
                )
            ],
        ),
        # html.Br(),

        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Iframe(
                            id='horizontal_barplot',
                            style={'border-width': '0', 'width': '100%', 'height': '450px'})  

                        ],
                    width=6
                ),
                dbc.Col(
                    [
                        html.Div(
                            [ 
                                html.H6("Nationality"),
                                dcc.Dropdown(
                                    id='xcountry-widget',
                                    value=vg_df.Country[0],  # REQUIRED for page to load with a graph
                                    options=[{'label': c, 'value': c} for c in vg_df.Country.unique()]
                                ),
                                html.Iframe(
                                    id='Country',
                                    style={'border-width': '0', 'width': '100%', 'height': '450px'}
                                )
                            ]
                        ),
                    ],
                )
            ],
        )
    ]
)

@app.callback(
    Output("lineplot", "srcDoc"),
    Output('Country', 'srcDoc'),
    Output("horizontal_barplot", "srcDoc"),
    Input('my_checklist', 'value'),
    Input('xcountry-widget', 'value')
)
def vertical_barplot(my_checklist, xcol_vbarplot):
    plot_data = qwl_df[(qwl_df['Country of Residence '].isin([my_checklist]))]

    lineplot = alt.Chart(plot_data, title='How healthy are the employees feeling overall?').mark_area(
        color = "lightblue",
        interpolate = "step-after",
        line = True
    ).encode(
        alt.X("Total score"),
        alt.Y("count():Q",
              title="# of Employees",
    )).properties(width=750, height=250).interactive()

    #vertical boxplot
    data = vg_df[(vg_df['Country'] == xcol_vbarplot)]
    vertical_boxplot = alt.Chart(data, title = "Workshop Preference (lower is more important)").mark_boxplot().encode(
        x = 'Workshop_Topic',
        y = 'Preference',
        color = alt.Color('Workshop_Topic', legend=None)
    ).properties(
        width=300,
        height=250
    )
    
    #horizontal barchart
    col_name = '17. I experience MEANINGFULNESS at work ... (e.g. inspired, trusted, respected, purpose, seen and heard, acknowledged, fulfilled, growth, contribution to something greater, etc.) '

    plot_data = plot_data[col_name].value_counts().to_frame().reset_index()
    plot_data = plot_data.rename(columns={col_name:'Count', 'index':'Response'})

    chart = alt.Chart(plot_data, title='How frequently do employees find meaningfulness at work?').mark_bar().encode(
        x='Count:Q',
        y='Response:O',  
    ).properties(
        width=300,
        height=350
    )

    return lineplot.to_html(), vertical_boxplot.to_html(), chart.to_html()

if __name__ == "__main__":
    app.run_server(debug=False)
