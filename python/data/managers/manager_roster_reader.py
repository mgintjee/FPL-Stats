# Add the libraies path to python
import sys
import os
sys.path.append(os.path.join(os.getcwd(), '..\\python\\data'))
sys.path.append(os.path.join(os.getcwd(), '..\\python\\data\\players'))

# Import libraries
import manager_constants
import player_data
import player_database

# Constants
DELIMTER = ";"
MIN_PARTS = 5
ID_INDEX = 0
POSITION_INDEX = 1
KEEPER_VALUE = "G"
ID_PREFIX = "*"
        
def format_player_line(line):
    line = line.rstrip()
    line = line.replace("\",\"", ";")
    line = line.replace("\"", "")
    line = line.replace("\'", "")
    line = line.replace(",", "")
    return line
    
def is_valid(line_parts):
    return len(line_parts) > MIN_PARTS and \
       ID_PREFIX in line_parts[ID_INDEX]

def get_player_database(path_to_data):
    player_db = player_database.player_database()
    for line in open(path_to_data):
        line = format_player_line(line)
        line_parts = line.split(DELIMTER)
        if is_valid(line_parts):
            data = None
            position = line_parts[POSITION_INDEX]
            if position != KEEPER_VALUE:
                data = player_data.player_data(line_parts)
            else:
                data = player_data.player_data(line_parts)
            player_db.add_data(position, data)
    return player_db

class manager_roster_reader:
    def __init__(self, path, name):
        path_to_data = path + "\\" + name + "\\" +\
            manager_constants.ROSTER_SCORES
        self._player_database = get_player_database(path_to_data)
        
    def get_player_database(self):
        return self._player_database