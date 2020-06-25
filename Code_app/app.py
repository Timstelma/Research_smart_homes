import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import datetime as dt

# link fontawesome to get the chevron icons

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

server = app.server #needed for going Live

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#021f44",
}
# the styles for the main content position it to the right of the sidebar and adds some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}
submenu_1 = [
    html.Li(
            # use Row and Col components to position the chevrons
            dbc.Row(
                [
                    dbc.Col("Home"),
                    dbc.Col(
                        html.I(className="fas fa-chevron-right mr-3"), width="auto"
                    ),
                ],
                className="my-1",
            ),
            id="submenu-1",
            style={"color": "white"},
    ),
    # we use the Collapse component to hide and reveal the navigation links
    html.Li(
        [
            dbc.NavLink("Introductie", href="/page-1/1"), #href="https://forms.gle/dvuxj71bzzfVVUVq8"),
            #dbc.NavLink("Statistics", href="/page-1/2"),
            #dbc.NavLink("Network activity", href="/page-1/3"),
            #dbc.NavLink("Network actors", href="/page-1/4"),
        ],
        #id="submenu-1-collapse",
    ),
]
submenu_2 = [
    html.Li(
        dbc.Row(
            [
                dbc.Col("Dashboard"),
            ],
            className="my-1",
        ),
        id="submenu-2",
        style={"color": "white"},
    ),
    html.Li(
        [
            dbc.NavLink("Statistieken", href="/page-1/2"
            ),
            dbc.NavLink("Apparaten classificeren", href="/page-1/3"
            ),
            #dbc.NavLink("Page 2.1", href="/page-2/1"),
            #dbc.NavLink("Page 2.2", href="/page-2/2"),
            html.Br(
            ),
        ],
        #id="submenu-3-collapse",
    ),
]
sidebar = html.Div(
    [
        html.H6("App", className="display-4", style={"color": "mistyrose"}),
        html.Hr(),
        dbc.Nav(submenu_1 + submenu_2, vertical=True), 
    ],
    style=SIDEBAR_STYLE,
    id="sidebar",
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

df = pd.read_csv('review_set2.csv')
df['AT'] = pd.to_datetime(df['AT'])
df['TS'] = df['AT'].astype('int64') // 10**9



def create_KPI_1():
    fig = go.Figure(go.Indicator(
    mode = "number", #+delta",
    value = df.Length.count(),
    title = {"text": "Communicatie" },
    #number = {'prefix': "$"},
    #delta = {'position': "top", 'reference': 320},
    domain = {'x': [0, 1], 'y': [0, 1]}))

    fig.update_layout(
        #autosize=False,
        #width=250,
        height=150,
        margin=dict(
            l=1,
            r=1,
            b=1,
            t=50,
            pad=1
         ),
        #paper_bgcolor = 'linen') #can also use linen or any other pre def css value
    )
    return fig

def create_KPI_2():
    fig = go.Figure(go.Indicator(
    mode = "number", #+delta",
    value = df.Length.sum() / 1000000,
    title = {"text": "Communicatie<br><span style='font-size:0.8em;color:gray'>(in MegaBytes)</span>"},
    #number = {'suffix': "MB"},
    #delta = {'position': "top", 'reference': 320},
    domain = {'x': [0, 1], 'y': [0, 1]}))

    fig.update_layout(
        #autosize=False,
        #width=250,
        height=150,
        margin=dict(
            l=1,
            r=1,
            b=1,
            t=50,
            pad=1
         ),
        #paper_bgcolor = 'linen') #can also use linen or any other pre def css value
    )
    return fig

def create_KPI_3():
    fig = go.Figure(go.Indicator(
    mode = "number", #+delta",
    value = df.SA.nunique(),
    title = {"text": "Bronnen" },
    #number = {'prefix': "$"},
    #delta = {'position': "top", 'reference': 320},
    domain = {'x': [0, 1], 'y': [0, 1]}))

    fig.update_layout(
        #autosize=False,
        #width=250,
        height=150,
        margin=dict(
            l=1,
            r=1,
            b=1,
            t=50,
            pad=1
         ),
        #paper_bgcolor = 'linen') #can also use linen or any other pre def css value
    )
    return fig

def create_KPI_4():
    fig = go.Figure(go.Indicator(
    mode = "number", #+delta",
    value = df.DA.nunique(),
    title = {"text": "Bestemmingen" },
    #number = {'prefix': "$"},
    #delta = {'position': "top", 'reference': 320},
    domain = {'x': [0, 1], 'y': [0, 1]}))

    fig.update_layout(
        #autosize=False,
        #width=250,
        height=150,
        margin=dict(
            l=1,
            r=1,
            b=1,
            t=50,
            pad=1
         ),
        #paper_bgcolor = 'linen') #can also use linen or any other pre def css value
    )
    return fig

def create_Pie_1():
    fig = go.Figure(
        go.Histogram(
            x= df['SA'],
            bingroup=1, name='Bestemming', marker=dict(
            color='rebeccapurple',
            line=dict(color='rebeccapurple', width=1)
            )
        ),
    )
    fig.add_trace(
        go.Histogram(x= df['DA'] ,bingroup=1, name='Bron', 
            marker=dict(
            color='palevioletred',
            line=dict(color='palevioletred', width=1)
            )
        )
    )
    fig.update_layout(
        title_text='Communicatie per actor', # title of plot
        barmode='stack',
        bargap=0.2,
        xaxis= {'categoryorder':'total descending'},
        height=450,
        margin=dict(
            l=1,
            r=1,
            b=1,
            t=30,
            pad=1
         ),
    )
    fig.update_xaxes(
        rangeslider_visible=True,
    )
    return fig

def create_Pie_2():
    df_sub3 = df.groupby('DA').sum().reset_index()
    df_sub4 = df.groupby('SA').sum().reset_index()

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=df_sub3['DA'],
        y=df_sub3['Length'] / 1000000,
        name='Bestemming',
        
        marker=dict(
            color='rebeccapurple',
            line=dict(color='rebeccapurple', width=1)
        )
    ))
    fig.add_trace(go.Bar(
        x=df_sub4['SA'],
        y=df_sub4['Length'] / 1000000,
        name='Bron',
        
        marker=dict(
            color='palevioletred',
            line=dict(color='palevioletred', width=1)
        )
    ))
    fig.update_layout(barmode='stack')

    fig.update_xaxes(
        rangeslider_visible=True,
    )
    fig.update_layout(
        title_text='Communicatie per actor (in MB)', # title of plot
        barmode='stack',
        bargap=0.2,
        xaxis= {'categoryorder':'total descending'},
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

def create_Pie_3():
    data_1 = [df.groupby('DA')['DA'].nunique().count(), df.groupby('SA')['SA'].nunique().count()]
    colors = ['rebeccapurple','palevioletred']
    labels = ['Bestemming','Bron']
    values = data_1
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.3)])
    fig.update_layout(title_text="Actoren per communicatierichting")
    fig.update_layout(
        #autosize=False,
        #width=250,
        #height=300,
        margin=dict(
            l=1,
            r=1,
            b=1,
            t=30,
            pad=1
        ),
    )
    fig.update_traces(
        textposition='inside',
        hoverinfo='label+value',
        textinfo='percent',
        textfont_size=20,
        marker=dict(
            colors=colors,
        #    line=dict(
        #        color='#000000', width=2
        #    )
        )
    )
    return fig

