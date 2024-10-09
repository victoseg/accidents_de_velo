from dash import dcc, html
import plotly.express as px

# Exemple de graphique spécifique pour cette page
def specific_component(data):
    fig = px.line(
        data, 
        x="mois", 
        y="nombre_accidents", 
        title="Évolution mensuelle des accidents",
        labels={'mois': 'Mois', 'nombre_accidents': 'Nombre d\'accidents'}
    )
    
    return html.Div([
        html.H3("Graphique spécifique à cette page"),
        dcc.Graph(figure=fig)
    ])
