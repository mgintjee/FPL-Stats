# Add the libraies path to python
import sys
import os
sys.path.append(os.path.join(os.getcwd(), '..\\python\\data' ))
sys.path.append(os.path.join(os.getcwd(), '..\\python\\data\\managers' ))
sys.path.append(os.path.join(os.getcwd(), '..\\python\\data\\\draft' ))
sys.path.append(os.path.join(os.getcwd(), '..\\python\\stats' ))

# Import libraries
import data_constants
import manager_reader
import draft_reader
import stats_utils
import database_utils
import math

class database:
    def __init__(self, season):
        path_to_data = os.getcwd() + "\\..\\" +\
            data_constants.DATA + "\\" +\
            data_constants.SEASONS + "\\" +\
            season
        self._season = season
        self._draft_reader = draft_reader.draft_reader(path_to_data)
        self._manager_reader = manager_reader.manager_reader(path_to_data)
        
    def get_season(self):
        return self._season
    
    def get_managers(self):
        return self._draft_reader.get_order()
    
    def get_schedules(self):
        return self._draft_reader.get_schedules()
    
    def get_draft_results(self):
        return self._draft_reader.get_results()
    
    def get_manager_gw_scores(self, name):
        return self._manager_reader.get_manager_gw_scores(name)
    
    def get_manager_activity_reader(self, name):
        return self._manager_reader.get_manager_activity_reader(name)
    
    def get_manager_player_database(self, name):
        return self._manager_reader.get_player_database(name)
    
    def get_draft_length(self):
        return self._draft_reader.get_length()
    
    def get_draft_round_player_for(self, name, draft_round):
        return self.get_draft_results()[name][draft_round]
    
    def get_player_data_for(self, name, player_id):
        return database_utils.get_player_data_for(self, name, player_id)
    
    def get_player_data(self, name):
        return self._manager_reader.get_player_database(name).get_all_player_data()
    
    def get_opponent_gw_scores(self, name):
        return database_utils.get_opponent_gw_scores(self, name)
    
    def get_number_of_gws(self):
        return len(self._manager_reader.get_manager_gw_scores(self.get_managers()[0]))
    
    def get_gw_z_scores(self, gw):
        return database_utils.get_gw_z_scores(self, gw)
    
    def get_manager_z_scores(self, name):
        return database_utils.get_manager_z_scores(self, name)
    
    def get_manager_best_performing_loss_gws(self):
        return database_utils.get_best_performing_loss_gws(self)
    
    def get_manager_worst_performing_win_gws(self):
        return database_utils.get_worst_performing_win_gws(self)

    def get_best_performing_loss_gws(database):
        return database_utils.get_best_performing_loss_gws(database)
    
    def get_worst_performing_win_gws(database):
        return database_utils.get_worst_performing_win_gws(database)

    def get_best_performing_win_gws(database):
        return database_utils.get_best_performing_win_gws(database)

    def get_worst_performing_loss_gws(database):
        return database_utils.get_worst_performing_loss_gws(database)
    
    def get_opponent_z_scores(self, opponent):
        return database_utils.get_opponent_z_scores(self, opponent)
    
    def get_manager_avg_z_score(self, name):
        return stats_utils.get_mean(self.get_manager_z_scores(name))
    
    def get_opponent_avg_z_score(self, opponent):
        return stats_utils.get_mean(self.get_opponent_z_scores(opponent))
    
    def get_gw_score(self, name, gw):
        return self.get_manager_gw_scores(name)[gw]
    
    def get_opponent(self, name, gw):
        return database_utils.get_opponent(self, name, gw)
    
    def get_opponent_score(self, name, gw):
        return self.get_manager_gw_scores(database_utils.get_opponent(self, name, gw))[gw]
    
    def get_opponent_gws(self, name, opponent):
        return database_utils.get_opponent_gws(self, name, opponent)
    
    def get_gw_scores(self, gw):
        return database_utils.get_gw_scores(self, gw)
        
    def get_z_score(self, manager, gw):
        return database_utils.get_z_score(self, manager, gw)
    
    def get_winning_gw_scores(self, manager):
        return self.get_gw_scores_based_off_result(self, manager, True)
        
    def get_losing_gw_scores(self, manager):
        return self.get_gw_scores_based_off_result(self, manager, False)
    
    def get_gw_scores_based_off_result(self, manager, won):
        results = list()
        
        for gw in range(0, self.get_number_of_gws()):
            manager_score = self.get_gw_score(manager, gw)
            opponent_score = self.get_opponent_score(manager, gw)
            won_gw = manager_score > opponent_score
            if(won and won_gw):
                results.append(manager_score)
            elif(not won and not won_gw):
                results.append(manager_score)
        
        return results
        
    def get_player_id_map(self):
        player_id_data_map = dict()
        for manager in self.get_managers():
            player_db = self.get_manager_player_database(manager)
            for player_data in player_db.get_all_player_data():
                player_id = player_data.get_id()
                if(player_id not in player_id_data_map.keys()):
                    player_id_data_map[player_id] = list()
                player_id_data_map[player_id].append(player_data)
        return player_id_data_map
    
    def was_player_id_drafted(self, manager, player_id):
        manager_index = self.get_managers().index(manager)
        return player_id in self.get_draft_results()[manager_index]