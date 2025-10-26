# Add the libraies path to python
import sys
import os
#sys.path.append(os.path.join(os.getcwd(), '..\\python\\data' ))
#sys.path.append(os.path.join(os.getcwd(), '..\\python\\data\\managers' ))
#sys.path.append(os.path.join(os.getcwd(), '..\\python\\data\\\draft' ))
sys.path.append(os.path.join(os.getcwd(), '..\\python\\stats' ))

# Import libraries
import math
import stats_utils

def get_player_data_for(databse, name, player_id):
    player_data = databse.get_player_data(name)
    for datum in player_data:
        if datum.get_id() == player_id:
            return datum
    return None
        
def get_opponent_gw_scores(database, name):
    opponent_scores = list()
    for gw in range(database.get_number_of_gws()):
        opponent = database.get_opponent(name, gw)
        opponent_scores.append(database.get_gw_score(opponent, gw))
    return opponent_scores

def get_opponent_gws(database, name, opponent):
    gws = list()
    manager_index = database.get_managers().index(name)
    opponent_index = database.get_managers().index(opponent)
    schedule = database.get_schedules()[manager_index]
    gw_step = schedule.index(opponent_index)
    max_head_to_heads = math.ceil(database.get_number_of_gws() / (len(database.get_managers()) - 1))
    for i in range(max_head_to_heads):
        gw = gw_step + (i * (len(database.get_managers()) - 1))
        if(gw > database.get_number_of_gws() - 1):
            break
        gws.append(gw)
    return gws

def get_gw_scores(database, gw):
    gw_data = list()
    for name in database.get_managers():
        gw_data.append(database.get_gw_score(name, gw))
    return gw_data
        
def get_z_score(database, manager, gw):
    gw_data = database.get_gw_scores(gw)
    score = database.get_gw_score(manager, gw)
    return stats_utils.get_z_score(score, gw_data)

def get_opponent(database, name, gw):
    manager_index = database.get_managers().index(name)
    schedule = database.get_schedules()[manager_index]
    if(gw >= len(schedule)):
        gw = gw % len(schedule)
    opponent_index = schedule[gw]
    return database.get_managers()[opponent_index]
    
def get_gw_z_scores(database, gw):
    gw_z_scores = list()
    for name in database.get_managers():
        gw_z_scores.append(database.get_z_score(name, gw))
    return gw_z_scores
    
def get_manager_z_scores(database, name):
    manager_scores = database.get_manager_gw_scores(name)
    manager_z_scores = list()
    for gw in range(len(manager_scores)):
        gw_scores = database.get_gw_scores(gw)
        manager_z_scores.append(stats_utils.get_z_score(manager_scores[gw], gw_scores))
    return manager_z_scores
    
def get_opponent_z_scores(database, opponent):
    opponent_scores = database.get_opponent_gw_scores(opponent)
    opponent_z_scores = list()
    for gw in range(len(opponent_scores)):
        gw_scores = database.get_gw_scores(gw)
        opponent_z_scores.append(stats_utils.get_z_score(opponent_scores[gw], gw_scores))
    return opponent_z_scores

def get_manager_performance_for_gw(database, manager, best_performance, won_gw):
    gw_to_return = -1
    manager_z_score = -100 if best_performance else 100
    manager_gw_score = -1000 if best_performance else 1000
    for gw in range(database.get_number_of_gws()):
        opponent = database.get_opponent(manager, gw)
        manager_score = database.get_gw_score(manager, gw)
        opponent_score = database.get_gw_score(opponent, gw)
        # Check if the result matches the parameter
        if((manager_score > opponent_score) == won_gw):
            # manager_gw_z_score = database.get_z_score(manager, gw)
#            if((best_performance and manager_gw_z_score > manager_z_score) or
#               (not best_performance and manager_gw_z_score < manager_z_score)):
            if((best_performance and manager_score > manager_gw_score) or
               (not best_performance and manager_score < manager_gw_score)):
                manager_gw_score = manager_score
                gw_to_return = gw
    return gw_to_return
    
def get_manager_performance_gws(database, best_performance, won_gw):
    manager_results = dict()
    for manager in database.get_managers():
        manager_results[manager] = get_manager_performance_for_gw(database, manager, best_performance, won_gw)
    return manager_results

def get_best_performing_loss_gws(database):
    return get_manager_performance_gws(database, True, False)

def get_worst_performing_win_gws(database):
    return get_manager_performance_gws(database, False, True)

def get_best_performing_win_gws(database):
    return get_manager_performance_gws(database, True, True)

def get_worst_performing_loss_gws(database):
    return get_manager_performance_gws(database, False, False)
