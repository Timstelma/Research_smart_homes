import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import datetime as dt


BS = dbc.themes.MINTY
app = dash.Dash(__name__, external_stylesheets=[BS], suppress_callback_exceptions=True)

server = app.server #needed for going Live

colors = {
    'background': '#fcffff',
    'text': '#7FDBFF',
    'cardcolor': '#40515e',
}

colors2 = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen']


df = pd.read_csv('DF_complete.csv')
df['AT'] = pd.to_datetime(df['AT'])

def create_Line_2():
    fig = go.Figure(go.Scatter(
        x = df['AT'],
        y = df['Length'],
        line=dict(
            width=3),
            connectgaps=True,
            )
        )
    fig.update_xaxes(
        rangeslider_visible=True,
        tickformatstops = [
            dict(dtickrange=[None, 1000], value="%H:%M:%S.%L ms"),
            dict(dtickrange=[1000, 60000], value="%H:%M:%S s"),
            dict(dtickrange=[60000, 3600000], value="%H:%M m"),
            dict(dtickrange=[3600000, 86400000], value="%H:%M h"),
            dict(dtickrange=[86400000, 604800000], value="%e. %b d"),
            dict(dtickrange=[604800000, "M1"], value="%e. %b w"),
            dict(dtickrange=["M1", "M12"], value="%b '%y M"),
            dict(dtickrange=["M12", None], value="%Y Y")
        ]
    )
    fig.update_layout(
        xaxis=dict(
            showline=True,
            showgrid=True,
            showticklabels=True,
            linecolor='dimgray',
            linewidth=1,
            ticks='outside',
            tickfont=dict(
                #family='Arial',
                size=12,
                color='black',
            ),
        ),
        yaxis=dict(
            showgrid=True,
            zeroline=False,
            showline=False,
            showticklabels=True,
        ),
        showlegend=False,
        plot_bgcolor='white'
    )
    fig.update_layout(
        #autosize=False,
        #width=250,
        height=450,
        margin=dict(
            l=1,
            r=1,
            b=1,
            t=30,
            pad=1
         ),
    )
    return fig

Maingraph = html.Div(
    [
        html.H4("Network Activity"), 
        dbc.Card(
            [
                dbc.CardBody(
                    [
                        #html.H1(
                        #    "Main traffic graph",
                        #    className="display-3"
                        #),
                        dcc.Graph(
                            figure= create_Line_2()
                        ),
                    ]
                ), 
            ],
            outline=True,
            color='white'
        ),
    ]
)

