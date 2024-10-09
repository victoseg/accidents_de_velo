# import dash
# from dash import dcc, html
# from dash.dependencies import Input, Output
# from src.components import navbar  # Barre de navigation
# from src.pages import home, about  # Import des pages principales
# from src.pages.more_complex_page.layout import layout as data_analysis_layout  # Import du layout pour la page d'analyse des données
# import pandas as pd

# # Charger les données nettoyées depuis le fichier cleaned
# data = pd.read_csv('data/cleaned/cleaneddata.csv', low_memory=False)

# # Créer l'application Dash
# app = dash.Dash(__name__)
# app.title = "Dashboard des Accidents de Vélo"

# # Layout principal avec barre de navigation et routage
# app.layout = html.Div([
#     dcc.Location(id='url', refresh=False),  # Gère les changements d'URL pour la navigation
#     navbar.Navbar(),  # Affiche la barre de navigation
#     html.Div(id='page-content'),  # Affiche le contenu des différentes pages
# ])

# # Callback pour gérer le routage entre les différentes pages
# @app.callback(Output('page-content', 'children'),
#               [Input('url', 'pathname')])
# def display_page(pathname):
#     if pathname == '/data-analysis':
#         return data_analysis_layout  # Page d'analyse des données avec les graphiques
#     elif pathname == '/about':
#         return about.layout  # Page "À propos"
#     else:
#         return home.layout  # Page d'accueil par défaut

# # Lancer le serveur Dash
# if __name__ == '__main__':
#     app.run_server(debug=True)




# CELUI QUI MARCHE LE MIEUX
# import os
# from flask import send_from_directory
# from dash import dcc, html
# import dash
# from dash.dependencies import Input, Output
# from src.pages import home, about, simple_page
# from src.pages.more_complex_page.layout import data_analysis_layout
# from src.components.navbar import Navbar

# # Charger Google Fonts pour une belle police
# app = dash.Dash(__name__, external_stylesheets=[
#     "https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap"
# ])
# app.title = "Dashboard des Accidents de Vélo"

# # Configurer le layout principal avec styles globaux
# app.layout = html.Div(
#     style={
#         'fontFamily': 'Roboto, sans-serif',  # Appliquer la police Roboto
#         'padding': '20px'                    # Espacement global
#     },
#     children=[
#         dcc.Location(id='url', refresh=False),  # Permet de gérer les URL
#         Navbar(),  # Barre de navigation
#         html.Div(id='page-content')  # Contenu dynamique en fonction de la page sélectionnée
#     ]
# )

# # Route pour servir des fichiers depuis le dossier 'images'
# @app.server.route('/images/<path:path>')
# def serve_image(path):
#     return send_from_directory(os.path.join(os.getcwd(), 'images'), path)

# # Callbacks pour la navigation entre les pages
# @app.callback(
#     Output('page-content', 'children'),
#     [Input('url', 'pathname')]
# )
# def display_page(pathname):
#     if pathname == '/':
#         return home.layout  # Page d'accueil
#     elif pathname == '/about':
#         return about.layout  # Page "À propos"
#     elif pathname == '/data-analysis':
#         return data_analysis_layout  # Page d'analyse des données
#     else:
#         return simple_page.layout  # Page par défaut ou page non trouvée
# # Lancer le serveur Dash
# if __name__ == '__main__':
#     app.run_server(debug=True)


# #Importation de l'application Dash à partir du fichier app.py
# from app import app  # Maintenant, app est importé depuis app.py

# from dash import dcc, html
# from dash.dependencies import Input, Output
# from src.components import navbar  # Barre de navigation
# from src.pages import home, about  # Import des pages principales
# from src.pages.more_complex_page.layout import data_analysis_layout  # Import du layout pour la page d'analyse des données

# # Configurer le layout principal avec navigation
# app.layout = html.Div([
#     dcc.Location(id='url', refresh=False),  # Permet de gérer les URL
#     navbar.Navbar(),  # Barre de navigation
#     html.Div(id='page-content')  # Contenu dynamique en fonction de la page sélectionnée
# ])

