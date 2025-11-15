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
MIN_GW_SCORE = 100
MAX_GW_SCORE = 175
MIN_Z_SCORE = -1
MAX_Z_SCORE = 1
#Constant list of strings to use as headers
MANAGER_Z_SCORE_HEADERS = ["Manager Avg. Z-Score", "Manager Med. Z-Score"]
MANAGER_GW_SCORE_HEADERS = ["Manager Avg. GW-Score", "Manager Med. GW-Score"]
OPPONENT_Z_SCORE_HEADERS = ["Opponent Avg. Z-Score", "Opponent Med. Z-Score"]
OPPONENT_GW_SCORE_HEADERS = ["Opponent Avg. GW-Score", "Opponent Med. GW-Score"]
# Constant strings for the file names to save with
DISPLAY_DATA_FILES = "../export/"
RACE_TO_THE_BOTTOM_FILE = "RaceToTheBottom.csv"
HEAD_TO_HEADS_FILE = "HeadToHeads.csv"
MANAGER_Z_SCORES_FILE = "ManagerZScores.csv"
MANAGER_GW_SCORES_FILE = "ManagerGwScores.csv"
OPPONENT_Z_SCORES_FILE = "OpponentZScores.csv"
OPPONENT_GW_SCORES_FILE = "OpponentGwScores.csv"
# Constant booleans for what actions to run when displaying the data
DEBUG = True
LOG_TO_FILES = True

def get_directory_to_write_to(file_path):
    directory_path = ""

    file_path_parts = file_path.split("/")
    for i in range(len(file_path_parts) - 1):
        directory_path += file_path_parts[i] + "/"

    return directory_path

def log_to_files(file_path, header, data):
    
    print("Logging data to", file_path)
    
    if os.path.exists(file_path): os.remove(file_path)
        
    directory_path = get_directory_to_write_to(file_path)
    if not os.path.exists(directory_path): os.makedirs(directory_path)

    file_to_write_to = open(file_path, "x")
    
    header_to_log = "#HEADER:"  
    for i in range(len(header)):
        header_to_log += str(header[i])
        if i < len(header) - 1: header_to_log += ","
            
    file_to_write_to.write(header_to_log + "\n")
        
    for datum in data:
        data_to_log = datum + ","
        values = data[datum]
            
        for j in range(len(values)):
            data_to_log += str(values[j])
            if j < len(values) - 1: data_to_log += ","
                
        file_to_write_to.write(data_to_log + "\n")
        
    file_to_write_to.close()
    
def display_race_to_the_bottom(db):
    data_to_display = database_formatter.format_race_to_the_bottom(db)
        
    df = pd.DataFrame(data=data_to_display)
    df.head()    
    ax = df.plot(title = db.get_season() + ' Race to the Bottom')
    ax.invert_yaxis()
    plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
    plt.yticks(range(1, len(db.get_managers()) + 1))
    
    if(DEBUG): print(data_to_display)
    if(LOG_TO_FILES): 
        header = list()
        for i in range(1, db.get_number_of_gws() + 1):
            header.append("GW" + str(i))
        log_to_files(DISPLAY_DATA_FILES + str(db.get_season()) + "/" + RACE_TO_THE_BOTTOM_FILE, header, data_to_display)

def display_head_to_heads(db):
    data_to_display = database_formatter.format_head_to_heads(db)
        
    print(db.get_season() + ' Head to Heads')
    
    max_possible_wins = db.get_number_of_gws() / len(db.get_managers())
    new_labels = list()
    
    for name in db.get_managers():
        new_labels.append("Against " + name)
    
    df = pd.DataFrame(data = data_to_display, index = db.get_managers())
    
    display(df.style \
           .format(precision = 0) \
           .background_gradient(axis = None, vmin = 0, vmax = max_possible_wins, cmap = COLOR_MAP) \
           .text_gradient(axis = None, vmin = -1, vmax = -1, cmap = "hot") \
           .relabel_index(new_labels, axis = 0))
    
    if(DEBUG): print(data_to_display)
    if(LOG_TO_FILES): log_to_files(DISPLAY_DATA_FILES + str(db.get_season()) + "/" + HEAD_TO_HEADS_FILE, new_labels, data_to_display)
    
