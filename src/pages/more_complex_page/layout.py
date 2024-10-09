# from dash import dcc, html
# import plotly.express as px
# import pandas as pd

# # Charger les données nettoyées
# #data = pd.read_csv('data/cleaned/cleaneddata.csv', low_memory=False)
# data = pd.read_csv('data/cleaned/cleaneddata.csv', low_memory=False)
# # Histogramme de répartition des accidents par mois
# fig_histogram = px.histogram(
#     data,
#     x="annee",  # Use 'annee' or another relevant column
#     title="Répartition des accidents par année",
#     labels={'annee': 'Année'},
#     nbins=12,
#     color_discrete_sequence=["#636EFA"]
# )

# fig_histogram.update_layout(
#     xaxis_title="Année",
#     yaxis_title="Nombre d'accidents",
#     bargap=0.2
# )

# # Carte géolocalisée des accidents
# fig_map = px.scatter_mapbox(
#     data, 
#     lat="lat", 
#     lon="long", 
#     hover_name="nom_insee_region",
#     title="Carte des accidents de vélo en France",
#     mapbox_style="open-street-map",
#     zoom=5,
#     height=600
# )
# fig_map.update_layout(
#     mapbox=dict(
#         center={"lat": 46.603354, "lon": 1.888334},  # Centré sur la France
#         zoom=5,
#     ),
#     margin={"r": 0, "t": 50, "l": 0, "b": 0}
# )

# # Layout de la page d'analyse des données
# data_analysis_layout = html.Div([  # Renommez le layout pour faciliter l'import
#     html.H2("Analyse des données d'accidents de vélo"),
    
#     # Affichage de l'histogramme
#     dcc.Graph(
#         id='histogram',
#         figure=fig_histogram
#     ),
    
#     # Affichage de la carte géolocalisée
#     dcc.Graph(
#         id='map',
#         figure=fig_map
#     )
# ])


# from dash import dcc, html
# from dash.dependencies import Input, Output
# import plotly.express as px
# import pandas as pd
# from main import app

# # Charger les données nettoyées
# data = pd.read_csv('data/cleaned/cleaneddata.csv', low_memory=False)

# # Récupérer les options uniques pour le type d'accident
# types_accidents = data['typevehicules'].unique()

# # Récupérer les options uniques pour les régions (départements ici)
# regions = data['dep'].unique()

# # Layout de la page d'analyse des données avec filtres dynamiques et option "Tous"
# layout = html.Div([
#     html.H2("Analyse des données d'accidents de vélo", style={'textAlign': 'center'}),

#     # Dropdown pour filtrer par type d'accident, avec option "Tous les types"
#     dcc.Dropdown(
#         id='type-dropdown',
#         options=[{'label': 'Tous les types', 'value': 'all'}] + [{'label': typ, 'value': typ} for typ in types_accidents],
#         value='all',  # Valeur par défaut = "Tous"
#         clearable=False,
#         style={'width': '50%', 'margin': 'auto'}
#     ),

#     # Slider pour filtrer par date (ici je suppose qu'il y a une colonne 'date')
#     dcc.Slider(
#         id='date-slider',
#         min=data['date'].min(),
#         max=data['date'].max(),
#         value=data['date'].max(),
#         marks={str(date): str(date) for date in sorted(data['date'].unique())},
#         step=None,
#         tooltip={"placement": "bottom", "always_visible": True},
#         style={'width': '80%', 'margin': '50px auto'}
#     ),

#     # Boutons radio pour sélectionner une région, avec option "Toutes les régions"
#     dcc.RadioItems(
#         id='region-radio',
#         options=[{'label': 'Toutes les régions', 'value': 'all'}] + [{'label': region, 'value': region} for region in regions],
#         value='all',  # Valeur par défaut = "Toutes les régions"
#         labelStyle={'display': 'inline-block', 'margin-right': '20px'},
#         style={'textAlign': 'center', 'marginBottom': '20px'}
#     ),

#     # Affichage de l'histogramme (qui sera mis à jour en fonction des filtres)
#     dcc.Graph(id='filtered-histogram'),

#     # Affichage de la carte géolocalisée (qui sera mise à jour en fonction des filtres)
#     dcc.Graph(id='filtered-map')
# ])

