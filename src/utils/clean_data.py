# import pandas as pd

# def clean_data(data):
#     """
#     Cette fonction nettoie les données en gérant les valeurs manquantes, les types mixtes et en supprimant les valeurs aberrantes.
#     :param data: DataFrame contenant les données brutes.
#     :return: DataFrame nettoyé.
#     """
    
#     # 1. Gestion des colonnes géolocalisées (lat/long)
#     data['lat'] = pd.to_numeric(data['lat'], errors='coerce')
#     data['long'] = pd.to_numeric(data['long'], errors='coerce')
    
#     # Filtrer les lignes valides avec des latitudes et longitudes correctes
#     data = data[(data['lat'].between(-90, 90)) & (data['long'].between(-180, 180))].copy()

#     # 2. Gestion des colonnes avec types mixtes pour les colonnes numériques
#     columns_to_fix = ['secuexist', 'equipement', 'obs', 'obsm', 'choc', 'manv']
#     for col in columns_to_fix:
#         data.loc[:, col] = pd.to_numeric(data[col], errors='coerce')

#     # Remplacer les valeurs manquantes par des valeurs par défaut
#     data = data.fillna({
#         'secuexist': 0,
#         'equipement': 0,
#         'obs': 0,
#         'obsm': 0,
#         'choc': 0,
#         'manv': 0
#     })
    
#     # 3. Remplacer les valeurs manquantes dans 'typevehicules' par 'inconnu'
#     data['typevehicules'] = data['typevehicules'].fillna('inconnu')

#     # 4. Supprimer les lignes où l'heure 'hrmn' est manquante
#     data = data.dropna(subset=['hrmn'])
    
#     # 5. Renommage des colonnes pour plus de clarté
#     data.rename(columns={
#         'secuexist': 'securite_existante',
#         'equipement': 'equipement',
#         'obs': 'obstacle',
#         'obsm': 'obstacle_mobile',
#         'choc': 'type_choc',
#         'manv': 'manoeuvre',
#     }, inplace=True)

#     print("Données nettoyées avec succès.")
#     return data


# import pandas as pd

# def clean_data(data):
#     """
#     Cette fonction nettoie les données en gérant les valeurs manquantes, les types mixtes et en supprimant les valeurs aberrantes.
#     :param data: DataFrame contenant les données brutes.
#     :return: DataFrame nettoyé.
#     """
    
#     # 1. Gestion des colonnes géolocalisées (lat/long)
#     #data['lat'] = pd.to_numeric(data['lat'], errors='coerce')
#     #data['long'] = pd.to_numeric(data['long'], errors='coerce')
#     data['latitude'] = pd.to_numeric(data['latitude'], errors='coerce')
#     data['longitude'] = pd.to_numeric(data['longitude'], errors='coerce')

#     # Filtrer les lignes valides avec des latitudes et longitudes correctes
#     data = data[(data['lat'].between(-90, 90)) & (data['long'].between(-180, 180))].copy()

#     # 2. Gestion des colonnes avec types mixtes pour les colonnes numériques
#     columns_to_fix = ['secuexist', 'equipement', 'obs', 'obsm', 'choc', 'manv']
    # for col in columns_to_fix:
    #     data.loc[:, col] = pd.to_numeric(data[col], errors='coerce')

    # # Remplacer les valeurs manquantes par des valeurs par défaut
    # data = data.fillna({
    #     'secuexist': 0,
    #     'equipement': 0,
    #     'obs': 0,
    #     'obsm': 0,
    #     'choc': 0,
    #     'manv': 0
    # })
    
    # # 3. Remplacer les valeurs manquantes dans 'typevehicules' par 'inconnu'
    # data['typevehicules'] = data['typevehicules'].fillna('inconnu')

    # # 4. Supprimer les lignes où l'heure 'hrmn' est manquante
    # data = data.dropna(subset=['hrmn'])
    
    # # 5. Renommage des colonnes pour plus de clarté
    # data.rename(columns={
    #     'secuexist': 'securite_existante',
    #     'equipement': 'equipement',
    #     'obs': 'obstacle',
    #     'obsm': 'obstacle_mobile',
    #     'choc': 'type_choc',
    #     'manv': 'manoeuvre',
    # }, inplace=True)

    # print("Données nettoyées avec succès.")
    # return data

# Fonction pour charger, nettoyer et sauvegarder les données
# def main():
#     # Chemin vers le fichier brut
#     raw_file_path = 'data/raw/prod-region-annuelle-enr-2.csv'
    
