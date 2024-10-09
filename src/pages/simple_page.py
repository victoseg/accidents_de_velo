from dash import html

layout = html.Div([
    html.H2("Page Simple"),
    html.P("Ceci est une page simple contenant des informations statiques sur les accidents de vélo."),
    html.Ul([
        html.Li("Point 1: Les accidents sont plus fréquents en été."),
        html.Li("Point 2: Les grandes villes sont les plus touchées."),
        html.Li("Point 3: Les voitures sont les véhicules les plus impliqués.")
    ])
])