def create_Line_1():
    df_sub = df.set_index('AT')
    df_sub = df_sub.groupby(pd.Grouper(freq='300S')).nunique().reset_index()
    colors = ['palevioletred', 'rebeccapurple']
    labels = ['Bron', 'Bestemming']
    y_data = [
        df_sub['SA'],
        df_sub['DA']
    ]
    
    fig = go.Figure()
    for i in range(0, 2):
        fig.add_trace(go.Scatter(x=df_sub['AT'], y=y_data[i], mode='lines+markers',
            name=labels[i],
            line=dict(color=colors[i], width=3),
            marker=dict(color=colors[i], size=8),
            connectgaps=True,
        ),
    )
    fig.update_xaxes(
        #rangeslider_visible=True,
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
        showlegend=True,
        plot_bgcolor='white'
    )
    fig.update_layout(title_text="Actoren over tijd")
    fig.update_layout(
        #autosize=False,
        #width=300,
        height=300,
        margin=dict(
            l=1,
            r=1,
            b=1,
            t=30,
            pad=1
        ),
    )
    return fig

def create_Line_2():
    fig = go.Figure(go.Scatter(
        x = df['AT'],
        y = df['Length'],
        line=dict(color='lightcoral',
            width=3),
            connectgaps=True,
            )
        )
    fig.update_xaxes(
        #rangeslider_visible=True,
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
        plot_bgcolor='white',
        title_text="Netwerk communicatie over tijd",
        #autosize=False,
        #width=250,
        height=300,
        margin=dict(
            l=1,
            r=1,
            b=1,
            t=30,
            pad=1
        ),
    )
    return fig

