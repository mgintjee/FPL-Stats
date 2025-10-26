# Constants
ID_INDEX = 0
POSITION_INDEX = 1
NAME_INDEX = 2
TEAM_INDEX = 3
STATUS_INDEX = 5
POINTS_INDEX = 7
POINTS_PER_GAME_INDEX = 8
GAMES_PLAYED_INDEX = 9
MIN_INDEX = 10
GOALS_INDEX = 11
ASSISTS_INDEX = 12
SHOTS_ON_TARGETS_INDEX = 13
TACKLES_INDEX = 14
DISPOSSESSED_INDEX = 15
YELLOW_CARD_INDEX = 16
RED_CARD_INDEX = 17
ACCURATE_CROSS_INDEX = 18
INTERCEPTION_INDEX = 19
CLEARANCE_INDEX = 20
DRIBBLES_INDEX = 21
BLOCKED_SHOT_INDEX = 22
AERIALS_INDEX = 23
PK_MISSED_INDEX = 24
PK_DRAWN_INDEX = 25
OWN_GOALS_INDEX = 26
GOALS_AGAINST_INDEX = 27
CLEAN_SHEET_INDEX = 28

class player_data:
    def __init__(self, data_parts):
        self._id = data_parts[ID_INDEX]
        self._position = data_parts[POSITION_INDEX]
        self._name = data_parts[NAME_INDEX]
        self._team = data_parts[TEAM_INDEX]
        self._status = data_parts[STATUS_INDEX]
        self._points = float(data_parts[POINTS_INDEX])
        self._ppg = float(data_parts[POINTS_PER_GAME_INDEX])
        self._games = int(data_parts[GAMES_PLAYED_INDEX])
        self._min = int(data_parts[MIN_INDEX].replace(",", ""))
        self._goals = int(data_parts[GOALS_INDEX])
        self._assists = int(data_parts[ASSISTS_INDEX])
        self._shots = int(data_parts[SHOTS_ON_TARGETS_INDEX])
        self._tackles = int(data_parts[TACKLES_INDEX])
        self._dispossessions = int(data_parts[DISPOSSESSED_INDEX])
        self._yellow_cards = int(data_parts[YELLOW_CARD_INDEX])
        self._red_cards = int(data_parts[RED_CARD_INDEX])
        self._crosses = int(data_parts[ACCURATE_CROSS_INDEX])
        self._interceptions = int(data_parts[INTERCEPTION_INDEX])
        self._clearances = int(data_parts[CLEARANCE_INDEX])
        self._dribbles = int(data_parts[DRIBBLES_INDEX])
        self._blocked_shots = int(data_parts[BLOCKED_SHOT_INDEX])
        self._aerials = int(data_parts[AERIALS_INDEX])
        self._pk_missed = int(data_parts[PK_MISSED_INDEX])
        self._pk_drawn = int(data_parts[PK_DRAWN_INDEX])
        self._own_goals = int(data_parts[OWN_GOALS_INDEX])
        self._goals_against = int(data_parts[GOALS_AGAINST_INDEX])
        self._clean_sheet = int(data_parts[CLEAN_SHEET_INDEX])
    
    def get_id(self):
        return self._id;
    
    def is_free_agent(self):
        return self._status == "-"
        
    def get_position(self):
        return self._position;
        
    def get_name(self):
        return self._name;
        
    def get_team(self):
        return self._team;
        
    def get_points(self):
        return self._points;
        
    def get_ppg(self):
        return self._ppg;
        
    def get_games(self):
        return self._games;
        
    def get_min(self):
        return self._min;
        
    def get_goals(self):
        return self._goals;
        
    def get_assists(self):
        return self._assists;
        
    def get_shots(self):
        return self._shots;
        
    def get_tackles(self):
        return self._tackles;
        
    def get_dispossessions(self):
        return self._dispossessions;
        
    def get_yellow_cards(self):
        return self._yellow_cards;
        
    def get_red_cards(self):
        return self._red_cards;
        
    def get_crosses(self):
        return self._crosses;
        
    def get_interceptions(self):
        return self._interceptions;
        
    def get_clearances(self):
        return self._clearances;
        
    def get_dribbles(self):
        return self._dribbles;
        
    def get_blocked_shots(self):
        return self._blocked_shots;
        
    def get_aerials(self):
        return self._aerials;
        
    def get_pk_missed(self):
        return self._pk_missed;
        
    def get_pk_drawn(self):
        return self._pk_drawn;
        
    def get_own_goals(self):
        return self._own_goals;
        
    def get_goals_against(self):
        return self._goals_against;
        
    def get_clean_sheet(self):
        return self._clean_sheet;
        