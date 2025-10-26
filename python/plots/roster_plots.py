# Add the libraies path to python
import sys
import os
sys.path.append(os.path.join(os.getcwd(), '..\\python\\data'))
sys.path.append(os.path.join(os.getcwd(), '..\\python\\data\\common'))
sys.path.append(os.path.join(os.getcwd(), '..\\python\\data\\players'))

# Import libraries
import matplotlib.pyplot
import player_constants
import math

def plot_roster_scores_by_team_for(database, name):
    player_data = database.get_player_data(name)    
    team_points = dict()
    total = 0
    
    for datum in player_data:
        if datum == None:
            continue
            
        team = datum.get_team()
        if "/" in team:
            team_parts = team.split("/")
            team = team_parts[len(team_parts) - 1]
        if team not in team_points.keys():
            team_points[team] = 0
        points = datum.get_points()
        team_points[team] = team_points[team] + points
        total += points
    
    plot_data = dict()    
    for value in team_points.keys():
        plot_data[value] = team_points[value] / total * 100
    
    x_values = list(plot_data.keys())
    y_values = list(plot_data.values())
    
    fig = matplotlib.pyplot.figure(figsize = (10, 5))
    matplotlib.pyplot.xticks(rotation=45)
    matplotlib.pyplot.bar(x_values, y_values)
    matplotlib.pyplot.xlabel("Team")
    matplotlib.pyplot.ylabel("Points Contribution %")
    matplotlib.pyplot.title(name + "'s Team Point Contributions")
    matplotlib.pyplot.show()
    
def plot_roster_scores_by_position_for(database, name):
    player_data = database.get_player_data(name)
    positional_points = dict()
    total = 0
    
    for datum in player_data:
        if datum == None:
            continue
            
        position = datum.get_position()
        if position not in positional_points.keys():
            positional_points[position] = 0
        points = datum.get_points()
        positional_points[position] = positional_points[position] + points
        total += points
    
    plot_data = dict()    
    for value in positional_points.keys():
        plot_data[value] = positional_points[value] / total * 100
    
    x_values = list(plot_data.keys())
    y_values = list(plot_data.values())
    
    fig = matplotlib.pyplot.figure(figsize = (10, 5))
    matplotlib.pyplot.bar(x_values, y_values)
    matplotlib.pyplot.xlabel("Position")
    matplotlib.pyplot.ylabel("Points Contribution %")
    matplotlib.pyplot.title(name + "'s Positional Point Contributions")
    matplotlib.pyplot.show()
    
def plot_roster_scores_by_position(database):
    for name in database.get_managers():
        plot_roster_scores_by_position_for(database, name)
        
def plot_roster_scores_by_team(database):
    for name in database.get_managers():
        plot_roster_scores_by_team_for(database, name)