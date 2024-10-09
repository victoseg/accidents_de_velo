from dash import html

def Navbar():
    return html.Nav(
        style={
            'position': 'fixed',        # Rend la barre de navigation fixe
            'top': '0',                 # Fixe la barre en haut de la page
            'width': '100%',            # Prend toute la largeur de la fenêtre
            'zIndex': '1000',           # Assure que la barre est au-dessus du contenu
            'backgroundColor': '#f8f9fa',  # Couleur de fond (modifiable)
            'display': 'flex',          # Utiliser flexbox pour aligner les éléments horizontalement
            'justifyContent': 'center',  # Centrer les liens
            'padding': '10px 0',        # Espacement vertical (haut/bas)
            'boxShadow': '0 2px 5px rgba(0, 0, 0, 0.1)'  # Ajoute une légère ombre pour un effet visuel agréable
        },
        children=[
            html.A(
                "Accueil",
                href="/",
                style={
                    'textDecoration': 'none',  # Supprimer le soulignement
                    'margin': '0 15px',        # Espacement entre les éléments
                    'color': 'black',           # Couleur noire pour les liens
                    'fontSize': '1.2rem',       # Taille du texte
                    'fontWeight': 'bold'        # Mettre en gras
                }
            ),
            html.A(
                "Analyse des données",
                href="/data-analysis",  # Corrigé pour correspondre à votre routage
                style={
                    'textDecoration': 'none',  # Supprimer le soulignement
                    'margin': '0 15px',        # Espacement entre les éléments
                    'color': 'black',           # Couleur noire pour les liens
                    'fontSize': '1.2rem',       # Taille du texte
                    'fontWeight': 'bold'        # Mettre en gras
                }
            ),
            html.A(
                "À propos de CycleSafe",
                href="/about",  # Corrigé pour correspondre à votre routage
                style={
                    'textDecoration': 'none',  # Supprimer le soulignement
                    'margin': '0 15px',        # Espacement entre les éléments
                    'color': 'black',           # Couleur noire pour les liens
                    'fontSize': '1.2rem',       # Taille du texte
                    'fontWeight': 'bold'        # Mettre en gras
                }
            )
        ]
    )