# # Callback pour mettre à jour les graphiques en fonction des filtres sélectionnés
# @app.callback(
#     [Output('filtered-histogram', 'figure'),
#      Output('filtered-map', 'figure')],
#     [Input('type-dropdown', 'value'),
#      Input('date-slider', 'value'),
#      Input('region-radio', 'value')]
# )
# def update_graphs(selected_type, selected_date, selected_region):
#     # Commencer avec toutes les données
#     filtered_data = data.copy()

#     # Filtrer les données en fonction des entrées
#     if selected_type != 'all':
#         filtered_data = filtered_data[filtered_data['typevehicules'] == selected_type]

#     if selected_date is not None:
#         filtered_data = filtered_data[filtered_data['date'] == selected_date]

#     if selected_region != 'all':
#         filtered_data = filtered_data[filtered_data['dep'] == selected_region]

#     # Histogramme de répartition des accidents par mois
#     fig_histogram = px.histogram(
#         filtered_data,
#         x="mois",
#         title="Répartition des accidents par mois",
#         labels={'mois': 'Mois'},
#         nbins=12,
#         color_discrete_sequence=["#636EFA"]
#     )
#     fig_histogram.update_layout(
#         xaxis_title="Mois",
#         yaxis_title="Nombre d'accidents",
#         bargap=0.2
#     )

#     # Carte géolocalisée des accidents
#     fig_map = px.scatter_mapbox(
#         filtered_data,
#         lat="lat",
#         lon="long",
#         hover_name="dep",
#         title="Carte des accidents de vélo en France",
#         mapbox_style="open-street-map",
#         zoom=5,
#         height=600
#     )
#     fig_map.update_layout(
#         mapbox=dict(
#             center={"lat": 46.603354, "lon": 1.888334},
#             zoom=5,
#         ),
#         margin={"r": 0, "t": 50, "l": 0, "b": 0}
#     )

#     return fig_histogram, fig_map

# src/pages/more_complex_page/layout.py


# 


# from dash import dcc, html
# import plotly.express as px
# import pandas as pd
# from app import app  # Assurez-vous que cela est bien importé depuis le bon module
# from dash.dependencies import Input, Output  # Import des dépendances nécessaires

# # Charger les données nettoyées
# data = pd.read_csv('data/cleaned/cleaneddata.csv', low_memory=False)

# # Créer les graphiques avec les données filtrées
# def create_figures(data):
#     fig_histogram = px.histogram(
#         data,
#         x="mois",
#         title="Répartition des accidents par mois",
#         labels={'mois': 'Mois'},
#         nbins=12,
#         color_discrete_sequence=["#636EFA"]
#     )
#     fig_histogram.update_layout(
#         xaxis_title="Mois",
#         yaxis_title="Nombre d'accidents",
#         bargap=0.2
#     )

#     fig_map = px.scatter_mapbox(
#         data,
#         lat="lat",
#         lon="long",
#         hover_name="dep",
#         title="Carte des accidents de vélo en France",
#         mapbox_style="open-street-map",
#         zoom=5,
#         height=600
#     )
#     fig_map.update_layout(
#         mapbox=dict(
#             center={"lat": 46.603354, "lon": 1.888334},  # Centré sur la France
#             zoom=5,
#         ),
#         margin={"r": 0, "t": 50, "l": 0, "b": 0}
#     )

#     return fig_histogram, fig_map

# # Layout de la page d'analyse des données
# data_analysis_layout = html.Div([
#     html.H2("Analyse des données d'accidents de vélo"),
    
#     # Filtres dynamiques
#     html.Div([
#         dcc.Dropdown(
#             id='month-filter',
#             options=[
#                 {'label': str(i), 'value': i} for i in range(1, 13)
#             ],
#             value=[1],  # Valeur par défaut (liste pour multi)
#             multi=True,
#             placeholder="Sélectionnez le(s) mois"
#         ),
#     ], style={'marginBottom': '20px'}),

#     dcc.Graph(
#         id='histogram',
#         figure=create_figures(data)[0]  # Histogramme
#     ),
#     dcc.Graph(
#         id='map',
#         figure=create_figures(data)[1]  # Carte géolocalisée
#     )
# ])

