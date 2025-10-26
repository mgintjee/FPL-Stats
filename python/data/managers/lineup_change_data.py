class lineup_change_data:
    def __init__(self, line):
        line = line.replace("\"", '')
        line_parts = line.split(",")
        self.name = line_parts[0]
        self.team = line_parts[1]
        self.position = line_parts[2]
        self.target = line_parts[3]
        self.gw = int(line_parts[9])
        
    def get_name(self):
        return self.name
    
    def get_team(self):
        return self.team
    
    def get_position(self):
        return self.position
    
    def get_target(self):
        return self.target
    
    def get_gw(self):
        return self.gw
    