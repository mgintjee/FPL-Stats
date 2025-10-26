# Add the libraies path to python
import sys
import os
sys.path.append(os.path.join(os.getcwd(), '..\\python\\data' ))

# Import libraries
import manager_constants
    
def get_gw_scores(path_to_data, name):
    gw_scores = list()
    for line in open(path_to_data):
        if( name in line ):
            line_parts = line.split("\t")
            if(line_parts[0].rstrip() == name):
                line_part = line_parts[1]
            else:
                line_part = line_parts[3]
            value = round(float(line_part.rstrip()), 2)
            gw_scores.append(value)
    return gw_scores
    
        
class manager_gw_reader:
    def __init__(self, path, name):
        path_to_data = path + "\\" +\
            manager_constants.GW_SCORES
        self._gw_scores = get_gw_scores(path_to_data, name)
        
    def get_gw_scores(self):
        return self._gw_scores