def create_Line_3():
    df_sub = df.set_index('AT')
    df_sub = df_sub.groupby(pd.Grouper(freq='300S')).count().reset_index()
    colors = ['coral', 'cadetblue']
    labels = ['Communicatie']
    y_data = [
        df_sub['SA'],
        df_sub['DA']
    ]
    
    fig = go.Figure()
    for i in range(0, 1):
        fig.add_trace(go.Scatter(x=df_sub['AT'], y=y_data[i], mode='lines+markers',
            name=labels[i],
            line=dict(color=colors[i], width=3),
            marker=dict(color=colors[i], size=8),
            connectgaps=True,
        ),
    )
    fig.update_xaxes(
        #rangeslider_visible=True,
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
        showlegend=True,
        plot_bgcolor='white'
    )
    fig.update_layout(title_text="Communicatie over tijd")
    fig.update_layout(
        #autosize=False,
        #width=300,
        height=300,
        margin=dict(
            l=1,
            r=1,
            b=1,
            t=30,
            pad=1
        ),
    )
    return fig

def create_Line_4():
    df_sub = df.set_index('AT')
    df_sub = df_sub.groupby(pd.Grouper(freq='300S')).sum().reset_index()
    colors = ['mediumturquoise', 'cadetblue']
    labels = ['Communicatie']
    y_data = [
        df_sub['Length'] / 1000000 ,
        #df_sub['DA']
    ]
    
    fig = go.Figure()
    for i in range(0, 1):
        fig.add_trace(go.Scatter(x=df_sub['AT'], y=y_data[i], mode='lines+markers',
            name=labels[i],
            line=dict(color=colors[i], width=3),
            marker=dict(color=colors[i], size=8),
            connectgaps=True,
        ),
    )
    fig.update_xaxes(
        #rangeslider_visible=True,
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
        showlegend=True,
        plot_bgcolor='white'
    )
    fig.update_layout(title_text="Communicatie over tijd (in MB)")
    fig.update_layout(
        #autosize=False,
        #width=300,
        height=300,
        margin=dict(
            l=1,
            r=1,
            b=1,
            t=30,
            pad=1
        ),
    )
    return fig

Introduction = html.Div(
    [
        #html.H4("Smarthome environment"),
        dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H4("Introductie", className="card-title"),
                    html.P(
                        'Op deze pagina vind je een dashboard die Wi-Fi netwerkcommunicatie verzamelt en analyseert. De data die gebruikt wordt is door apparaten, verbonden met het Wi-Fi netwerk, gegenereerd. Door het netwerk kunnen apparaten onderling communiceren, zodat je handelingen kunt uitbesteden aan deze apparaten. Deze apparaten worden ook wel ‘slimme apparaten’ genoemd en de toepassing op de thuissituatie een ‘smart home’ omgeving.'
                    ),
                    html.P(
                        'Communicatie tussen deze slimme apparaten is versleuteld zodat er van buiten het netwerk niet kan worden geluisterd wat er wordt gezegd. Wat wel kan worden gezien is wie er communiceert (Bron & Bestemming) maar niet wat voor apparaat dit is (zie ook afbeelding hieronder).'
                    ),
                    html.P(
                        'Wat ook wordt gezien is een hartslag van communicatie. Deze hartslag wordt door dit dashboard gebruikt om een voorspelling te maken wat voor slimme apparaten er communiceren.'
                    ),
                    html.P(
                        'Probeer aan de hand van dit dashboard te onderzoeken wanneer er veel wordt gecommuniceerd in dit netwerk en door welk apparaat dit gebeurt. Vul daarna de evaluatie in hieronder op de pagina. Kun je uitzoeken welk apparaat voornamelijk actief was om 20:19?'
                    ),
                    #dbc.Button("Go to questionnaire", color="primary", href="https://forms.gle/dvuxj71bzzfVVUVq8", external_link=True),
                ]
            ),
            dbc.CardImg(src="https://i.pinimg.com/originals/b5/c5/61/b5c5611c34b680021d48289dc3fe8d75.png", bottom=True),
        ],
        #style={"width": "18rem"},
        )
    ]
)

