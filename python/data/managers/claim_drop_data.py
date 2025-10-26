class claim_drop_data:
    def __init__(self, line):
        line = line.replace("\"", '')
        line_parts = line.split(",")
        self.name = line_parts[0]
        self.team = line_parts[1]
        self.position = line_parts[2]
        self.claimed = "Claim" in line
        self.gw = int(line_parts[10])
        
    def get_name(self):
        return self.name
    
    def get_team(self):
        return self.team
    
    def get_position(self):
        return self.position
    
    def is_claim(self):
        return self.claimed
    
    def get_gw(self):
        return self.gw
    