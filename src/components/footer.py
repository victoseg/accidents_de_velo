from dash import html

def Footer():
    return html.Div([
        html.P("© 2024, Projet Dashboard - Analyse des Accidents de Vélo", style={'textAlign': 'center', 'padding': '20px'})
    ], style={'position': 'fixed', 'left': '0', 'bottom': '0', 'width': '100%', 'backgroundColor': '#f1f1f1'})
