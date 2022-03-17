from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import altair as alt
import pandas as pd

# disable Altair limits
qwl_df = pd.read_csv("data/bei_vita_qwl_assessment.csv")

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
                        html.H3("Bei Vita"),
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
                        html.H2("Quality of Work Life"),
                        html.H3("Client Name: HDBC Bank")
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
                                    id = 'my_checklist_1',
                                    options = [{'label' : y , 'value' : y,'disabled':False}
                                    for y in qwl_df['Country of Residence '].unique()],
                                    value = 'HK & Macau'),

                                html.H6("Role Classification"),
                                dcc.Dropdown(
                                    id = 'my_checklist_2',
                                    options = [{'label' : x , 'value' : x,'disabled':False}
                                    for x in qwl_df['Role Classification'].unique()],
                                    value = 'Entry (Associate)'),

                                html.Iframe(
                                    id="histogram",
                                    style={"border-width": "0", "width": "100%", "height": "370px"}
                                )
                            ]
                        )
                    ],
                    width=12
                )
            ],
        ),

        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Iframe(
                            id='horizontal_barplot',
                            style={'border-width': '0', 'width': '100%', 'height': '500px'})  
                        ],
                    width=6
                ),
                dbc.Col(
                    [
                        html.Div(
                            [
                            html.Iframe(
                                id='Country',
                                style={'border-width': '0', 'width': '100%', 'height': '575px'})
                            ]
                        ),
                    ],
                )
            ],
        )   
    ]
)

@app.callback(
    Output('histogram', 'srcDoc'),
    Output("horizontal_barplot", "srcDoc"),
    Output('Country', 'srcDoc'),
    Input('my_checklist_1', 'value'),
    Input('my_checklist_2', 'value')
)

def vertical_barplot(my_checklist_1,my_checklist_2):
    plot_data = qwl_df[(qwl_df["Country of Residence "].isin([my_checklist_1])) & 
                        (qwl_df["Role Classification"].isin([my_checklist_2]))]

    #histogram
    histogram = alt.Chart(plot_data, ).mark_bar(
        color = "lightblue").encode(
        alt.X("Total score", bin = True),
        alt.Y("count():Q",
              title="# of Employees", axis = alt.Axis(values = list(range(1,17,1)))
    )).properties(width=750, height=250, title= {'text': ['How healthy are the employees feeling overall?'],'subtitle': 'At country and designation level'}).interactive()

    #horizontal barchart
    col_name = '17. I experience MEANINGFULNESS at work ... (e.g. inspired, trusted, respected, purpose, seen and heard, acknowledged, fulfilled, growth, contribution to something greater, etc.) '

    plot_data = plot_data[col_name].value_counts().to_frame().reset_index()
    plot_data = plot_data.rename(columns={col_name:'Count', 'index':'Response'})

    chart = alt.Chart(plot_data).mark_bar().encode(
        x='Count:Q',
        y='Response:O',
        color = alt.Color('Response', legend=None) 
    ).properties(
        width=300,
        height=350, title = {'text': ['How frequently do employees find meaningfulness at work?'],'subtitle': 'At country and designation level'}
    )

    #vertical boxplot
    # NEW Data wrangling for vertical bar graph
    plot_data_2 = qwl_df[(qwl_df["Country of Residence "].isin([my_checklist_1]))]

    workshop_topics = ['Stress Optimization',
                        'Mindset Coaching',
                        'Sleep Strategies',
                        'Social Wellbeing',
                        'Leadership and Teamwork',
                        'Physical Health & Fitness',
                        'Nutrition & Gut Health']

    temp = plot_data_2.iloc[:,55:62]
    temp = temp.set_axis(workshop_topics, axis=1)
    temp['Country'] = plot_data_2.iloc[:,4]
    temp = temp.set_index('Country')

    vg_df = temp.melt(var_name = "Workshop_Topic", value_name = "Preference", ignore_index = False)
    vg_df = vg_df.reset_index(level=0)


    #data = vg_df[(vg_df['Country'].isin([my_checklist_1]))]
    vertical_boxplot = alt.Chart(vg_df).mark_boxplot().encode(
        x = 'Workshop_Topic',
        y = 'Preference',
        color = alt.Color('Workshop_Topic', legend=None)
    ).properties(
        width=300,
        height=350,title = {'text': ["Workshop Preference (lower is more important)"],'subtitle': 'At country level'}
    )

    return histogram.to_html(), chart.to_html(), vertical_boxplot.to_html()

if __name__ == "__main__":
    app.run_server(debug=False)
