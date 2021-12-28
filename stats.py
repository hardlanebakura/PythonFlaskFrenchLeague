import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
from teams import all_players, get_players_for_team
from matches import *
from logging.config import logging
from player import Player

plt.rcdefaults()

def find_number_one_players_in_various_categories():
    sort_players_h = sorted(all_players, key=lambda x: x.height_cm)
    sort_players_w = sorted(all_players, key=lambda x: x.weight_kg)
    players = [player for player in all_players if isinstance(player, Player)]
    sort_players_fk_accuracy = sorted(players, key=lambda x: x.skill_fk_accuracy, reverse=True)
    lowest_height_player = sort_players_h[0]
    highest_height_player = sort_players_h[-1]
    lowest_weight_player = sort_players_w[0]
    highest_weight_player = sort_players_w[-1]
    highest_fk_accuracy_player = sort_players_fk_accuracy[0]
    list1 = [lowest_height_player, highest_height_player, lowest_weight_player, highest_weight_player, highest_fk_accuracy_player]
    return list1

def remove_small_labels(d):
    others = {}
    sum = 0
    for item in d:
        if d[item] < 4:
            others[item] = d[item]
            sum = sum + d[item]
    for item in others:
        if item in d:
            del d[item]
    d["Others"] = sum
    logging.info(d)
    return d

def find_preferred_foot():
    right_footed_players = [player for player in all_players if player.preferred_foot == "Right"]
    left_footed_players = [player for player in all_players if player.preferred_foot == "Left"]
    labels = ["Right", "Left"]
    sizes = [len(right_footed_players), len(left_footed_players)]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, shadow=False, startangle=90, labeldistance=1.1, autopct=lambda p: '{:.0f}'.format(p * sum(sizes) / 100), pctdistance=0.9)
    ax1.axis('equal')
    plt.legend(labels=labels, loc="center left")
    plt.tight_layout()
    fig1.set_size_inches(8, 6)
    plt.subplots_adjust(left=0.0, bottom=0.1, right=1.05)
    plt.savefig("static/images/chartforplayerpreferredfoot.png")
    return len(right_footed_players), len(left_footed_players)

def get_chart_player_countries():
    labels = []
    sizes = []
    all_countries = [player.nationality_name for player in all_players]
    newlist = [n for n, count in Counter(all_countries).most_common() for i in range(count)]
    logging.debug(newlist)
    a = remove_small_labels(dict(Counter(all_countries)))
    logging.debug(a)
    for country in a:
        labels.append(country)
    for value in a.values():
        sizes.append(value)
    logging.debug(sizes)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, shadow=False, startangle=90, labeldistance=1.1, autopct=lambda p: '{:.0f}'.format(p * sum(sizes) / 100), pctdistance=0.9)
    ax1.axis('equal')
    plt.legend(labels=labels, loc="center left")
    plt.tight_layout()
    fig1.set_size_inches(8, 6)
    plt.subplots_adjust(left=0.0, bottom=0.1, right=1.05)
    plt.savefig("static/images/chartforplayernationalities.png")
    remove_small_labels(a)

find_number_one_players_in_various_categories()
#find_preferred_foot()
#get_chart_player_countries()

def find_biggest_upset():
    #finds the most unexpected outcome
    list_of_matches = []
    for match in matches:
        if match["home_team_goals"] != match["away_team_goals"]:
            for club in clubs_sorted:
                if club["name"] == match["home_team"]:
                    home_team_rank = club["rank"]
                if club["name"] == match["away_team"]:
                    away_team_rank = club["rank"]
            if match["home_team_goals"] > match["away_team_goals"]:
                if away_team_rank < home_team_rank:
                    list_of_matches.append(match)
                    list_of_matches[-1]["rank_difference"] = home_team_rank - away_team_rank
            else:
                if home_team_rank < away_team_rank:
                    list_of_matches.append(match)
                    list_of_matches[-1]["rank_difference"] = away_team_rank - home_team_rank
    element = sorted(list_of_matches, key=lambda x: x["rank_difference"])[-1]
    logging.info(element)
    return element

