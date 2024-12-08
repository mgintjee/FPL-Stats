# Add the libraies path to python
import sys
import os
sys.path.append(os.path.join(os.getcwd(), '..\\python\\data'))
sys.path.append(os.path.join(os.getcwd(), '..\\python\\data\\common'))

# Import libraries
import matplotlib.pyplot
from prettytable import PrettyTable 
import chart_utils


def get_draft_player_data(database):
    draft_player_data = dict()
    for draft_round in range(database.get_draft_length()):
        draft_round_players = dict()
        for name in database.get_managers():
            drafter = database.get_managers().index(name)
            draft_round_players[name] = database.get_draft_round_player_for(drafter, draft_round)
            
        draft_round_player_data = list()
        for name in database.get_managers():
            draft_round_player_data.append(database.get_player_data_for(name, draft_round_players[name]))
        draft_player_data[draft_round] = draft_round_player_data        
    return draft_player_data

def chart_draft_most_active(database):
    draft_player_data = get_draft_player_data(database)
    
    headers = ["Most Active", "Drafter", "Position", "Name", "Total Minutes"]
    pretty_table = PrettyTable(headers);
        
    for draft_round in range(database.get_draft_length()):
        draft_picks = list(draft_player_data[draft_round])
        player = None
        drafter = "UNKNOWN"
        
        for i in range(len(draft_picks)):
            draft_pick = draft_picks[i]
            # Ignore empty picks
            if draft_pick == None:
                continue
            if player == None or draft_pick.get_min() > player.get_min():
                drafter = database.get_managers()[i]
                player = draft_pick
                
        pretty_table.add_row(["Round " + str(draft_round + 1), drafter, player.get_position(), player.get_name(), player.get_min()])
        
    print(pretty_table)

def chart_draft_most_impactful(database):
    draft_player_data = get_draft_player_data(database)
    
    headers = ["Most Impactful", "Drafter", "Position", "Name", "Total Points"]
    pretty_table = PrettyTable(headers);
        
    for draft_round in range(database.get_draft_length()):
        draft_picks = list(draft_player_data[draft_round])
        player = None
        drafter = "UNKNOWN"
        
        for i in range(len(draft_picks)):
            draft_pick = draft_picks[i]
            # Ignore empty picks
            if draft_pick == None:
                continue
            if player == None or draft_pick.get_points() > player.get_points():
                drafter = database.get_managers()[i]
                player = draft_pick
                
        pretty_table.add_row(["Round " + str(draft_round + 1), drafter, player.get_position(), player.get_name(), player.get_points()])
        
    print(pretty_table)
    
def chart_draft_most_effective(database):
    draft_player_data = get_draft_player_data(database)
    
    headers = ["Most Effective", "Drafter", "Position", "Name", "Points per Game"]
    pretty_table = PrettyTable(headers);
        
    for draft_round in range(database.get_draft_length()):
        draft_picks = list(draft_player_data[draft_round])
        player = None
        drafter = "UNKNOWN"
        
        for i in range(len(draft_picks)):
            draft_pick = draft_picks[i]
            # Ignore empty picks
            if draft_pick == None:
                continue
            if player == None or draft_pick.get_ppg() > player.get_ppg():
                drafter = database.get_managers()[i]
                player = draft_pick
                
        pretty_table.add_row(["Round " + str(draft_round + 1), drafter, player.get_position(), player.get_name(), player.get_ppg()])
        
    print(pretty_table)
    
def chart_draft_impacts(database):
    draft_player_data = get_draft_player_data(database)
    
    headers = ["Most Effective", "Drafter", "Position", "Name", "Points per Game"]
    pretty_table = PrettyTable(headers);
        
    for draft_round in range(database.get_draft_length()):
        draft_picks = list(draft_player_data[draft_round])
        
        headers = ["Round " + str(draft_round + 1) + ": Drafter", "Position", "Name", "Total Points"]
        pretty_table = PrettyTable(headers);
        
        for i in range(len(draft_picks)):
            drafter = database.get_managers()[i]
            draft_pick = draft_picks[i]
            # Ignore empty picks
            if draft_pick == None:
                pretty_table.add_row([drafter, "-", "-", "-"])
            else:
                pretty_table.add_row([drafter, draft_pick.get_position(), draft_pick.get_name(), draft_pick.get_points()])
        
        print(pretty_table)