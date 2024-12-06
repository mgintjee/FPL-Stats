# Add the libraies path to python
import sys
import os
sys.path.append(os.path.join(os.getcwd(), '..\\python\\data'))
sys.path.append(os.path.join(os.getcwd(), '..\\python\\data\\common'))

# Import libraries
import draft_constants
import player_data

# Constants
DELIMITER = ","
ROUND_PICK_INDEX = 1
OVERALL_PICK_INDEX = 3
PLAYER_ID_INDEX = 0

def get_manager(overall_pick, round_length):
    managers = list()
    for i in range(round_length):
        managers.append(i)
    round_remainder = overall_pick % round_length
    round_index = int(overall_pick / round_length)
    is_snaked = round_index % 2 != 0
    index = round_remainder
    if(is_snaked):
        index = round_length - 1 - round_remainder
    return managers[index]
        
def get_results(path_to_data, manager_count):
    results = dict()
    
    for i in range(manager_count):
        results[i] = list()
    # Skip the file's header
    skip_first = True
    for line in open(path_to_data):
        if skip_first:
            skip_first = False
            continue
        line_parts = line.split(DELIMITER)
        round_pick = int(line_parts[ROUND_PICK_INDEX])
        overall_pick = int(line_parts[OVERALL_PICK_INDEX]) - 1
        player_id = line_parts[PLAYER_ID_INDEX]
        manager = get_manager(overall_pick, manager_count)
        results[manager].append(player_id)
    return results
    
class draft_results_reader:
    def __init__(self, path, manager_count):
        path_to_data = path + "\\" +\
            draft_constants.RESULTS
        self._results = get_results(path_to_data, manager_count)
    
    def get_results(self):
        return self._results