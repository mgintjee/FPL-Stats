# Add the libraies path to python
import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
sys.path.append(os.path.join(os.getcwd(), '..\\python\\data'))
sys.path.append(os.path.join(os.getcwd(), '..\\python\\data\\common'))
sys.path.append(os.path.join(os.getcwd(), '..\\python\\database'))

# Import libraries
import matplotlib.pyplot
import database_formatter
from IPython.display import display, HTML

#Constants
MANAGER_KEY = "Manager"
PICKUP_PLAYER_IMPACT_KEY = "Most Impactful Player (Pick-up)"
DRAFT_PLAYER_IMPACT_KEY = "Most Impactful Player (Drafted)"
CONTRIBUTION_KEY = "% Contribution"
TOTAL_POINTS_KEY = "Total Points"
TOTAL_MINUTES_KEY = "Total Minutes"
POINTS_PER_90_KEY = "Points Per 90"
COLOR_MAP = "RdYlGn"
DEBUG = False
MIN_GW_SCORE = 100
MAX_GW_SCORE = 175
MIN_Z_SCORE = -1
MAX_Z_SCORE = 1

def get_team_from(team):
    if "/" in team:
        team_parts = team.split("/")
        return team_parts[len(team_parts) - 1]
    else:
        return team
    
def display_race_to_the_bottom(db):
    data_to_display = database_formatter.format_race_to_the_bottom(db)
    if(DEBUG): print(data_to_display)
    df = pd.DataFrame(data=data_to_display)
    df.head()    
    ax = df.plot(title = db.get_season() + ' Race to the Bottom')
    ax.invert_yaxis()
    plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
    plt.yticks(range(1, len(db.get_managers()) + 1))

def display_head_to_heads(db):
    data_to_display = database_formatter.format_head_to_heads(db)
    if(DEBUG): print(data_to_display)
    
    max_possible_wins = db.get_number_of_gws() / len(db.get_managers())
    new_labels = list()
    
    for name in db.get_managers():
        new_labels.append("Against " + name)
    
    df = pd.DataFrame(data = data_to_display, index = db.get_managers())
    
    display(df.style \
           .set_caption(db.get_season() + " Head to Heads") \
           .format(precision = 0) \
           .background_gradient(axis = None, vmin = 0, vmax = max_possible_wins, cmap = COLOR_MAP) \
           .text_gradient(axis = None, vmin = -1, vmax = -1, cmap = "hot") \
           .relabel_index(new_labels, axis = 0))
    
def display_manager_z_scores(db):
    data_to_display = database_formatter.format_manager_z_scores(db)
    if(DEBUG): print(data_to_display)
        
    df = pd.DataFrame(data = data_to_display, index = ["Average", "Median"])
    
    display(df.style \
           .set_caption(db.get_season() + " Manager Z-Scores") \
           .format(precision = 2) \
           .background_gradient(axis = None, vmin = MIN_Z_SCORE, vmax = MAX_Z_SCORE, cmap = COLOR_MAP) \
           .text_gradient(axis = None, vmin = -1, vmax = -1, cmap = "hot"))
    
def display_manager_gw_scores(db):
    data_to_display = database_formatter.format_manager_gw_scores(db)
    if(DEBUG): print(data_to_display)
        
    df = pd.DataFrame(data = data_to_display, index = ["Average", "Median"])
    
    display(df.style \
           .set_caption(db.get_season() + " Manager Scores") \
           .format(precision = 2) \
           .background_gradient(axis = None, vmin = MIN_GW_SCORE, vmax = MAX_GW_SCORE, cmap = COLOR_MAP) \
           .text_gradient(axis = None, vmin = -1, vmax = -1, cmap = "hot"))
    
def display_opponent_z_scores(db):
    data_to_display = database_formatter.format_opponent_z_scores(db)
    if(DEBUG): print(data_to_display)
        
    df = pd.DataFrame(data = data_to_display, index = ["Average", "Median"])

    display(df.style \
           .set_caption(db.get_season() + " Opponent Z-Scores") \
           .format(precision = 2) \
           .background_gradient(axis = None, vmin = MIN_Z_SCORE, vmax = MAX_Z_SCORE, cmap = plt.cm.get_cmap(COLOR_MAP).reversed()) \
           .text_gradient(axis = None, vmin = -1, vmax = -1, cmap = "hot"))
    
def display_opponent_gw_scores(db):
    data_to_display = database_formatter.format_opponent_gw_scores(db)
    if(DEBUG): print(data_to_display)
        
    df = pd.DataFrame(data = data_to_display, index = ["Average", "Median"])
    
    display(df.style \
           .set_caption(db.get_season() + " Opponent Scores") \
           .format(precision = 2) \
           .background_gradient(axis = None, vmin = MIN_GW_SCORE, vmax = MAX_GW_SCORE, cmap = plt.cm.get_cmap(COLOR_MAP).reversed()) \
           .text_gradient(axis = None, vmin = -1, vmax = -1, cmap = "hot"))
    
