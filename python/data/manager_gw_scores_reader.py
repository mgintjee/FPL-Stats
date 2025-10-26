import os
import data_constants
import manager_constants
import manager_data
from pathlib import Path

def get_season_data_from(path):
    all_gw_data = list()
    for file in os.listdir(path):
        if os.fsdecode(file).endswith(".score"):
            name = Path(file).stem
            gw_data = get_manager_data_from(path + "\\" + file)
            all_gw_data.append(manager_data.manager_data(name, gw_data))
    return all_gw_data

def get_manager_data_from(path):
    gw_data = list()
    for line in open(path):
        gw_data.append(float(line.rstrip()))
    return gw_data
    
class manager_gw_scores_reader:
    def __init__(self, season, manager):
        print("Building manager gw scores reader for", manager, " during season", season)
        self.path_to_data = os.getcwd() + "\\" +\
            data_constants.DATA + "\\" +\
            data_constants.SEASONS + "\\" +\
            season + "\\" +\
            data_constants.MANAGERS + "\\" +\
            manager + "\\" +\
            manager_constants.GW_SCORES
        print(self.path_to_data)
    
    def get_data(self):
        return self.season_data