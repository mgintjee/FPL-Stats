# Add the libraies path to python
import sys
import os
sys.path.append(os.path.join(os.getcwd(), '..\\python\\data'))
sys.path.append(os.path.join(os.getcwd(), '..\\python\\data\\common'))

# Import libraries
import matplotlib.pyplot
from prettytable import PrettyTable 
import chart_utils

TABLE_DELIMITER = "\n----------\n"

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

def get_least_effective_row(database, player_data):
    player = None
    drafter = None
    for i in range(len(player_data)):
        datum = player_data[i]
        # Check if the data for this player is empty
        if datum == None:
            player = None
            drafter = database.get_managers()[i]
            break
        elif player == None or datum.get_ppg() < player.get_ppg():
            player = datum
            drafter = database.get_managers()[i]
    row_entry = [drafter]
    if player != None:
        row_entry.extend([player.get_position(), player.get_name(), player.get_ppg()])
    else:
        row_entry.extend(["-", "-", "-"])
        
    return row_entry

def get_most_effective_row(database, player_data):
    player = None
    drafter = None
    for i in range(len(player_data)):
        datum = player_data[i]
        # Ignore empty picks
        if datum == None:
            continue
        if player == None or datum.get_ppg() > player.get_ppg():
            drafter = database.get_managers()[i]
            player = datum
    return [drafter, player.get_position(), player.get_name(), player.get_ppg()]

def get_least_impact_row(database, player_data):
    player = None
    drafter = None
    for i in range(len(player_data)):
        datum = player_data[i]
        # Check if the data for this player is empty
        if datum == None:
            player = None
            drafter = database.get_managers()[i]
            break
        elif player == None or datum.get_points() < player.get_points():
            player = datum
            drafter = database.get_managers()[i]
    row_entry = [drafter]
    if player != None:
        row_entry.extend([player.get_position(), player.get_name(), player.get_points()])
    else:
        row_entry.extend(["-", "-", "-"])
        
    return row_entry

def get_most_impact_row(database, player_data):
    player = None
    drafter = None
    for i in range(len(player_data)):
        datum = player_data[i]
        # Ignore empty picks
        if datum == None:
            continue
        if player == None or datum.get_points() > player.get_points():
            drafter = database.get_managers()[i]
            player = datum
    return [drafter, player.get_position(), player.get_name(), player.get_points()]

def get_least_active_row(database, player_data):
    player = None
    drafter = None
    for i in range(len(player_data)):
        datum = player_data[i]
        # Check if the data for this player is empty
        if datum == None:
            player = None
            drafter = database.get_managers()[i]
            break
        elif player == None or datum.get_min() < player.get_min():
            player = datum
            drafter = database.get_managers()[i]
    row_entry = [drafter]
    if player != None:
        row_entry.extend([player.get_position(), player.get_name(), player.get_min()])
    else:
        row_entry.extend(["-", "-", "-"])
        
    return row_entry

def get_most_active_row(database, player_data):
    player = None
    drafter = None
    for i in range(len(player_data)):
        datum = player_data[i]
        # Ignore empty picks
        if datum == None:
            continue
        if player == None or datum.get_min() > player.get_min():
            drafter = database.get_managers()[i]
            player = datum
    return [drafter, player.get_position(), player.get_name(), player.get_min()]

def chart_draft_most_least_active(database):
    draft_player_data = get_draft_player_data(database)
    
    headers = ["Round", "Most Active", "Least Active"]
    pretty_table = PrettyTable(headers);
        
    for draft_round in range(database.get_draft_length()):
        draft_picks = list(draft_player_data[draft_round])
        row_entry = [str(draft_round + 1)]         
        headers = ["Drafter", "Position", "Name", "Minutes Played"]
        most_pretty_table = PrettyTable(headers);
        most_pretty_table.add_row(get_most_active_row(database, draft_picks))
        least_pretty_table = PrettyTable(headers);
        least_pretty_table.add_row(get_least_active_row(database, draft_picks))
        row_entry.extend([most_pretty_table, least_pretty_table])
        pretty_table.add_row(row_entry)
        
    print(pretty_table)

def chart_draft_most_least_impact(database):
    draft_player_data = get_draft_player_data(database)
    
    headers = ["Round", "Most Impact", "Least Impact"]
    pretty_table = PrettyTable(headers);
        
    for draft_round in range(database.get_draft_length()):
        draft_picks = list(draft_player_data[draft_round])
        row_entry = [str(draft_round + 1)]         
        headers = ["Drafter", "Position", "Name", "Total Points"]
        most_pretty_table = PrettyTable(headers);
        most_pretty_table.add_row(get_most_impact_row(database, draft_picks))
        least_pretty_table = PrettyTable(headers);
        least_pretty_table.add_row(get_least_impact_row(database, draft_picks))
        row_entry.extend([most_pretty_table, least_pretty_table])
        pretty_table.add_row(row_entry)
        
    print(pretty_table)
    
def chart_draft_most_least_effective(database):
    draft_player_data = get_draft_player_data(database)
    
    headers = ["Round", "Most Effective", "Least Effective"]
    pretty_table = PrettyTable(headers);
        
    for draft_round in range(database.get_draft_length()):
        draft_picks = list(draft_player_data[draft_round])
        row_entry = [str(draft_round + 1)]         
        headers = ["Drafter", "Position", "Name", "Points per game"]
        most_pretty_table = PrettyTable(headers);
        most_pretty_table.add_row(get_most_effective_row(database, draft_picks))
        least_pretty_table = PrettyTable(headers);
        least_pretty_table.add_row(get_least_effective_row(database, draft_picks))
        row_entry.extend([most_pretty_table, least_pretty_table])
        pretty_table.add_row(row_entry)
        
    print(pretty_table)
    
def has_player_been_traded_or_dropped(database, manager, player):   
    if player.is_free_agent():
        return True
    
    for other_manager in database.get_managers():
        if manager == other_manager:
            continue
        if database.get_player_data_for(other_manager, player.get_id()):
            return True
    return False
    
def chart_draft_impacts(database):
    draft_player_data = get_draft_player_data(database)
    
    headers = ["Drafter", "Position", "Name", "Total Points", "Traded / Dropped"]
    pretty_table = PrettyTable(headers);
            
    for draft_round in range(database.get_draft_length()):
        draft_picks = list(draft_player_data[draft_round])
        pretty_table.add_row(["\nRound " + str(draft_round + 1) + "\n", TABLE_DELIMITER, TABLE_DELIMITER, TABLE_DELIMITER, TABLE_DELIMITER])
        
        for i in range(len(draft_picks)):
            drafter = database.get_managers()[i]
            draft_pick = draft_picks[i]
            # Ignore empty picks
            if draft_pick == None:
                pretty_table.add_row([drafter, "-", "-", "-", "-"])
            else:
                pretty_table.add_row([drafter, draft_pick.get_position(), draft_pick.get_name(), draft_pick.get_points(), \
                                      has_player_been_traded_or_dropped(database, drafter, draft_pick)])
        
    print(pretty_table)