# # Callback pour mettre à jour les graphiques en fonction des filtres
# @app.callback(
#     [Output('histogram', 'figure'),
#      Output('map', 'figure')],
#     [Input('month-filter', 'value')]
# )
# def update_graphs(selected_months):
#     filtered_data = data[data['mois'].isin(selected_months)] if selected_months else data
#     return create_figures(filtered_data)





#MARCHE
# import pandas as pd
# from dash import dcc, html
# import plotly.express as px

# # Charger les données nettoyées
# data = pd.read_csv('data/cleaned/cleaneddata.csv', low_memory=False)

# # Vérifier les noms des colonnes
# print("Noms des colonnes :", data.columns.tolist())

# # Calculer la production totale par région
# data['production_totale'] = (
#     data['hydraulique_renouvelable'] +
#     data['bioenergies_renouvelable'] +
#     data['eolienne_renouvelable'] +
#     data['solaire_renouvelable'] +
#     data['electrique_renouvelable'] +
#     data['gaz_renouvelable']
# )

# # Créer un histogramme de la production totale d'énergie renouvelable
# fig_histogram = px.histogram(
#     data,
#     x='production_totale',  # Valeurs à afficher sur l'axe X
#     title='Distribution de la production d\'énergie renouvelable par code INSEE',
#     labels={'production_totale': 'Production d\'énergie renouvelable'},
#     nbins=20  # Nombre de bins pour l'histogramme
# )

# fig_histogram.update_layout(
#     xaxis_title="Production d'énergie renouvelable",
#     yaxis_title="Nombre de régions",
#     bargap=0.2
# )

# # Créer la carte géolocalisée des régions
# fig_map = px.scatter_mapbox(
#     data,
#     lat="lat",
#     lon="long",
#     hover_name="geo_shape_region",  # Afficher le nom de la région
#     title="Carte de la production d'énergie renouvelable en France",
#     mapbox_style="open-street-map",
#     zoom=5,
#     height=600
# )

# fig_map.update_layout(
#     mapbox=dict(
#         center={"lat": 46.603354, "lon": 1.888334},  # Centré sur la France
#         zoom=5,
#     ),
#     margin={"r": 0, "t": 50, "l": 0, "b": 0}
# )

# # Layout de la page d'analyse des données
# data_analysis_layout = html.Div([
#     html.H2("Analyse des données d'accidents de vélo"),
#     dcc.Graph(
#         id='histogram',
#         figure=fig_histogram
#     ),
#     dcc.Graph(
#         id='map',
#         figure=fig_map
#     )
# ])


# import pandas as pd
# from dash import dcc, html
# import plotly.express as px

# # Charger les données nettoyées
# data = pd.read_csv('data/cleaned/cleaneddata.csv', low_memory=False)

# # Vérifier les noms des colonnes
# print("Noms des colonnes :", data.columns.tolist())

# # Créer un histogramme de la production totale d'énergie renouvelable
# data['production_totale'] = (
#     data['hydraulique_renouvelable'] +
#     data['bioenergies_renouvelable'] +
#     data['eolienne_renouvelable'] +
#     data['solaire_renouvelable'] +
#     data['electrique_renouvelable'] +
#     data['gaz_renouvelable']
# )

# # Créer un histogramme de la production totale d'énergie renouvelable
# fig_histogram = px.histogram(
#     data,
#     x='production_totale',  # Valeurs à afficher sur l'axe X
#     title='Distribution de la production d\'énergie renouvelable par code INSEE',
#     labels={'production_totale': 'Production d\'énergie renouvelable'},
#     nbins=20  # Nombre de bins pour l'histogramme
# )

# fig_histogram.update_layout(
#     xaxis_title="Production d'énergie renouvelable",
#     yaxis_title="Nombre de régions",
#     bargap=0.2
# )

# # Créer la carte géolocalisée des régions avec différentes couleurs pour chaque type d'énergie
# fig_map = px.scatter_mapbox(
#     data,
#     lat="lat",
#     lon="long",
#     hover_name="nom_insee_region",  # Afficher le nom de la région
#     title="Carte de la production d'énergie renouvelable en France",
#     color="production_totale",  # Colonne à utiliser pour les couleurs
#     mapbox_style="open-street-map",
#     zoom=5,
#     height=600
# )

