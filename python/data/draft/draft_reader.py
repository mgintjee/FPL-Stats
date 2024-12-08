# Add the libraies path to python
import sys
import os
sys.path.append(os.path.join(os.getcwd(), '..\\\python\\data' ))

# Import libraries
import data_constants
import draft_order_reader
import draft_results_reader
import draft_schedule_reader

class draft_reader:
    def __init__(self, path):
        path_to_data = path + "\\" +\
            data_constants.DRAFT
        self._draft_schedule_reader = draft_schedule_reader.draft_schedule_reader(path_to_data)
        self._draft_order_reader = draft_order_reader.draft_order_reader(path_to_data)
        self._draft_results_reader = draft_results_reader.draft_results_reader(path_to_data, len(self.get_order()))
        
    def get_order(self):
        return self._draft_order_reader.get_order()
    
    def get_schedules(self):
        return self._draft_schedule_reader.get_schedules()  
    
    def get_results(self):
        return self._draft_results_reader.get_results()
    
    def get_length(self):
        return self._draft_results_reader.get_length()