# Add the libraies path to python
import sys
import os
sys.path.append(os.path.join(os.getcwd(), '..\\python\\data'))
sys.path.append(os.path.join(os.getcwd(), '..\\python\\data\\common'))
sys.path.append(os.path.join(os.getcwd(), '..\\python\\data\\players'))

# Import libraries
import matplotlib.pyplot
from prettytable import PrettyTable 
import pandas as pd
import chart_utils
import player_constants

#Constants
MANAGER_KEY = "Manager"
PICKUP_PLAYER_IMPACT_KEY = "Most Impactful Player (Pick-up)"
DRAFT_PLAYER_IMPACT_KEY = "Most Impactful Player (Drafted)"
CONTRIBUTION_KEY = "% Contribution"
TOTAL_POINTS_KEY = "Total Points"
TOTAL_MINUTES_KEY = "Total Minutes"
POINTS_PER_90_KEY = "Points Per 90"

def get_team_from(team):
    if "/" in team:
        team_parts = team.split("/")
        return team_parts[len(team_parts) - 1]
    else:
        return team

def get_roster_contributions_for_all_teams(manager, database):
    team_points = dict()
    
    for datum in database.get_player_data(manager):
            
        team = get_team_from(datum.get_team())
        if team not in team_points.keys():
            team_points[team] = [0, 0]
        team_points[team][0] = team_points[team][0] + datum.get_points()
        team_points[team][1] = team_points[team][1] + datum.get_min()
    
    return team_points

def get_roster_contributions_for_top_team(manager, database):
    team_name = ""
    team_total_points = 0
    team_minutes = 0
    manager_total_points = 0
    
    team_points = get_roster_contributions_for_all_teams(manager, database) 
    for name in team_points.keys():
        points = team_points[name][0]
        if points > team_total_points:
            team_name = name
            team_total_points = points
            team_minutes = team_points[name][1]
        manager_total_points += points
    
    return [team_name, round((team_total_points / manager_total_points) * 100, 2), team_total_points, team_minutes, round(team_total_points / (team_minutes / 90), 2)]

def get_roster_contributions_for_team(manager, database):
    team_points = get_roster_contributions_for_all_teams(manager, database) 
    
    manager_total_points = 0    
    
    for name in team_points.keys():
        points = team_points[name][0]
        manager_total_points += points
    
    sorted_teams = sorted(team_points.items(), key = lambda item: item[1], reverse = True)
    
    top_1_team = sorted_teams[0]
    top_2_team = sorted_teams[1]
    top_3_team = sorted_teams[2]
    
    top_1_team_contribution = round((top_1_team[1][0] / manager_total_points) * 100, 2)
    top_2_team_contribution = round((top_2_team[1][0] / manager_total_points) * 100, 2)
    top_3_team_contribution = round((top_3_team[1][0] / manager_total_points) * 100, 2)
    
    return [top_1_team[0] + " (" + str(top_1_team_contribution) + " % )", \
            top_2_team[0] + " (" + str(top_2_team_contribution) + " % )", \
            top_3_team[0] + " (" + str(top_3_team_contribution) + " % )"]

def get_roster_contributions_for_position(manager, database):
    manager_total_points = 0
    positional_data = dict()
    for position in player_constants.POSITIONS:
        positional_data[position] = 0
    
    for datum in database.get_player_data(manager):
        positional_data[datum.get_position()] += datum.get_points()
        manager_total_points += datum.get_points()
        
    return [round((positional_data[player_constants.KEEPER_VALUE] / manager_total_points) * 100, 2), \
            round((positional_data[player_constants.DEFENDER_VALUE] / manager_total_points) * 100, 2), \
            round((positional_data[player_constants.MIDFIELDER_VALUE] / manager_total_points) * 100, 2), \
            round((positional_data[player_constants.FORWARD_VALUE] / manager_total_points) * 100, 2)]

def get_roster_contributions_for_players(manager, database, wasDrafted):
    player_name = ""
    player_total_points = 0
    player_minutes = 0
    manager_total_points = 0
    
    for datum in database.get_player_data(manager):
        datumDrafted = database.was_player_id_drafted(manager, datum.get_id())
        if wasDrafted == datumDrafted and datum.get_points() > player_total_points:
            player_name = datum.get_name() + " (" + datum.get_team() + ")"
            player_total_points = datum.get_points()
            player_minutes = datum.get_min()
        manager_total_points += datum.get_points()
    
    return [player_name, round((player_total_points / manager_total_points) * 100, 2), player_total_points, player_minutes, round(player_total_points / (player_minutes / 90), 2)]

