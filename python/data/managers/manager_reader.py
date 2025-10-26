# Add the libraies path to python
import sys
import os
sys.path.append(os.path.join(os.getcwd(), '..\\python\\data' ))

# Import libraries
import data_constants
import manager_constants
import manager_gw_reader
import manager_roster_reader
import manager_activity_reader

def get_managers(path_to_data):
    managers = list()
    for file in os.listdir(path_to_data):
        if('.' not in file and file != "transactions"):
            managers.append(file)
    return managers
        
class manager_reader:
    def __init__(self, path):
        path_to_data = path + "\\" +\
            data_constants.MANAGERS
        self._managers = get_managers(path_to_data)
        self._manager_gw_readers = dict()
        self._manager_roster_readers = dict()
        self._manager_activity_readers = dict()
        
        for name in self._managers:
            self._manager_roster_readers[name] = manager_roster_reader.manager_roster_reader(path_to_data, name)
            self._manager_gw_readers[name] = manager_gw_reader.manager_gw_reader(path_to_data, name)
            self._manager_activity_readers[name] = manager_activity_reader.manager_activity_reader(path_to_data, name)
            
    def get_managers(self):
        return self._managers
    
    def get_manager_gw_scores(self, name):
        return self._manager_gw_readers[name].get_gw_scores()
    
    def get_player_database(self, name):
        return self._manager_roster_readers[name].get_player_database()
    
    def get_manager_activity_reader(self, name):
        return self._manager_activity_readers[name]