# # Utiliser une échelle de couleurs pour les types d'énergies renouvelables
# fig_map.update_traces(marker=dict(size=10, opacity=0.7))

# fig_map.update_layout(
#     mapbox=dict(
#         center={"lat": 46.603354, "lon": 1.888334},  # Centré sur la France
#         zoom=5,
#     ),
#     margin={"r": 0, "t": 50, "l": 0, "b": 0}
# )

# # Layout de la page d'analyse des données
# data_analysis_layout = html.Div([
#     html.H2("Analyse des données d'accidents de vélo"),
#     dcc.Graph(
#         id='histogram',
#         figure=fig_histogram
#     ),
#     dcc.Graph(
#         id='map',
#         figure=fig_map
#     )
# ])


#carte et histogramme simple

# import dash
# from dash import dcc, html
# import folium
# from dash.dependencies import Input, Output
# import pandas as pd
# import plotly.express as px
# import os
# from flask import send_from_directory

# # Charger les données nettoyées
# df_cleaned = pd.read_csv('data/cleaned/cleaneddata.csv')

# # Créer une nouvelle colonne pour la production totale d'énergie renouvelable
# df_cleaned['production_totale'] = (
#     df_cleaned['hydraulique_renouvelable'] +
#     df_cleaned['bioenergies_renouvelable'] +
#     df_cleaned['eolienne_renouvelable'] +
#     df_cleaned['solaire_renouvelable'] +
#     df_cleaned['electrique_renouvelable'] +
#     df_cleaned['gaz_renouvelable']
# )

# # Créer un histogramme de la production totale d'énergie renouvelable
# fig_histogram = px.histogram(
#     df_cleaned,
#     x='production_totale',
#     title='Distribution de la production d\'énergie renouvelable par région',
#     labels={'production_totale': 'Production d\'énergie renouvelable (GWh)'},
#     nbins=20
# )

# fig_histogram.update_layout(
#     xaxis_title="Production d'énergie renouvelable (GWh)",
#     yaxis_title="Nombre de régions",
#     bargap=0.2,
#     title={'x': 0.5}  # Centrer le titre
# )

# # Créer une carte interactive avec Plotly
# fig_map = px.scatter_mapbox(
#     df_cleaned,
#     lat="lat",
#     lon="long",
#     hover_name="nom_insee_region",
#     title="Carte de la production d'énergie renouvelable en France",
#     color="production_totale",
#     mapbox_style="open-street-map",
#     zoom=5,
#     height=600
# )

# fig_map.update_traces(marker=dict(size=10, opacity=0.7))
# fig_map.update_layout(
#     mapbox=dict(
#         center={"lat": 46.603354, "lon": 1.888334},
#         zoom=5,
#     ),
#     margin={"r": 0, "t": 50, "l": 0, "b": 0}
# )

# # Route pour servir les fichiers depuis src/components
# app = dash.Dash(__name__, external_stylesheets=[
#     "https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap"
# ])

# @app.server.route('/components/<path:path>')
# def serve_static_files(path):
#     return send_from_directory(os.path.join(os.getcwd(), 'src/components'), path)

# # Fonction pour créer la carte avec Folium
# def create_map():
#     map_france_renouvelable = folium.Map(location=[46.603354, 1.888334], zoom_start=6)

#     couleurs = {
#         'Solaire': 'yellow',
#         'Éolienne': 'blue',
#         'Hydraulique': 'green',
#         'Bioénergies': 'brown'
#     }

#     for i, row in df_cleaned.iterrows():
#         total_renouvelable = row['production_totale']
        
#         energie_dominante = max(
#             row['solaire_renouvelable'],
#             row['eolienne_renouvelable'],
#             row['hydraulique_renouvelable'],
#             row['bioenergies_renouvelable'],
#             key=lambda x: x if x > 0 else 0
#         )
#         energie_dominante_type = 'Solaire' if energie_dominante == row['solaire_renouvelable'] else (
#             'Éolienne' if energie_dominante == row['eolienne_renouvelable'] else (
#                 'Hydraulique' if energie_dominante == row['hydraulique_renouvelable'] else 'Bioénergies'
#             )
#         )

