import pandas as pd

def load_data(file_path):
    """
    Cette fonction charge les données brutes depuis un fichier CSV.
    :param file_path: Chemin vers le fichier CSV à charger.
    :return: DataFrame pandas contenant les données brutes.
    """
    try:
        data = pd.read_csv(file_path, low_memory=False)  # Ajout de low_memory=False
        print("Données brutes chargées avec succès.")
        return data
    except FileNotFoundError:
        print("Le fichier n'a pas été trouvé.")
        return None

file_path = 'data/raw/prod-region-annuelle-enr-2.csv'  # Chemin vers le nouveau fichier
data = load_data(file_path)