def display_manager_z_scores(db):
    data_to_display = database_formatter.format_manager_z_scores(db)
        
    print(db.get_season() + ' Manager Z-Scores')
        
    df = pd.DataFrame(data = data_to_display, index = MANAGER_Z_SCORE_HEADERS).T
    
    display(df.style \
           .format(precision = 2) \
           .background_gradient(axis = None, vmin = MIN_Z_SCORE, vmax = MAX_Z_SCORE, cmap = COLOR_MAP) \
           .text_gradient(axis = None, vmin = -1, vmax = -1, cmap = "hot"))
    
    if(DEBUG): print(data_to_display)
    if(LOG_TO_FILES): log_to_files(DISPLAY_DATA_FILES + str(db.get_season()) + "/" + MANAGER_Z_SCORES_FILE, MANAGER_Z_SCORE_HEADERS, data_to_display)
    
def display_manager_gw_scores(db):
    data_to_display = database_formatter.format_manager_gw_scores(db)
        
    print(db.get_season() + ' Manager GW-Scores')
        
    df = pd.DataFrame(data = data_to_display, index = MANAGER_GW_SCORE_HEADERS).T
    
    display(df.style \
           .format(precision = 2) \
           .background_gradient(axis = None, vmin = MIN_GW_SCORE, vmax = MAX_GW_SCORE, cmap = COLOR_MAP) \
           .text_gradient(axis = None, vmin = -1, vmax = -1, cmap = "hot"))
    
    if(DEBUG): print(data_to_display)
    if(LOG_TO_FILES): log_to_files(DISPLAY_DATA_FILES + str(db.get_season()) + "/" + MANAGER_GW_SCORES_FILE, MANAGER_GW_SCORE_HEADERS, data_to_display)
    
def display_opponent_z_scores(db):
    data_to_display = database_formatter.format_opponent_z_scores(db)
        
    print(db.get_season() + ' Opponent Z-Scores')
        
    df = pd.DataFrame(data = data_to_display, index = OPPONENT_Z_SCORE_HEADERS).T

    display(df.style \
           .format(precision = 2) \
           .background_gradient(axis = None, vmin = MIN_Z_SCORE, vmax = MAX_Z_SCORE, cmap = plt.cm.get_cmap(COLOR_MAP).reversed()) \
           .text_gradient(axis = None, vmin = -1, vmax = -1, cmap = "hot"))
    
    if(DEBUG): print(data_to_display)
    if(LOG_TO_FILES): log_to_files(DISPLAY_DATA_FILES + str(db.get_season()) + "/" + OPPONENT_Z_SCORES_FILE, OPPONENT_Z_SCORE_HEADERS, data_to_display)
    
def display_opponent_gw_scores(db):
    data_to_display = database_formatter.format_opponent_gw_scores(db)
        
    print(db.get_season() + ' Opponent GW-Scores')
        
    df = pd.DataFrame(data = data_to_display, index = OPPONENT_GW_SCORE_HEADERS).T
    
    display(df.style \
           .format(precision = 2) \
           .background_gradient(axis = None, vmin = MIN_GW_SCORE, vmax = MAX_GW_SCORE, cmap = plt.cm.get_cmap(COLOR_MAP).reversed()) \
           .text_gradient(axis = None, vmin = -1, vmax = -1, cmap = "hot"))
    
    if(DEBUG): print(data_to_display)
    if(LOG_TO_FILES): log_to_files(DISPLAY_DATA_FILES + str(db.get_season()) + "/" + OPPONENT_GW_SCORES_FILE, OPPONENT_GW_SCORE_HEADERS, data_to_display)
    