#         folium.CircleMarker(
#             location=[row['lat'], row['long']],
#             radius=5 + (total_renouvelable / 1000),
#             color=couleurs[energie_dominante_type],
#             fill=True,
#             fill_color=couleurs[energie_dominante_type],
#             fill_opacity=0.6,
#             popup=f"{row['nom_insee_region']} - {total_renouvelable} GWh"
#         ).add_to(map_france_renouvelable)

#     if not os.path.exists('src/components'):
#         os.makedirs('src/components')
#     map_france_renouvelable.save('src/components/map_energie.html')

# # Appeler la fonction pour générer la carte au lancement
# create_map()

# # Layout principal
# app.layout = html.Div(
#     style={'fontFamily': 'Roboto, sans-serif', 'padding': '20px'},
#     children=[
#         dcc.Location(id='url', refresh=False),
#         html.Nav([
#             dcc.Link('Accueil', href='/'),
#             " | ",
#             dcc.Link('Analyse des données', href='/data-analysis'),
#             " | ",
#             dcc.Link('À propos', href='/about')
#         ], style={'padding': '10px', 'font-size': '18px'}),  # Améliorer la barre de navigation
#         html.Div(id='page-content')  # Contenu dynamique en fonction de la page
#     ]
# )

# # Layout pour la page d'accueil avec l'image de fond et le titre
# home_layout = html.Div(
#     style={
#         'fontFamily': 'Roboto, sans-serif',  # Applique la police Roboto
#         'backgroundImage': 'url("/images/Fond.png")',  # Image d'arrière-plan
#         'backgroundSize': 'cover',  # L'image couvre toute la page
#         'backgroundPosition': 'center',  # Centre l'image
#         'height': '100vh',  # Prend toute la hauteur de la fenêtre
#         'display': 'flex',  # Utilise flexbox pour centrer le contenu
#         'flexDirection': 'column',  # Aligne verticalement le contenu
#         'justifyContent': 'center',  # Centre le contenu verticalement
#         'alignItems': 'center',  # Centre le contenu horizontalement
#         'textAlign': 'center',  # Centrer le texte
#         'color': 'white',  # Texte en blanc pour contraste
#         'padding': '20px'  # Espacement interne
#     },
#     children=[
#         html.H1("Bienvenue sur le Dashboard des Énergies Renouvelables", style={'fontSize': '48px'})
#     ]
# )

# # Layout pour la page d'analyse des données
# data_analysis_layout = html.Div([
#     html.H2("Analyse des données d'énergie renouvelable"),
#     dcc.Graph(id='histogram', figure=fig_histogram),
#     dcc.Graph(id='map', figure=fig_map)
# ])

# # Callbacks pour afficher les pages en fonction de l'URL
# @app.callback(
#     Output('page-content', 'children'),
#     [Input('url', 'pathname')]
# )
# def display_page(pathname):
#     if pathname == '/':
#         return home_layout
#     elif pathname == '/data-analysis':
#         return data_analysis_layout
#     else:
#         return html.Div([html.H1("404"), html.P("Page non trouvée")])

# # Lancer le serveur
# if __name__ == '__main__':
#     app.run_server(debug=True)


import dash
from dash import dcc, html
import folium
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import os
from flask import send_from_directory

# Charger les données nettoyées
df_cleaned = pd.read_csv('data/cleaned/cleaneddata.csv')

# Filtrer les données pour l'année 2008 et 2023
df_2008 = df_cleaned[df_cleaned['annee'] == 2008]
df_2023 = df_cleaned[df_cleaned['annee'] == 2023]

# Créer l'histogramme pour 2008
fig_histogram_2008 = px.histogram(
    df_2008,
    x='totale_renouvelable',
    title="Production d'énergie renouvelable par région en 2008",
    labels={'totale_renouvelable': 'Production d\'énergie renouvelable (GWh)'},
    nbins=20
)

fig_histogram_2008.update_layout(
    xaxis_title="Production d'énergie renouvelable (GWh)",
    yaxis_title="Nombre de régions",
    bargap=0.2
)

# Créer l'histogramme pour 2023
fig_histogram_2023 = px.histogram(
    df_2023,
    x='totale_renouvelable',
    title="Production d'énergie renouvelable par région en 2023",
    labels={'totale_renouvelable': 'Production d\'énergie renouvelable (GWh)'},
    nbins=20
)