# # Callbacks pour la navigation entre les pages
# @app.callback(
#     Output('page-content', 'children'),
#     [Input('url', 'pathname')]
# )
# def display_page(pathname):
#     if pathname == '/':
#         return home.layout  # Page d'accueil
#     elif pathname == '/about':
#         return about.layout  # Page "À propos"
#     elif pathname == '/data-analysis':
#         return data_analysis_layout  # Page d'analyse des données
#     else:
#         return "404 - Page not found"

# # Lancer le serveur Dash
# if __name__ == '__main__':
#     app.run_server(debug=True)



# import os
# from flask import send_from_directory
# from dash import dcc, html
# import dash
# from dash.dependencies import Input, Output
# from src.pages import home, about
# from src.pages.more_complex_page.layout import data_analysis_layout
# from src.components.navbar import Navbar

# # Charger Google Fonts pour une belle police
# app = dash.Dash(__name__, external_stylesheets=[
#     "https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap"
# ])
# app.title = "Dashboard des Accidents de Vélo"

# # Configurer le layout principal avec styles globaux
# app.layout = html.Div(
#     style={
#         'fontFamily': 'Roboto, sans-serif',  # Appliquer la police Roboto
#         'padding': '20px'                    # Espacement global
#     },
#     children=[
#         dcc.Location(id='url', refresh=False),  # Permet de gérer les URL
#         Navbar(),  # Barre de navigation
#         html.Div(id='page-content')  # Contenu dynamique en fonction de la page sélectionnée
#     ]
# )

# # Route pour servir des fichiers depuis le dossier 'images'
# @app.server.route('/images/<path:path>')
# def serve_image(path):
#     return send_from_directory(os.path.join(os.getcwd(), 'images'), path)

# # Callbacks pour la navigation entre les pages
# @app.callback(
#     Output('page-content', 'children'),
#     [Input('url', 'pathname')]
# )
# def display_page(pathname):
#     if pathname == '/':
#         return home.layout  # Page d'accueil
#     elif pathname == '/about':
#         return about.layout  # Page "À propos"
#     elif pathname == '/data-analysis':
#         return data_analysis_layout  # Page d'analyse des données
#     else:
#         return "404 - Page not found"

# # Lancer le serveur Dash
# if __name__ == '__main__':
#     app.run_server(debug=True)


import os
from flask import send_from_directory
from dash import dcc, html
import dash
from dash.dependencies import Input, Output
from src.pages import home, about, simple_page
from src.pages.more_complex_page.layout import data_analysis_layout
from src.components.navbar import Navbar

# Charger Google Fonts pour une belle police
app = dash.Dash(__name__, external_stylesheets=[
    "https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap"
])
app.title = "Dashboard des Accidents de Vélo"

# Configurer le layout principal avec styles globaux
app.layout = html.Div(
    style={
        'fontFamily': 'Roboto, sans-serif',  # Appliquer la police Roboto
        'padding': '20px'                    # Espacement global
    },
    children=[
        dcc.Location(id='url', refresh=False),  # Permet de gérer les URL
        Navbar(),  # Barre de navigation
        html.Div(id='page-content')  # Contenu dynamique en fonction de la page sélectionnée
    ]
)

# Route pour servir des fichiers depuis le dossier 'images'
@app.server.route('/images/<path:path>')
def serve_image(path):
    return send_from_directory(os.path.join(os.getcwd(), 'images'), path)

# Callbacks pour la navigation entre les pages
@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    if pathname == '/':
        return home.layout  # Page d'accueil
    elif pathname == '/about':
        return about.layout  # Page "À propos"
    elif pathname == '/data-analysis':
        return data_analysis_layout  # Page d'analyse des données
    else:
        return simple_page.layout  # Page par défaut ou page non trouvée

# Lancer le serveur Dash
if __name__ == '__main__':
    app.run_server(debug=True)
