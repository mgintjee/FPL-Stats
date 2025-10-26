# Add the libraies path to python
import sys
import os
sys.path.append(os.path.join(os.getcwd(), '..\\python\\data' ))

# Import libraries
import manager_constants
import transactions_constants
import lineup_change_data
import claim_drop_data

def get_lineup_changes(path_to_data, name):
    lineup_changes = dict()
    
    for line in open(path_to_data):
        if(name in line):
            lineup_change = lineup_change_data.lineup_change_data(line.rstrip())
            gw = lineup_change.get_gw() 
            
            if(gw not in lineup_changes):
                lineup_changes[gw] = list()
                
            lineup_changes[gw].append(lineup_change)
            
    return lineup_changes

def get_claims_drops(path_to_data, name):
    claims_drops = dict()
    
    for line in open(path_to_data):
        if(name in line):
            claim_drop = claim_drop_data.claim_drop_data(line.rstrip())
            gw = claim_drop.get_gw() 
            if(gw not in claims_drops):
                claims_drops[gw] = list()
            claims_drops[gw].append(claim_drop)
    
    return claims_drops

class manager_activity_reader:
    def __init__(self, path, name):
        path_to_transactions = path + "\\" + transactions_constants.TRANSACTIONS_FOLDER 
        self._lineup_changes = get_lineup_changes(path_to_transactions + "\\" + transactions_constants.LINEUP_CHANGES_FILE, name)
        self._claims_drops= get_claims_drops(path_to_transactions + "\\" + transactions_constants.CLAIMS_DROPS_FILE, name)
        
    def get_lineup_changes(self):
        return self._lineup_changes
    
    def get_claims_drops(self):
        return self._claims_drops