find_biggest_upset()

def stats_team_foreigners():
    list_foreigners = []
    for team in fifa_names:
        foreigners_team = 0
        for player in get_players_for_team(team):
            if player.nationality_name != "France":
                foreigners_team = foreigners_team + 1
        list_foreigners.append({"name":team, "foreigners":foreigners_team})
    list_foreigners = sorted(list_foreigners, key=itemgetter("foreigners"), reverse=True)
    return list_foreigners

team_with_most_foreigners = stats_team_foreigners()
logging.debug(clubs_sorted)


def get_preferred_foot_teams():
    list_preferred_foot = []
    for team in fifa_names:
        preferred_foot_team = 0
        for player in get_players_for_team(team):
            if player.preferred_foot == "Left":
                preferred_foot_team = preferred_foot_team + 1
        list_preferred_foot.append({"name":team, "left_footed_players":preferred_foot_team})
    list_preferred_foot = sorted(list_preferred_foot, key=itemgetter("left_footed_players"), reverse=True)
    return list_preferred_foot[0]

get_preferred_foot_teams()

def get_weight_kg_skill_relationship():
    d = {}
    player_weights = [player.weight_kg for player in all_players]
    min_weight = min(player_weights)
    max_weight = max(player_weights)
    for i in range(min_weight, max_weight):
        d[i] = 0
    for item in d:
        players_with_selected_weight = []
        for player in all_players:
            if player.weight_kg == item:
                players_with_selected_weight.append(player.overall)
        player_skills_for_selected_weight = {item:int(sum(players_with_selected_weight)/len(players_with_selected_weight))}
        d[item] = player_skills_for_selected_weight[item]
    logging.info(d)
    labels = [weight for weight in d]
    sizes = [d[weight] for weight in d]
    y_pos = np.arange(len(labels))
    plt.figure(figsize=(15, 4))
    plt.bar(y_pos, sizes, align='center', alpha=0.5)
    #plt.barh makes horizontal bar chart
    plt.xticks(y_pos, labels)
    #plt.xticks(y_pos, labels, np.arange(0, 100, 0.712123))
    plt.ylabel('Player overall skill')
    plt.xlabel('Weight')
    plt.title('Player weight to skill relationship')

    #always call savefig before plt.show()
    plt.savefig("./static/images/playerweighttoskillrelationshipchart.png")
    logging.info(plt.rcParams)
    return

#get_weight_kg_skill_relationship()

def get_foreigners_rank_relationship():
    player_nationalities = []
    for team in fifa_names:
        player_nationalities_for_team = [player.nationality_name for player in get_players_for_team(team) if player.nationality_name != "France"]
        #logging.info(player_nationalities_for_team)
        logging.info(team)
        for club in clubs_sorted:
            if club["name"] == club_names[fifa_names.index(team)]:
                logging.info(club["name"])
                logging.info(club["rank"])
                logging.info(len(player_nationalities_for_team))
                player_nationalities.append({"name":club["name"], "rank":club["rank"], "foreigners_number":len(player_nationalities_for_team)})
    player_nationalities = sorted(player_nationalities, key=itemgetter("rank"))
    logging.info(player_nationalities)

    labels = [i + 1 for i in range(20)]
    sizes = [item["foreigners_number"] for item in player_nationalities]

    y_pos = np.arange(len(labels))
    plt.bar(y_pos, sizes, align='center', alpha=0.5)
    # plt.barh makes horizontal bar chart
    plt.xticks(y_pos, labels)
    # plt.xticks(y_pos, labels, np.arange(0, 100, 0.712123))
    plt.ylabel('Foreigners in team')
    plt.xlabel('Rank')
    plt.title('Rank in relation to number of foreigners')

    plt.savefig("./static/images/teamforeignerstorankrelationshipchart.png")

    return player_nationalities

get_foreigners_rank_relationship()
#get_chart_player_countries()
find_biggest_upset()
get_preferred_foot_teams()