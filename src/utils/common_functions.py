def format_number(number):
    """Formate un nombre avec des séparateurs de milliers."""
    return f"{number:,}".replace(",", " ")

def generate_title(title):
    """Génère un titre formaté pour les sections du dashboard."""
    return title.upper()
