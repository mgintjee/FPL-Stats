# Add the libraies path to python
import sys
import os
sys.path.append(os.path.join(os.getcwd(), '..\\python\\data' ))

# Import libraries
import manager_constants
    
def get_gw_scores(path_to_data):
    gw_scores = list()
    for line in open(path_to_data):
        gw_scores.append(round(float(line.rstrip()), 2))
    return gw_scores
    
        
class manager_gw_reader:
    def __init__(self, path):
        path_to_data = path + "\\" +\
            manager_constants.GW_SCORES
        self._gw_scores = get_gw_scores(path_to_data)
        
    def get_gw_scores(self):
        return self._gw_scores