fig_histogram_2023.update_layout(
    xaxis_title="Production d'énergie renouvelable (GWh)",
    yaxis_title="Nombre de régions",
    bargap=0.2
)

# Créer la carte pour 2008
fig_map_2008 = px.scatter_mapbox(
    df_2008,
    lat="lat",
    lon="long",
    hover_name="nom_insee_region",
    title="Carte de la production d'énergie renouvelable en 2008",
    color="totale_renouvelable",  # Colonne à utiliser pour les couleurs
    mapbox_style="open-street-map",
    zoom=5,
    height=600
)

fig_map_2008.update_traces(marker=dict(size=10, opacity=0.7))
fig_map_2008.update_layout(
    mapbox=dict(
        center={"lat": 46.603354, "lon": 1.888334},  # Centré sur la France
        zoom=5,
    ),
    margin={"r": 0, "t": 50, "l": 0, "b": 0}
)

# Créer la carte pour 2023
fig_map_2023 = px.scatter_mapbox(
    df_2023,
    lat="lat",
    lon="long",
    hover_name="nom_insee_region",
    title="Carte de la production d'énergie renouvelable en 2023",
    color="totale_renouvelable",  # Colonne à utiliser pour les couleurs
    mapbox_style="open-street-map",
    zoom=5,
    height=600
)

fig_map_2023.update_traces(marker=dict(size=10, opacity=0.7))
fig_map_2023.update_layout(
    mapbox=dict(
        center={"lat": 46.603354, "lon": 1.888334},  # Centré sur la France
        zoom=5,
    ),
    margin={"r": 0, "t": 50, "l": 0, "b": 0}
)

# Layout principal pour le dashboard
app = dash.Dash(__name__, external_stylesheets=[
    "https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap"
])

# Layout pour la page d'accueil avec l'image de fond et le titre
home_layout = html.Div(
    style={
        'backgroundImage': 'url("/images/Fond.png")',  # Chemin vers l'image de fond
        'backgroundSize': 'cover',  # L'image couvre tout l'écran
        'height': '100vh',  # L'image couvre toute la hauteur de la page
        'display': 'flex',
        'alignItems': 'center',
        'justifyContent': 'center',
        'color': 'white',  # Couleur du texte pour bien le voir sur l'image
        'textAlign': 'center'
    },
    children=[
        html.H1("Bienvenue sur le Dashboard des Énergies Renouvelables", style={'fontSize': '48px'})
    ]
)

# Layout pour la page d'analyse des données avec les deux histogrammes et les deux cartes
data_analysis_layout = html.Div([
    html.H2("Analyse des données d'énergie renouvelable"),
    
    # Cartes pour 2008 et 2023
    html.Div([
        html.H3("2008 - Carte de la production"),
        dcc.Graph(id='map_2008', figure=fig_map_2008),
    ]),
    html.Div([
        html.H3("2023 - Carte de la production"),
        dcc.Graph(id='map_2023', figure=fig_map_2023),
    ]),
    
    # Histogrammes pour 2008 et 2023
    html.Div([
        html.H3("2008 - Histogramme"),
        dcc.Graph(id='histogram_2008', figure=fig_histogram_2008),
    ]),
    html.Div([
        html.H3("2023 - Histogramme"),
        dcc.Graph(id='histogram_2023', figure=fig_histogram_2023),
    ])
])

# Callback pour afficher la page Analyse des données
@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    if pathname == '/':
        return home_layout
    elif pathname == '/data-analysis':
        return data_analysis_layout  # Afficher les deux cartes et les histogrammes ici
    else:
        return html.Div([html.H1("404"), html.P("Page non trouvée")])

# Layout principal pour le routing
app.layout = html.Div(
    style={'fontFamily': 'Roboto, sans-serif', 'padding': '20px'},
    children=[
        dcc.Location(id='url', refresh=False),
        html.Nav([
            dcc.Link('Accueil', href='/'),
            " | ",
            dcc.Link('Analyse des données', href='/data-analysis'),
            " | ",
            dcc.Link('À propos', href='/about')
        ], style={'padding': '10px', 'font-size': '18px'}),  # Barre de navigation
        html.Div(id='page-content')  # Contenu dynamique en fonction de la page
    ]
)

# Lancer le serveur
if __name__ == '__main__':
    app.run_server(debug=True)
