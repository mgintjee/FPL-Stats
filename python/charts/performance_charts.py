# Add the libraies path to python
import sys
import os
sys.path.append(os.path.join(os.getcwd(), '..\\python\\data'))
sys.path.append(os.path.join(os.getcwd(), '..\\python\\data\\common'))

# Import libraries
import matplotlib.pyplot
from prettytable import PrettyTable 
import chart_utils

def get_head_to_heads(database):
    head_to_heads = dict()
    for name in database.get_managers():
        head_to_heads[name] = dict()
        for opponent in database.get_managers():
            if name == opponent: 
                continue
            head_to_heads[name][opponent] = list()
            gws = database.get_opponent_gws(name, opponent)
            for gw in gws:
                score = database.get_gw_score(name, gw)
                opponent_score = database.get_gw_score(opponent, gw)
                if(score > opponent_score):
                    head_to_heads[name][opponent].append(1)
                else:
                    head_to_heads[name][opponent].append(0)
    return head_to_heads

def get_managers_sorted_by_wins(head_to_heads):
    managers = head_to_heads.keys()
    total_wins = dict()
    for name in managers:
        total_wins[name] = 0
        for opponent in managers:
            if name == opponent:
                continue
            for value in head_to_heads[name][opponent]:
                total_wins[name] += value
    return sorted(managers, reverse = True, key = lambda ele: total_wins[ele])

def plot_head_to_heads(database):
    head_to_heads = get_head_to_heads(database)  
    sorted_managers = get_managers_sorted_by_wins(head_to_heads)
    
    headers = [database.get_season()]
    for name in sorted_managers:
        headers.append("Against " + name)
    headers.append("Total Wins")
    
    pretty_table = PrettyTable(headers);
        
    for name in sorted_managers:
        row_data = [name]
        total_wins = 0
        for opponent in sorted_managers:
            if name == opponent:
                row_data.append("X")
            else:
                head_to_head = head_to_heads[name][opponent]
                wins = sum(head_to_head)
                total = len(head_to_head)
                row_data.append(chart_utils.get_colored_win_ratio(wins, total))
                total_wins += wins
        row_data.append(chart_utils.get_colored_win_ratio(total_wins, database.get_number_of_gws()))
        pretty_table.add_row(row_data)
    print(pretty_table)
                
def plot_manager_performances(database):
    headers = [database.get_season(), "Avg Z-Score"]
    pretty_table = PrettyTable(headers);
    
    avg_z_scores = dict()
    
    for name in database.get_managers():
        avg_z_scores[name] = database.get_manager_avg_z_score(name)

    for name in sorted(database.get_managers(), reverse = True, key = lambda ele: avg_z_scores[ele]):
        row_data = [name]
        row_data.append(chart_utils.get_color_for_avg_z_score(avg_z_scores[name], False))
        pretty_table.add_row(row_data)
        
    print(pretty_table)
    
def plot_opponent_performances(database):
    headers = [database.get_season(), "Avg Opponent Z-Score"]
    pretty_table = PrettyTable(headers);
        
    avg_z_scores = dict()
    
    for name in database.get_managers():
        avg_z_scores[name] = database.get_opponent_avg_z_score(name)

    for name in sorted(database.get_managers(), reverse = False, key = lambda ele: avg_z_scores[ele]):
        row_data = [name]
        row_data.append(chart_utils.get_color_for_avg_z_score(avg_z_scores[name], True))
        pretty_table.add_row(row_data)

    print(pretty_table)