def chart_roster_contributions_for_players(database, wasDrafted):    
    headers = ["Manager", "Most Impactful Player " + ("(Drafted)" if wasDrafted else "(Pick-up)") , "% Contribution", "Total Points", "Total Minutes", "Points per 90"]
    pretty_table = PrettyTable(headers);
    
    for manager in database.get_managers():
        row_data = [manager]
        row_data.extend(get_roster_contributions_for_players(manager, database, wasDrafted))
        pretty_table.add_row(row_data)
    
    
    pandas_headers = {
        #MANAGER_KEY: list(),
        DRAFT_PLAYER_IMPACT_KEY if wasDrafted else PICKUP_PLAYER_IMPACT_KEY: list(),
        CONTRIBUTION_KEY: list(),
        TOTAL_POINTS_KEY: list(),
        TOTAL_MINUTES_KEY: list(),
        POINTS_PER_90_KEY: list()
    }
    
    for manager in database.get_managers():
        data = get_roster_contributions_for_players(manager, database, wasDrafted)
        #pandas_headers[MANAGER_KEY].append(manager)
        pandas_headers[DRAFT_PLAYER_IMPACT_KEY if wasDrafted else PICKUP_PLAYER_IMPACT_KEY].append(data[0])
        pandas_headers[CONTRIBUTION_KEY].append(data[1])
        pandas_headers[TOTAL_POINTS_KEY].append(data[2])
        pandas_headers[TOTAL_MINUTES_KEY].append(data[3])
        pandas_headers[POINTS_PER_90_KEY].append(data[4])
    df = pd.DataFrame(pandas_headers, index = database.get_managers())
    print(df)
    
def chart_roster_contributions_for_top_teams(database):    
    headers = ["Manager", "Most Impactful Team", "% Contribution", "Total Points", "Total Minutes", "Points per 90"]
    pretty_table = PrettyTable(headers);
    
    for manager in database.get_managers():
        row_data = [manager]
        row_data.extend(get_roster_contributions_for_top_team(manager, database))
        pretty_table.add_row(row_data)
    
    print(pretty_table)
    
def chart_roster_contributions_for_teams(database):    
    headers = ["Manager", "Most Impactful Team", "2nd Most Impactful Team", "3rd Most Impactful Team"]
    pretty_table = PrettyTable(headers);
    
    for manager in database.get_managers():
        row_data = [manager]
        row_data.extend(get_roster_contributions_for_team(manager, database))
        pretty_table.add_row(row_data)
    
    print(pretty_table)
    
def chart_roster_contributions_for_positions(database):    
    headers = ["Manager", "G %", "D %", "M %", "F %"]
    pretty_table = PrettyTable(headers);
    
    for manager in database.get_managers():
        row_data = [manager]
        row_data.extend(get_roster_contributions_for_position(manager, database))
        pretty_table.add_row(row_data)
    
    print(pretty_table)
    
def chart_postitional_contributions(database):
    headers = ["Position", "% Contribution", "Total Points"]
    pretty_table = PrettyTable(headers);
    positional_data = dict()
    total = 0
    
    for position in player_constants.POSITIONS:
        positional_data[position] = 0
        
    for manager in database.get_managers():
        for data in database.get_player_data(manager):
            positional_data[data.get_position()] += data.get_points()
            total += data.get_points()
    sorted_positions = sorted(player_constants.POSITIONS, reverse = True, key = lambda ele: positional_data[ele])
    for position in sorted_positions:
        contribution = positional_data[position] / total * 100
        row_data = [position, round(contribution, 2), positional_data[position]]
        pretty_table.add_row(row_data)
        
    print(pretty_table)
    
def chart_team_contributions(database):
    headers = ["Team", "% Contribution", "Total Points"]
    pretty_table = PrettyTable(headers);
    team_data = dict()
    total = 0
        
    for manager in database.get_managers():
        for datum in database.get_player_data(manager):
            team = get_team_from(datum.get_team())
            if team not in team_data.keys():
                team_data[team] = 0
            team_data[team] += datum.get_points()
            total += datum.get_points()
            
    sorted_teams = sorted(team_data.keys(), reverse = True, key = lambda ele: team_data[ele])
    for team in sorted_teams:
        contribution = team_data[team] / total * 100
        row_data = [team, round(contribution, 2), team_data[team]]
        pretty_table.add_row(row_data)
        
    print(pretty_table)
    