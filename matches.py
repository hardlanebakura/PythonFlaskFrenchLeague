from log_config import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
#from mongo_collections import Database
from m import DatabaseAtlas
from match import Match
from clubs import club_names, clubs, fifa_names
from operator import itemgetter
import itertools
import difflib
from teams_info import teams_info

URL_8 = "https://www.uefa.com/memberassociations/fra/domesticleague/#/mt/2021/08"
URL_9 = "https://www.uefa.com/memberassociations/fra/domesticleague/#/mt/2021/09"
URL_10 = "https://www.uefa.com/memberassociations/fra/domesticleague/#/mt/2021/10"
URL_11 = "https://www.uefa.com/memberassociations/fra/domesticleague/#/mt/2021/11"
URL_12 = "https://www.uefa.com/memberassociations/fra/domesticleague/#/mt/2021/12"

def get_matches(matches_number):
    for i in range(1, matches_number):
        home_team = '//*[@id="calendar-container"]/div/div[{}]/div/div[2]/div[3]/div/div/span'.format(i)
        home_team_element = driver.find_element(By.XPATH, home_team).get_attribute("innerHTML")
        home_team_element = home_team_element.strip()
        home_team_goals = '// *[ @ id = "calendar-container"] / div / div[{}] / div / div[2] / div[4] / div / span[1]'.format(i)
        home_team_goals_element = driver.find_element(By.XPATH, home_team_goals).get_attribute("innerHTML")
        away_team_goals = '// *[ @ id = "calendar-container"] / div / div[{}] / div / div[2] / div[4] / div / span[2]'.format(i)
        away_team_goals_element = driver.find_element(By.XPATH, away_team_goals).get_attribute("innerHTML")
        away_team = '//*[@id="calendar-container"]/div/div[{}]/div/div[2]/div[5]/div/div/span'.format(i)
        away_team_element = driver.find_element(By.XPATH, away_team).get_attribute("innerHTML")
        away_team_element = away_team_element.strip()
        if home_team_goals_element != "":
            Match1 = Match({"home_team":home_team_element, "home_team_goals":int(home_team_goals_element), "away_team_goals":int(away_team_goals_element)
                               , "away_team":away_team_element})
            DatabaseAtlas.insertOne("french_league_1", Match1.__dict__)
            logging.debug(Match1)

MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
matches = {"August":40, "September":41, "October":41, "November":31, "December":41}

# driver = webdriver.Chrome("chromedriver_2.exe")
# for match in matches:
#     driver.get("URL_{}".format(selected_index)
#     get_matches(matches[match])
#     driver.quit()

matches = [item for item in DatabaseAtlas.findAll("french_league_1", {})]

def home_team_won(item, home_index, away_index):
    clubs[home_index]["pm"] += 1
    clubs[home_index]["last_5"].insert(0, "w")
    clubs[home_index]["last_5"].pop()
    clubs[home_index]["w"] += 1
    clubs[home_index]["pts"] += 3
    clubs[home_index]["gs"] += item["home_team_goals"]
    clubs[home_index]["gc"] += item["away_team_goals"]
    clubs[home_index]["gd"] += item["home_team_goals"] - item["away_team_goals"]

    clubs[away_index]["pm"] += 1
    clubs[away_index]["last_5"].insert(0, "l")
    clubs[away_index]["last_5"].pop()
    clubs[away_index]["l"] += 1
    clubs[away_index]["gs"] += item["away_team_goals"]
    clubs[away_index]["gc"] += item["home_team_goals"]
    clubs[away_index]["gd"] += item["away_team_goals"] - item["home_team_goals"]

def draw(item, home_index, away_index):
    clubs[home_index]["pm"] += 1
    clubs[home_index]["last_5"].insert(0, "d")
    clubs[home_index]["last_5"].pop()
    clubs[home_index]["d"] += 1
    clubs[home_index]["pts"] += 1
    clubs[home_index]["gs"] += item["away_team_goals"]
    clubs[home_index]["gc"] += item["away_team_goals"]

    clubs[away_index]["pm"] += 1
    clubs[away_index]["last_5"].insert(0, "d")
    clubs[away_index]["last_5"].pop()
    clubs[away_index]["d"] += 1
    clubs[away_index]["pts"] += 1
    clubs[away_index]["gs"] += item["away_team_goals"]
    clubs[away_index]["gc"] += item["home_team_goals"]

