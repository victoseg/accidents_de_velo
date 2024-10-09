from dash import html

def Header():
    return html.Div([
        html.H1("Dashboard des Accidents de Vélo en France", style={'textAlign': 'center', 'marginTop': '20px'}),
    ])