#     # Charger les données brutes
#     # raw_data = pd.read_csv(raw_file_path, low_memory=False)
    
#     # Nettoyer les données
# #     cleaned_data = clean_data(raw_data)
    
# #     # Sauvegarder les données nettoyées
# #     cleaned_file_path = 'data/cleaned/cleaneddata.csv'
# #     cleaned_data.to_csv(cleaned_file_path, index=False)
# #     print(f"Données nettoyées sauvegardées dans : {cleaned_file_path}")

# # # Exécuter le script si ce fichier est le programme principal
# # if __name__ == "__main__":
# #     main()
#     try:
#         # Charger les données brutes avec un délimiteur spécifique si nécessaire
#         raw_data = pd.read_csv(raw_file_path, delimiter=',', low_memory=False)  # Changez le délimiteur si nécessaire
        
#         # Nettoyer les données
#         cleaned_data = clean_data(raw_data)
        
#         # Sauvegarder les données nettoyées
#         cleaned_file_path = 'data/cleaned/cleaneddata.csv'
#         cleaned_data.to_csv(cleaned_file_path, index=False)
#         print(f"Données nettoyées sauvegardées dans : {cleaned_file_path}")

#     except pd.errors.ParserError as e:
#         print(f"Erreur lors de la lecture du fichier : {e}")

# if __name__ == "__main__":
#     main()



import pandas as pd

def clean_data(data):
    """
    Cette fonction nettoie les données en gérant les valeurs manquantes, les types mixtes et en supprimant les valeurs aberrantes.
    :param data: DataFrame contenant les données brutes.
    :return: DataFrame nettoyé.
    """
    
    # 1. Extraction des coordonnées géographiques depuis 'geo_point_region'
    data[['lat', 'long']] = data['geo_point_region'].str.split(',', expand=True).astype(float)

    # Filtrer les lignes valides avec des latitudes et longitudes correctes
    data = data[(data['lat'].between(-90, 90)) & (data['long'].between(-180, 180))].copy()

    # 2. Gestion des colonnes avec types mixtes pour les colonnes numériques
    columns_to_fix = ['production_hydraulique_renouvelable', 
                      'production_bioenergies_renouvelable', 
                      'production_eolienne_renouvelable', 
                      'production_solaire_renouvelable', 
                      'production_electrique_renouvelable', 
                      'production_gaz_renouvelable', 
                      'production_totale_renouvelable']

    for col in columns_to_fix:
        data.loc[:, col] = pd.to_numeric(data[col], errors='coerce')

    # Remplacer les valeurs manquantes par des valeurs par défaut
    data = data.fillna(0)  # On remplace toutes les valeurs manquantes par 0
    
    # 3. Supprimer les lignes où l'année 'annee' est manquante
    data = data.dropna(subset=['annee'])
    
    # 4. Renommage des colonnes pour plus de clarté
    data.rename(columns={
        'production_hydraulique_renouvelable': 'hydraulique_renouvelable',
        'production_bioenergies_renouvelable': 'bioenergies_renouvelable',
        'production_eolienne_renouvelable': 'eolienne_renouvelable',
        'production_solaire_renouvelable': 'solaire_renouvelable',
        'production_electrique_renouvelable': 'electrique_renouvelable',
        'production_gaz_renouvelable': 'gaz_renouvelable',
        'production_totale_renouvelable': 'totale_renouvelable',
    }, inplace=True)

    print("Données nettoyées avec succès.")
    return data

def main():
    # Chemin vers le fichier brut
    raw_file_path = 'data/raw/prod-region-annuelle-enr-2.csv'
    
    try:
        # Lire le fichier tout en ignorant les lignes malformées
        raw_data = pd.read_csv(raw_file_path, delimiter=';', on_bad_lines='skip')
        
        # Afficher les noms des colonnes pour vérification
        print("Noms des colonnes :")
        print(raw_data.columns.tolist())
        
        # Nettoyer les données
        cleaned_data = clean_data(raw_data)
        
        # Sauvegarder les données nettoyées
        cleaned_file_path = 'data/cleaned/cleaneddata.csv'
        cleaned_data.to_csv(cleaned_file_path, index=False)
        print(f"Données nettoyées sauvegardées dans : {cleaned_file_path}")

    except pd.errors.ParserError as e:
        print(f"Erreur lors de la lecture du fichier : {e}")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

if __name__ == "__main__":
    main()