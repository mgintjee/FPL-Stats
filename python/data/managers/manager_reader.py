# Add the libraies path to python
import sys
import os
sys.path.append(os.path.join(os.getcwd(), '..\\python\\data' ))

# Import libraries
import data_constants
import manager_constants
import manager_gw_reader
import manager_roster_reader

def get_managers(path_to_data):
    managers = list()
    for file in os.listdir(path_to_data):
        managers.append(file)
    return managers
        
class manager_reader:
    def __init__(self, path):
        path_to_data = path + "\\" +\
            data_constants.MANAGERS
        self._managers = get_managers(path_to_data)
        self._manager_gw_readers = dict()
        self._manager_roster_readers = dict()
        
        for name in self._managers:
            path_to_manager_data = path_to_data + "\\" + name
            self._manager_gw_readers[name] = manager_gw_reader.manager_gw_reader(path_to_manager_data)
            self._manager_roster_readers[name] = manager_roster_reader.manager_roster_reader(path_to_manager_data)
            
    def get_managers(self):
        return self._managers
    
    def get_manager_gw_scores(self, name):
        return self._manager_gw_readers[name].get_gw_scores()
    
    def get_manager_roster_scores(self, name):
        return self._manager_roster_readers[name].get_roster_scores()