KPI_graphs = html.Div(
    [
        html.H4("Visualizations"),
        dbc.CardDeck(
            [
                dbc.Card(
                    [
                        #dbc.CardHeader("Network Traffic"),
                        #dbc.CardHeader(
                        #    "Packets per day"
                        #),
                        dbc.CardBody(
                            [
                                html.P(
                                    "Packets per day",
                                ),
                                html.Hr(
                                    className="my-2"
                                ),
                                #html.P("Number of Packets", className="card-text"),
                                dcc.Graph(
                                    #id='example-graph-2',
                                    figure={
                                        'data': [
                                            {'x': ['Mon', 'Tue', 'Wed'], 'y': [500, 300, 1600], 'type': 'line', 'name': 'Unknown Activity'},
                                            #{'x': ['Mon', 'Tue', 'Wed'], 'y': [2, 4, 5], 'type': 'pie', 'name': 'Known Activity'},
                                        ],
                                        'layout': {
                                            'plot_bgcolor': colors['background'],
                                            'paper_bgcolor': colors['background'],
                                            'font': {
                                                'color': colors['text']
                                            }
                                        }
                                    }
                                ),
                            ]
                        ),
                    ],
                    outline=True,
                    #color='info',
                ),
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.P(
                                "Packet size per day",
                            ),
                            html.Hr(
                                className="my-2"
                            ),
                            dcc.Graph(
                                #id='example-graph-2',
                                figure={
                                    'data': [
                                        {'x': ['Mon', 'Tue', 'Wed'], 'y': [4600, 500, 2700], 'type': 'line', 'name': 'Unknown Activity'},
                                        #{'x': ['Mon', 'Tue', 'Wed'], 'y': [2, 4, 5], 'type': 'pie', 'name': 'Known Activity'},
                                    ],
                                    'layout': {
                                        'plot_bgcolor': colors['background'],
                                        'paper_bgcolor': colors['background'],
                                        'font': {
                                            'color': colors['text']
                                        }
                                    }
                                }
                            ),
                        ]
                    ), 
                    outline=False,
                    #color="info",
                ),
                dbc.Card(
                    [
                        dbc.CardBody(
                            [
                                html.P(
                                "Package size generated per source per day",
                            ),
                            html.Hr(
                                className="my-2"
                            ),
                                dcc.Graph(
                                figure = go.Figure(
                                    data= [
                                        go.Pie(
                                            labels=['127.0.0.1:88','127.0.0.1:89','127.0.0.1:72','127.0.0.1:84','127.0.0.2:87'],
                                            values=[4500,2500,1053,500,1300],
                                        ),
                                    ],
                                    #layout= dict(
                                    #title='Simple Graph'
                                    #),
                                ),
                                    #Figure.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20, marker=dict(colors=colors, line=dict(color='#000000', width=2)))
                                #fig.show()
                                    
                                ),
                            ]
                        ), 
                    ],
                    outline=False,
                    #color="info",
                ),
                dbc.Card(
                    [
                        dbc.CardBody(
                            [
                                html.P(
                                    "Package size sent to each destinations per day",
                                ),
                                html.Hr(
                                    className="my-2"
                                ),
                                dcc.Graph(
                                    figure = go.Figure(
                                        data= [
                                            go.Pie(
                                                labels=['127.0.0.1:88','127.0.0.1:89','127.0.0.1:72','127.0.0.1:84','127.0.0.2:87','127.0.0.2:88','127.0.0.4:87','192.0.0.2:87'],
                                                values=[4500,2500,1053,500,1300,6000,3450,300],
                                            ),
                                        ],
                                    ),
                                ),
                            ]
                        ), 
                    ],
                    outline=False,
                    #color="info",
                ),
            ]
        ),
    ]
)

KPIS = html.Div(
    [
        html.H4("KPI's"),
        dbc.CardDeck(
            [
                dbc.Card(
                    [
                        #dbc.CardHeader("Network Traffic"),
                        dbc.CardBody(
                            [
                                html.H1(
                                    "10.254",
                                    className="card-title",
                                ),
                                #html.P("Number of Packets", className="card-text"),
                            ]
                        ),
                        dbc.CardFooter(
                            [               
                                html.P(
                                    [
                                        "Total number of ",
                                        html.Span(
                                            "packets",
                                            id="tim",
                                            style={"textDecoration": "underline", "cursor": "pointer"},
                                        ),
                                        " captured from your network.",
                                    ]
                                ),
                                dbc.Tooltip(
                                    "Packets, "
                                    "contain data which you and your devices send over the network.",
                                    target="tim", 
                                    hide_arrow=True,
                                    placement='right',
                                ),
                            ]
                        ),
                    ],
                    outline=True,
                    #color='info',
                ),
                dbc.Card(
                    [
                        dbc.CardBody(
                            [
                                html.H1(
                                    "20.234",
                                    className="card-title",
                                ),
                                html.P(
                                    "MegaBytes"
                                ),
                            ]
                        ),
                        dbc.CardFooter(
                            [
                                html.P(
                                    [
                                        "Total ",
                                        html.Span(
                                            "packets size",
                                            id="tom",
                                            style={"textDecoration": "underline", "cursor": "pointer"},
                                        ),
                                        " sent over your network.",
                                    ]
                                ),
                                dbc.Tooltip(
                                    "Packet size, "
                                    "is the amount of data inside a package expressed in Megabytes.",
                                    target="tom", 
                                    hide_arrow=True,
                                    placement='right'
                                ),
                            ]
                        ), 
                    ],
                    outline=False,
                    #color="info",
                ),
                dbc.Card(
                    [
                        dbc.CardBody(
                            html.H1(
                                "5",
                                className="card-title",
                            ),
                        ),
                        dbc.CardFooter(
                            [
                                html.P(
                                    [
                                        #"Number of ",
                                        html.Span(
                                            "Sources",
                                            id="tam",
                                            style={"textDecoration": "underline", "cursor": "pointer"},
                                        ),
                                        " active in your network.",
                                    ]
                                ),
                                dbc.Tooltip(
                                    "Sources, "
                                    "generate packets and sends these packets over your network.",
                                    target="tam", 
                                    hide_arrow=True,
                                    placement='right'
                                ),
                            ]
                        ), 
                    ],
                    outline=False,
                    #color="info",
                ),
                dbc.Card(
                    [
                        dbc.CardBody(
                            html.H1(
                                "8",
                                className="card-title",
                            ),
                        ),
                        dbc.CardFooter(
                            [
                                html.P(
                                    [
                                        #"Number of ",
                                        html.Span(
                                            "Destinations",
                                            id="tem",
                                            style={"textDecoration": "underline", "cursor": "pointer"},
                                        ),
                                        " active in your network.",
                                    ]
                                ),
                                dbc.Tooltip(
                                    "Destinations, "
                                    "receive packets from your network",
                                    target="tem", 
                                    hide_arrow=True,
                                    placement='right'
                                ),
                            ]
                        ), 
                    ],
                    outline=False,
                    #color="info",
                ),
            ]
        ),
    ]
)

