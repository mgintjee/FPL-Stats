import os
import manager_data
from pathlib import Path

DRAFT_ORDER = "\\draft_order.txt"
SCHEDULE = "\\schedule.txt"

def get_schedules_for(path):
    manager_schedules = dict()
    index = 0
    for line in open(path):
        line_parts = line.rstrip().split(',')
        schedule = list()
        for val in line_parts:
            schedule.append(int(val))
        manager_schedules[index] = schedule
        index += 1
    return manager_schedules

def get_managers(path):
    managers = list()
    for line in open(path):
        managers.append(line.rstrip())
    return managers
    
class schedule_reader:
    def __init__(self, year):
        print("Initializing schedule reader for year: " + year)
        path_to_draft_order = os.getcwd() + "\\data\\seasons\\" + year + DRAFT_ORDER
        self.managers = get_managers(path_to_draft_order)
        path_to_schedule = os.getcwd() + "\\data\\seasons\\" + year + SCHEDULE
        self.manager_schedules = get_schedules_for(path_to_schedule)
        print("Draft Order:", self.managers)
    
    def get_managers(self):
        return self.managers
    
    def get_manager_schedules(self):
        return self.manager_schedules