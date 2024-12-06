# Add the libraies path to python
import sys
import os
sys.path.append(os.path.join(os.getcwd(), '..\\python\\data' ))

# Import libraries
import manager_constants
        
class manager_roster_reader:
    def __init__(self, path):
        path_to_data = path + "\\" +\
            manager_constants.ROSTER_SCORES