from log_config import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from mongo_collections import Database
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

'''element = find_element_by_xpath("element_xpath") needs be replaced with:
element = driver.find_element(By.XPATH, "element_xpath")'''

'''The Selenium automation testing session opens the driver for the selected matches webpages, and puts the results into a Mongo database. These lines
are commented out in order to prevent multiple unnecessary automation testing sessions and adds to the database'''

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
            Database.insertOne("french_league_1", Match1.__dict__)
            logging.debug(Match1)

# driver = webdriver.Chrome("chromedriver_2.exe")
# driver.get(URL_8)
# get_matches(40)
# driver.close()

# driver = webdriver.Chrome("chromedriver_2.exe")
# driver.get(URL_9)
# get_matches(41)
# driver.quit()
#
# driver = webdriver.Chrome("chromedriver_2.exe")
# driver.get(URL_10)
# get_matches(41)
# driver.quit()
#
# driver = webdriver.Chrome("chromedriver_2.exe")
# driver.get(URL_11)
# get_matches(31)
# driver.quit()
#
# driver = webdriver.Chrome("chromedriver_2.exe")
# driver.get(URL_12)
# get_matches(41)
# driver.quit()

matches = [item for item in Database.findAll("french_league_1", {})]

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

process_all_matches()
#logging.debug(matches)
#clubs = sorted(clubs, key = lambda k: k['pts'], reverse=True)
clubs_sorted = sorted(clubs, key=itemgetter('pts'), reverse=True)
rank = itertools.count()
for club in clubs_sorted:
    club["rank"] = next(rank) + 1
logging.debug(clubs_sorted)
logging.debug(matches)

def get_latest_team_match(team):
    matches_for_team = []
    team = clubs[fifa_names.index(team)]["name"]
    for match in matches:
        if match["home_team"] == team or match["away_team"] == team:
            matches_for_team.append(match)
    return matches_for_team[-1]

def get_next_match_for_team(team):
    for match in Database.findAll("french_ligue_1_upcoming_matches", {}):

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
            return match

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

#Database.dropCol("french_league_1")

#response = requests.get("https://soccer.sportmonks.com/api/v2.0/leagues")
#print(response.json())

highest_match_capacity()
