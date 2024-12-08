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
    
    def get_manager_roster_scores(self, name):
        return self._manager_reader.get_manager_roster_scores(name)
        
    def get_manager_gw_scores(self, name):
        return self._manager_reader.get_manager_gw_scores(name)
    
    def get_draft_length(self):
        return self._draft_reader.get_length()
    
    def get_draft_round_player_for(self, name, draft_round):
        return self.get_draft_results()[name][draft_round]
    
    def get_player_data_for(self, name, player_id):
        player_data = self.get_player_data(name)
        for datum in player_data:
            if datum.get_id() == player_id:
                return datum
    
    def get_player_data(self, name):
        return self._manager_reader.get_player_database(name).get_all_player_data()
    
    def get_opponent_gw_scores(self, name):
        opponent_scores = list()
        for gw in range(self.get_number_of_gws()):
            opponent = self.get_opponent(name, gw)
            opponent_scores.append(self.get_gw_score(opponent, gw))
        return opponent_scores
    
    def get_number_of_gws(self):
        return len(self._manager_reader.get_manager_gw_scores(self.get_managers()[0]))
    
    def get_manager_z_score(self, name):
        manager_scores = self.get_manager_gw_scores(name)
        manager_z_scores = list()
        for gw in range(len(manager_scores)):
            gw_scores = self.get_gw_scores(gw)
            manager_z_scores.append(stats_utils.get_z_score(manager_scores[gw], gw_scores))
        return manager_z_scores
    
    def get_opponent_z_score(self, opponent):
        opponent_scores = self.get_opponent_gw_scores(opponent)
        opponent_z_scores = list()
        for gw in range(len(opponent_scores)):
            gw_scores = self.get_gw_scores(gw)
            opponent_z_scores.append(stats_utils.get_z_score(opponent_scores[gw], gw_scores))
        return opponent_z_scores
    
    def get_manager_avg_z_score(self, name):
        return stats_utils.get_mean(self.get_manager_z_score(name))
    
    def get_opponent_avg_z_score(self, opponent):
        return stats_utils.get_mean(self.get_opponent_z_score(opponent))
    
    def get_gw_score(self, name, gw):
        return self.get_manager_gw_scores(name)[gw]
    
    def get_opponent(self, name, gw):
        manager_index = self.get_managers().index(name)
        schedule = self.get_schedules()[manager_index]
        if(gw >= len(schedule)):
            gw = gw % len(schedule)
        opponent_index = schedule[gw]
        return self.get_managers()[opponent_index]
    
    def get_opponent_gws(self, name, opponent):
        gws = list()
        manager_index = self.get_managers().index(name)
        opponent_index = self.get_managers().index(opponent)
        schedule = self.get_schedules()[manager_index]
        gw_step = schedule.index(opponent_index)
        max_head_to_heads = math.ceil(self.get_number_of_gws() / (len(self.get_managers()) - 1))
        for i in range(max_head_to_heads):
            gw = gw_step + (i * (len(self.get_managers()) - 1))
            if(gw > self.get_number_of_gws() - 1):
                break
            gws.append(gw)
        return gws
    
    def get_gw_scores(self, gw):
        gw_data = list()
        for name in self.get_managers():
            gw_data.append(self.get_gw_score(name, gw))
        return gw_data
        
    def get_z_score(self, manager, gw):
        gw_data = self.get_gw_scores(gw)
        score = self.get_gw_score(manager, gw)
        return stats_utils.get_z_score(score, gw_data)
    