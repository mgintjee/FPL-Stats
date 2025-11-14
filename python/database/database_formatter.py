# Add the libraies path to python
import sys
import os
sys.path.append(os.path.join(os.getcwd(), '..\\python\\stats' ))

# Import libraries
import math
import stats_utils
import statistics

def format_manager_gw_scores(db):
    managers_z_scores = dict()
    
    for name in db.get_managers():
        manager_gw_scores = db.get_manager_gw_scores(name)
        
        managers_z_scores[name] = list()
        managers_z_scores[name].append(statistics.mean(manager_gw_scores))
        managers_z_scores[name].append(statistics.median(manager_gw_scores))
    
    return managers_z_scores

def format_manager_z_scores(db):
    managers_z_scores = dict()
    
    for name in db.get_managers():
        manager_z_scores = db.get_manager_z_scores(name)
        
        managers_z_scores[name] = list()
        managers_z_scores[name].append(statistics.mean(manager_z_scores))
        managers_z_scores[name].append(statistics.median(manager_z_scores))
    
    return managers_z_scores

def format_opponent_gw_scores(db):
    managers_z_scores = dict()
    
    for name in db.get_managers():
        opponent_gw_scores = db.get_opponent_gw_scores(name)
        
        managers_z_scores[name] = list()
        managers_z_scores[name].append(statistics.mean(opponent_gw_scores))
        managers_z_scores[name].append(statistics.median(opponent_gw_scores))
    
    return managers_z_scores

def format_opponent_z_scores(db):
    managers_z_scores = dict()
    
    for name in db.get_managers():
        opponent_z_scores = db.get_opponent_z_scores(name)
        
        managers_z_scores[name] = list()
        managers_z_scores[name].append(statistics.mean(opponent_z_scores))
        managers_z_scores[name].append(statistics.median(opponent_z_scores))
    
    return managers_z_scores

def format_head_to_heads(db):
    head_to_heads = dict()
    
    for name in db.get_managers():
        head_to_heads[name] = list()
        
        for unused in db.get_managers():
            head_to_heads[name].append(0 if unused != name else None)
        
        for opponent in db.get_managers():
            
            if name == opponent: 
                continue
                
            gws = db.get_opponent_gws(name, opponent)
            opponent_index = db.get_managers().index(opponent)
            
            for gw in gws:
                previous_value = head_to_heads[name][opponent_index]
                if(db.get_gw_score(name, gw) > db.get_gw_score(opponent, gw)):
                    previous_value += 1                    
                head_to_heads[name][opponent_index] = previous_value
    
    return head_to_heads    

def format_race_to_the_bottom(db):
    number_of_gws = db.get_number_of_gws()
    managers = db.get_managers()

    manager_rank_scores = dict()
    manager_ranks_over_time = dict()

    for name in managers:
        manager_ranks_over_time[name] = list()
        manager_rank_scores[name] = list()
        manager_scores = db.get_manager_gw_scores(name)

        for gw in range(number_of_gws):
            if(gw == 0):
                rank_score = 0
            else:
                rank_score = manager_rank_scores[name][gw - 1]
            manager_score = db.get_gw_score(name, gw)
            opponent_score = db.get_opponent_score(name, gw)

            # Calculate the result score
            result_score = 30000 if manager_score > opponent_score else 10000 if manager_score == opponent_score else 0
            rank_score += result_score + manager_score
            manager_rank_scores[name].append(rank_score)

    for gw in range(number_of_gws):
        manager_rank_scores_for_gw = dict()

        for name in managers:
            manager_rank_scores_for_gw[name] = manager_rank_scores[name][gw]

        manager_ranks_for_gw = sorted(manager_rank_scores_for_gw.items(), key=lambda item: item[1], reverse = True)
        manager_ranks = list()
        for sorted_managers in manager_ranks_for_gw:
            name = sorted_managers[0]
            manager_ranks.append(name)

        for name in managers:
            manager_ranks_over_time[name].append(manager_ranks.index(name) + 1)
           
    return manager_ranks_over_time