card = dbc.Card(
    [
        dbc.CardHeader("This is the header"),
        dbc.CardBody(
            [
                html.P(
                    [
                        "I wonder what ",
                        html.Span(
                            "floccinaucinihilipilification", id="tooltip-target",
                            style={"textDecoration": "underline", "cursor": "pointer"},
                        ),
                        " means?",
                    ]
                ),
                dbc.Tooltip(
                    "Noun: rare, "
                    "the action or habit of estimating something as worthless.",
                    target="tooltip-target", 
                    hide_arrow=True,
                ),
                html.H4("Card title", className="card-title"),
                html.P("This is some card text", className="card-text"),
            ]
        ),
        dbc.CardFooter("This is the footer"),
    ],
    style={"width": "18rem"},
)

collapse = html.Div(
    [
        dbc.Button(
            "More info on KPI's",
            id="collapse-button",
            className="mb-3",
            color="info",
        ),
        dbc.Collapse(
            dbc.CardDeck(
                [
                    dbc.Card(
                        [
                            dbc.CardHeader(
                                "Header"
                            ),
                            dbc.CardBody(
                                "Additional content"
                            ),
                        ],
                        color='info',
                        inverse=True,
                        #outline=True,
                    ),
                    dbc.Card(
                        [
                            dbc.CardHeader(
                                "Header"
                            ),
                            dbc.CardBody(
                                "Additional content"
                            ),
                        ],
                        color='info',
                        inverse=True,
                        #outline=True,
                    ),
                    dbc.Card(
                        [
                            dbc.CardHeader(
                                "Header"
                            ),
                            dbc.CardBody(
                                "Additional content"
                            ),
                        ],
                        color='info',
                        inverse=True,
                        #outline=True,
                    ),
                    dbc.Card(
                        [
                            dbc.CardHeader(
                                "Header"
                            ),
                            dbc.CardBody(
                                "Additional content"
                            ),
                        ],
                        color='info',
                        inverse=True,
                        #outline=True,
                    ),
                ]
            ),
            id="collapse",
        ),
    ]
)

@app.callback(
    Output("collapse", "is_open"),
    [Input("collapse-button", "n_clicks")],
    [State("collapse", "is_open")],
)

def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

app.layout = html.Div(
    [
        #navbar,
        #dbc.Container(
        #    [
        #        html.Div(style={"height": "25px"}),
        #        tabs
        #    ],
        #),
        dbc.Container(
            [
                html.Div(style={"height": "25px"}),
                KPIS,
                html.Br(),
                #collapse,
                #html.Br(),
                KPI_graphs,
                html.Br(),
                Maingraph,
                html.Br(),
                #card,
                #html.Br(),
                #cards,
                #html.Br(),
                #row,
                #html.Br(),
                #toast,
                #html.Br(),
                #collapse,
                html.Div(style={"height": "150px"})
            ],
            fluid=True
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)