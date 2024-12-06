# Add the libraies path to python
import sys
import os
sys.path.append(os.path.join(os.getcwd(), '..\\python\\data' ))

# Import libraries
import draft_constants

# Constants
DELIMITER = ","

def get_schedules(path):
    schedules = dict()
    index = 0
    for line in open(path):
        line_parts = line.rstrip().split(DELIMITER)
        schedule = list()
        for val in line_parts:
            schedule.append(int(val))
        schedules[index] = schedule
        index += 1
    return schedules
        
class draft_schedule_reader:
    def __init__(self, path):
        path_to_data = path + "\\" +\
            draft_constants.SCHEDULE
        self._schedules = get_schedules(path_to_data)
        
    def get_schedules(self):
        return self._schedules