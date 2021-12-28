from log_config import logging

club_names = ['Monaco', 'Clermont', 'Lorient', 'Reims', 'Strasbourg', 'Bordeaux', 'Angers', 'Metz', 'St-Étienne', 'Lyon', 'Montpellier',
         'Rennes', 'LOSC', 'Paris', 'Troyes', 'Brest', 'Nantes', 'Nice','Lens', 'Marseille']

columns = ['pm', 'w', 'd', 'l', 'pts', 'gs', 'gc', 'gd']

clubs = []
for i in club_names:
    d = {"name":i}
    for column in columns:
        d[column] = 0
        d["last_5"] = ['-','-','-','-','-']
    clubs.append(d)

for club in clubs:
    if not (isinstance(club["pts"], int)):
        raise TypeError("Expected int input")

fifa_names = ['AS Monaco', 'Clermont Foot 63', 'FC Lorient', 'Stade de Reims', 'RC Strasbourg Alsace', 'FC Girondins de Bordeaux',
              'Angers SCO', 'FC Metz', 'AS Saint-Étienne', 'Olympique Lyonnais', 'Montpellier Hérault SC', 'Stade Rennais FC', 'LOSC Lille',
              'Paris Saint-Germain', 'ESTAC Troyes', 'Stade Brestois 29', 'FC Nantes', 'OGC Nice', 'Racing Club de Lens', 'Olympique de Marseille']

clubs_to_fifa = {}
for club in clubs:
    clubs_to_fifa[club["name"]] = fifa_names[club_names.index(club["name"])]

fifa_to_clubs = {}
for team in fifa_names:
    fifa_to_clubs[team] = club_names[fifa_names.index(team)]

logging.info(clubs_to_fifa)
logging.info(fifa_to_clubs)