KPIS = html.Div(
    [
        html.H4("Statistieken"),
        dbc.CardDeck(
            [
                dbc.Card(
                    [
                        #dbc.CardHeader("Network Traffic"),
                        dbc.CardBody(
                            [
                                #html.H1(
                                #    "test",
                                #    className="card-title",
                                #),
                                dcc.Graph(
                                    figure = create_KPI_1()
                                )
                                #html.P("Number of Packets", className="card-text"),
                            ]
                        ),
                        dbc.CardFooter(
                            [               
                                html.P(
                                    [
                                        "hoeveelheid aan ",
                                        html.Span(
                                            "communicatie",
                                            id="kpi1",
                                            style={"textDecoration": "underline", "cursor": "pointer"},
                                        ),
                                        " in het netwerk.",
                                    ]
                                ),
                                dbc.Tooltip(
                                    "Wordt ook wel uitgedrukt in pakketjes. ",
                                    target="kpi1", 
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
                                dcc.Graph(figure = 
                                    create_KPI_2()
                                )
                            ]
                        ),
                        dbc.CardFooter(
                            [
                                html.P(
                                    [
                                        "Communicatie ",
                                        html.Span(
                                            "grootte,",
                                            id="kpi2",
                                            style={"textDecoration": "underline", "cursor": "pointer"},
                                        ),
                                        " verstuurd over het network.",
                                    ]
                                ),
                                dbc.Tooltip(
                                    "Samen met de hoeveelheid pakketjes maakt dit de communicatie 'hartslag'.",
                                    target="kpi2", 
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
                            dcc.Graph(figure = 
                                    create_KPI_3()
                                )
                            #html.H1(
                            #    "5",
                            #    className="card-title",
                            #),
                        ),
                        dbc.CardFooter(
                            [
                                html.P(
                                    [
                                        #"Number of ",
                                        html.Span(
                                            "Bronnen",
                                            id="kpi3",
                                            style={"textDecoration": "underline", "cursor": "pointer"},
                                        ),
                                        " actief in het smart home network.",
                                    ]
                                ),
                                dbc.Tooltip(
                                    "Genereren communicatie en kunnen intern of extern zijn.",
                                    target="kpi3", 
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
                            dcc.Graph(figure = 
                                    create_KPI_4()
                            ),
                            #html.H1(
                            #    "8",
                            #    className="card-title",
                            #),
                        ),
                        dbc.CardFooter(
                            [
                                html.P(
                                    [
                                        #"Number of ",
                                        html.Span(
                                            "Bestemmingen",
                                            id="kpi4",
                                            style={"textDecoration": "underline", "cursor": "pointer"},
                                        ),
                                        " actief in het smart home network.",
                                    ]
                                ),
                                dbc.Tooltip(
                                    "Ontvangen communicatie en kunnen intern of extern zijn.",
                                    target="kpi4", 
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

collapse = html.Div(
    [
        dbc.Collapse(
            dbc.CardDeck(
                [
                    dbc.Card(
                        [
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
            id="submenu-3-collapse",
        ),
        html.Br(
        ),
        dbc.Button(
            "Hide/Show additional info",
            id="submenu-2",
            className="mb-3",
            color="info",
        ),
    ]
)

KPI_graphs = html.Div(
    [
        html.H4("Visualisatie"),
        dbc.CardDeck(
            [
                dbc.Card(
                    [
                        dbc.CardBody(
                            [
                                dcc.Graph(
                                figure = create_Line_3(),
                                ),
                            ]
                        ),
                    ],
                    outline=True,
                    #color='white',
                ),
                dbc.Card(
                    [
                        dbc.CardBody(
                            [
                                dcc.Graph(
                                figure = create_Line_4()
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
                                dcc.Graph(
                                figure = create_Line_1()
                                ),
                            ]
                        ),
                    ],
                    outline=False,
                    #color="info",
                ),
            ]
        )
    ]
)

KPI_graphs_2 = html.Div(
    [
        #html.H4("Visualizations"),
        dbc.CardDeck(
            [
                dbc.Card(
                    [
                        dbc.CardBody(
                            [
                                dcc.Graph(
                                figure = create_Pie_1(),
                                ),
                            ]
                        ),
                    ],
                    outline=True,
                    #color='white',
                ),
                dbc.Card(
                    [
                        dbc.CardBody(
                            [
                                dcc.Graph(
                                figure = create_Pie_2()
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
                                dcc.Graph(
                                figure = create_Pie_3()
                                ),
                            ]
                        ),
                    ],
                    outline=False,
                    #color="info",
                ),
            ]
        )
    ]
)

Maingraph = html.Div(
    [
        html.H4("Netwerk communicatie selecteren"), 
        dbc.Card(
            [
                dbc.CardBody(
                    [
                        #html.H1(
                        #    "Main traffic graph",
                        #    className="display-3"
                        #),
                        dcc.Graph(id='the_graph'
                            #figure= create_Line_2()
                        ),
                    ]
                ), 
            ],
            outline=True,
            color='white'
        ),
    ]
)

Maingraph_2 = html.Div(
    [
        html.H4("Voorspelling van actoren"),
        dbc.CardDeck(
            [
                dbc.Card(
                    [
                        dbc.CardBody(
                            [
                                dcc.Graph(
                                id='the_graph2'
                                ),
                            ]
                        ),
                    ],
                    outline=True,
                    #color='white',
                ),
                dbc.Card(
                    [
                        dbc.CardBody(
                            [
                                dcc.Graph(
                                id='the_graph3'
                                ),
                            ]
                        ),
                    ],
                    outline=False,
                    #color="info",
                ),
            ]
        )
    ]
)

Rangeslider = html.Div(
    [
        html.H5("Schuifregelaar tijd"),
        html.Br(),
        dcc.RangeSlider(
            id='my-range-slider',
            min=df.TS.min(),
            max=df.TS.max(),
            step=1,
            value=[df.TS.min(), df.TS.max()]
        ),
    #html.Div(id='the_time')
    ]
)

#@app.callback(
#    Output('the_time', 'children'),
#    [Input('my-range-slider', 'value')])

#def update_output(value):
#    return 'You have selected "{}" seconds'.format(value)

@app.callback(
    Output('the_graph', 'figure'),
    [Input('my-range-slider', 'value')])

def update_graph(chosen_time):

    dff=df[(df['TS']>=chosen_time[0])&(df['TS']<=chosen_time[1])]

    fig = go.Figure(go.Scatter(
        x = dff['AT'],
        y = dff['Length'],
        line=dict(color='mediumturquoise',
            width=3),
            connectgaps=True,
            )
        )
    fig.update_xaxes(
        #rangeslider_visible=True,
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
        plot_bgcolor='white',
        title_text="Netwerk communicatie over tijd",
        #autosize=False,
        #width=250,
        height=300,
        margin=dict(
            l=1,
            r=1,
            b=1,
            t=30,
            pad=1
        ), 
    )
    return fig

@app.callback(
    Output('the_graph2', 'figure'),
    [Input('my-range-slider', 'value')])

def update_graph_2(chosen_time):
    
    dff=df[(df['TS']>=chosen_time[0])&(df['TS']<=chosen_time[1])]

    #dff3 = dff.groupby('DSTI').sum().reset_index()
    dff4 = dff.groupby('SRCE').sum().reset_index()

    fig = go.Figure()
    #fig.add_trace(go.Bar(
    #    x=dff3['DSTI'],
    #    y=dff3['Length'] / 1000000,
    #    name='Bestemming',
    #    
    #    marker=dict(
    #        color='rebeccapurple',
    #        line=dict(color='rebeccapurple', width=1)
    #    )
    #))
    fig.add_trace(go.Bar(
        x=dff4['SRCE'],
        y=dff4['Length'] / 1000000,
        name='Bron',
        
        marker=dict(
            color='lightcoral',
            line=dict(color='palevioletred', width=1)
        )
    ))
    fig.update_layout(barmode='stack')

    fig.update_xaxes(
        rangeslider_visible=False,
    )
    fig.update_layout(
        title_text='Voorspelling van Apparaat', # title of plot
        barmode='stack',
        bargap=0.2,
        xaxis= {'categoryorder':'total descending'},
        height=350,
        margin=dict(
            l=1,
            r=1,
            b=1,
            t=30,
            pad=1
        ),
    )
    return fig

@app.callback(
    Output('the_graph3', 'figure'),
    [Input('my-range-slider', 'value')])

def update_graph_3(chosen_time):

    dff=df[(df['TS']>=chosen_time[0])&(df['TS']<=chosen_time[1])]

    #dff3 = dff.groupby('DA').sum().reset_index()
    dff4 = dff.groupby('SA').sum().reset_index()

    fig = go.Figure()
    #fig.add_trace(go.Bar(
    #    x=dff3['DA'],
    #    y=dff3['Length'] / 1000000,
    #    name='Bestemming',
    #    
    #    marker=dict(
    #        color='rebeccapurple',
    #        line=dict(color='rebeccapurple', width=1)
    #    )
    #))
    fig.add_trace(go.Bar(
        x=dff4['SA'],
        y=dff4['Length'] / 1000000,
        name='Bron',
        
        marker=dict(
            color='palevioletred',
            line=dict(color='palevioletred', width=1)
        )
    ))
    fig.update_layout(barmode='stack')

    fig.update_xaxes(
        rangeslider_visible=False,
    )
    fig.update_layout(
        title_text='Apparaat ID (MAC address)', # title of plot
        barmode='stack',
        bargap=0.2,
        xaxis= {'categoryorder':'total descending'},
        height=350,
        margin=dict(
            l=1,
            r=1,
            b=1,
            t=30,
            pad=1
        ),
    )
    return fig


app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

# this function is used to toggle the is_open property of each Collapse
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

for i in [1,2,3]:
    app.callback(
        Output(f"submenu-{i}-collapse", "is_open"),
        [Input(f"submenu-{i}", "n_clicks")],
        [State(f"submenu-{i}-collapse", "is_open")],
    )(toggle_collapse)

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])

def render_page_content(pathname):
    if pathname in ["/", "/page-1/1"]:
        return Introduction, dbc.Jumbotron(
            [
                html.H4("Klaar met rondkijken?"),
                html.Hr(),
                html.P("Geef een score op 9 vragen met betrekking wat je hebt gezien en geleerd in dit dashboard."),
                dbc.Button("Ga naar scorelijst", color="primary", href="https://forms.gle/dvuxj71bzzfVVUVq8", external_link=True, target='blank'),
                html.P("Beantwoord vragen met betrekking op gebruik, data en informatie."),
                dbc.Button("Ga naar vragenlijst", color="primary", href="https://forms.gle/MmT3Ytr8GH5kHtAN7", external_link=True, target='blank'),
            ]
        ) 
    elif pathname == "/page-1/2": 
        return KPIS, html.Br(), KPI_graphs, html.Br(), KPI_graphs_2
    elif pathname == "/page-1/3":
        return Maingraph, Rangeslider, Maingraph_2 
    elif pathname == "/page-1/4":
        return html.P("Works")
    #elif pathname == "/page-2/2":
    #    return html.P("No way! This is page 2.2!")
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

if __name__ == "__main__":
    app.run_server()

    