# Add the libraies path to python
import sys
import os
sys.path.append(os.path.join(os.getcwd(), '..\\python\\data' ))

# Import libraries
import draft_constants
        
def get_order(path_to_data):
    order = list()
    for file in open(path_to_data):
        order.append(file.rstrip())
    return order

class draft_order_reader:
    def __init__(self, path):
        path_to_data = path + "\\" +\
            draft_constants.ORDER
        self._order = get_order(path_to_data)
        
    def get_order(self):
        return self._order