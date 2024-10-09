from dash import html

layout = html.Div(
    style={
        'fontFamily': 'Roboto, sans-serif',  # Applique la police Roboto
        'backgroundImage': 'url("/images/Fond.png")',  # Image d'arrière-plan
        'backgroundSize': 'cover',  # L'image couvre toute la page
        'backgroundPosition': 'center',  # Centre l'image
        'height': '100vh',  # Prend toute la hauteur de la fenêtre
        'display': 'flex',  # Utilise flexbox pour centrer le contenu
        'flexDirection': 'column',  # Aligne verticalement le contenu
        'justifyContent': 'center',  # Centre le contenu verticalement
        'alignItems': 'center',  # Centre le contenu horizontalement
        'textAlign': 'center',  # Centrer le texte
        'color': 'white',  # Texte en blanc pour contraste
        'padding': '20px'  # Espacement interne
    },
    children=[
        html.H1(
            "Bienvenue sur le Dashboard des énergies renouvelables",
            style={
                'fontSize': '3rem',
                'fontWeight': '700',  # Texte en gras
                'letterSpacing': '0.05em',  # Espacement entre les lettres
                'textAlign': 'center'  # Centrage du texte
            }
        ),
        html.P(
            "Ce dashboard présente les données d'énergies renouvelables en France",
            style={
                'fontSize': '1.5rem',
                'lineHeight': '1.6',  # Espacement entre les lignes
                'letterSpacing': '0.05em',  # Espacement entre les lettres
                'textAlign': 'center',  # Centrage du texte
                'maxWidth': '800px',  # Limite la largeur du texte pour une meilleure lisibilité
            }
        )
    ]
)