def away_team_won(item, home_index, away_index):
    clubs[home_index]["pm"] += 1
    clubs[home_index]["last_5"].insert(0, "l")
    clubs[home_index]["last_5"].pop()
    clubs[home_index]["l"] += 1
    clubs[home_index]["gs"] += item["home_team_goals"]
    clubs[home_index]["gc"] += item["away_team_goals"]
    clubs[home_index]["gd"] += item["home_team_goals"] - item["away_team_goals"]

    clubs[away_index]["pm"] += 1
    clubs[away_index]["last_5"].insert(0, "w")
    clubs[away_index]["last_5"].pop()
    clubs[away_index]["w"] += 1
    clubs[away_index]["pts"] += 3
    clubs[away_index]["gs"] += item["away_team_goals"]
    clubs[away_index]["gc"] += item["home_team_goals"]
    clubs[away_index]["gd"] += item["away_team_goals"] - item["home_team_goals"]

def process_all_matches():
    for item in matches:
        #logging.debug(item)
        for club in clubs:
            if club["name"] == item["home_team"]:
                home_index = clubs.index(club)
            if club["name"] == item["away_team"]:
                away_index = clubs.index(club)
        if item["home_team_goals"] > item["away_team_goals"]:
            home_team_won(item, home_index, away_index)
        elif item["home_team_goals"] == item["away_team_goals"]:
            draw(item, home_index, away_index)
        else:
            away_team_won(item, home_index, away_index)

matches_length = int(len(matches)/2)
matches = matches[:matches_length]
process_all_matches()
clubs_sorted = sorted(clubs, key=itemgetter('pts'), reverse=True)
rank = itertools.count()
for club in clubs_sorted:
    club["rank"] = next(rank) + 1

def get_latest_team_match(team):
    matches_for_team = []
    team = clubs[fifa_names.index(team)]["name"]
    for match in matches:
        if match["home_team"] == team or match["away_team"] == team:
            matches_for_team.append(match)
    return matches_for_team[-1]

def get_next_match_for_team(team):
    for match in DatabaseAtlas.findAll("french_ligue_1_upcoming_matches", {}):

        home_team = match["homeTeam"]["name"]
        away_team = match["awayTeam"]["name"]

        home_team_1 = difflib.get_close_matches(home_team, fifa_names)
        away_team_1 = difflib.get_close_matches(away_team, fifa_names)

        if home_team == "Lille OSC":
            home_team_1 = ["LOSC Lille"]

        if away_team == "Lille OSC":
            away_team_1 = ["LOSC Lille"]

        home_team_1 = home_team_1[0]
        away_team_1 = away_team_1[0]

        if home_team_1 == team or away_team_1 == team:
            match["homeTeam"]["name"] = home_team_1
            match["awayTeam"]["name"] = away_team_1
            logging.info(match['homeTeam']['name'])
            return {"home_team": match["homeTeam"]["name"], "away_team":match["awayTeam"]["name"]}

next_matches = {}
for team in fifa_names:
    next_matches[team] = get_next_match_for_team(team)
logging.info(next_matches)

def matches_goals_number_records():

    matches_goals = [match["home_team_goals"] + match["away_team_goals"] for match in matches]
    min_goals = matches[matches_goals.index(min(matches_goals))]
    max_goals = matches[matches_goals.index(max(matches_goals))]
    return [min_goals, max_goals]

def highest_match_capacity():

    #find stadium with the highest capacity
    stadium_capacities = [teams_info[team]["stadium_capacity"] for team in teams_info]
    biggest_capacity = max(stadium_capacities)
    for team in teams_info:
        if teams_info[team]["stadium_capacity"] == biggest_capacity:
            biggest_capacity_stadium = team
            break
    club_with_biggest_stadium = club_names[fifa_names.index(biggest_capacity_stadium)]

    #find the strongest team that played as a guest on this stadium

    matches_on_biggest_stadium = [match for match in matches if match["home_team"] == club_with_biggest_stadium]
    rankings_for_guest = []
    for match in matches_on_biggest_stadium:
        for club in clubs_sorted:
            if match["away_team"] == club["name"]:
                rankings_for_guest.append(club["rank"])
                break

    for club in clubs_sorted:
        if club["rank"] == min(rankings_for_guest):
            highest_ranked_away_team = club["name"]
            break

    for match in matches:
        if match["home_team"] == club_with_biggest_stadium and match["away_team"] == highest_ranked_away_team:
            match_with_highest_visit = match
            break

    return [match_with_highest_visit, biggest_capacity]

#highest_match_capacity()


