# Import libraries
import player_constants

class player_database:
    def __init__(self):
        self._position_data = dict()
        for value in player_constants.POSITIONS:
            self._position_data[value] = list()
    
    def get_position_data(self, position):
        return self._position_data[position]
    
    def get_all_player_data(self):
        data = list()
        for position in self._position_data.keys():
            data.extend(self._position_data[position])
        return data
    
    def get_keeper_data(self, position):
        return self._position_data[player_constants.KEEPER]
    
    def get_player_data(self, player_id):
        for data in self._position_data.values():
            for datum in data:
                if datum.get_id() == player_id:
                    return data
    
    def add_data(self, position, data):
        self._position_data[position].append(data)