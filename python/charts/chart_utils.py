#Constants
UNSET     = "\033[0;49;39m"
PURPLE     = "\033[0;49;35m"
RED        = "\033[0;49;31m"
YELLOW     = "\033[0;49;33m"
GREEN      = "\033[0;49;32m"
BLUE       = "\033[0;49;34m"
CLEAR      = "\033[0;0m"

AVG_Z_SCORE_HORRIBLE = -0.5
AVG_Z_SCORE_TERRIBLE = -0.25
AVG_Z_SCORE_BAD = 0
AVG_Z_SCORE_AVERAGE = 0.25
AVG_Z_SCORE_GOOD = 0.5

Z_SCORE_HORRIBLE = -1.5
Z_SCORE_TERRIBLE = -.5
Z_SCORE_BAD = 0
Z_SCORE_AVERAGE = 0.5
Z_SCORE_GOOD = 1.5

RED_RATIO = 0.4
YELLOW_RATIO = 0.6
#GREEN_RATIO = 0.4

def get_colored_win_ratio(wins, total):
    color = CLEAR
    win_ratio = wins / total
    if(win_ratio < RED_RATIO):
        color = RED
    elif(win_ratio < YELLOW_RATIO):
        color = YELLOW
    else:
        color = GREEN
    return color + str(wins) + "/" + str(total) + CLEAR


def get_color_for_avg_z_score(std_value, flip):
    
    invert = 1
    if(flip):
        invert = -1
        
    comparing_value = std_value * invert
    
    color = UNSET
    if(comparing_value <= AVG_Z_SCORE_HORRIBLE):
        color = PURPLE
    elif(comparing_value < AVG_Z_SCORE_TERRIBLE):
        color = RED
    elif(comparing_value < AVG_Z_SCORE_BAD):
        color = YELLOW
    elif(comparing_value < AVG_Z_SCORE_AVERAGE):
        color = CLEAR
    elif(comparing_value < AVG_Z_SCORE_GOOD):
        color = GREEN
    elif(comparing_value >= AVG_Z_SCORE_GOOD):
        color = BLUE        
    return color + str(std_value) + CLEAR

def get_color_for_z_score(std_value, flip):
    
    invert = 1
    if(flip):
        invert = -1
        
    comparing_value = std_value * invert
    
    color = UNSET
    if(comparing_value <= Z_SCORE_HORRIBLE):
        color = PURPLE
    elif(comparing_value < Z_SCORE_TERRIBLE):
        color = RED
    elif(comparing_value < Z_SCORE_BAD):
        color = YELLOW
    elif(comparing_value < Z_SCORE_AVERAGE):
        color = CLEAR
    elif(comparing_value < Z_SCORE_GOOD):
        color = GREEN
    elif(comparing_value >= Z_SCORE_GOOD):
        color = BLUE        
    return color + str(std_value) + CLEAR