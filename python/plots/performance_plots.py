# Add the libraies path to python
import sys
import os
sys.path.append(os.path.join(os.getcwd(), '..\\python\\data'))
sys.path.append(os.path.join(os.getcwd(), '..\\python\\data\\common'))

# Import libraries
import matplotlib.pyplot

def plot_manager_performances(database):
    number_of_gws = database.get_number_of_gws()
    plot_data = list()
    managers = database.get_managers()
    for name in managers:
        plot_data.append(database.get_manager_z_scores(name))        
    fig = matplotlib.pyplot.figure(figsize =(10, 7))
    ax = fig.add_subplot(111)
    bp = ax.boxplot(plot_data, patch_artist = True, vert = 0)
    ax.set_yticklabels(managers)
    matplotlib.pyplot.xlabel("Z-Scores")
    matplotlib.pyplot.ylabel("Managers")
    matplotlib.pyplot.title("All Manager performances for " + str(number_of_gws) + " GWs")
    matplotlib.pyplot.show()
    
def plot_opponent_performances(database):
    number_of_gws = database.get_number_of_gws()
    plot_data = list()
    managers = database.get_managers()
    for name in managers:
        plot_data.append(database.get_opponent_z_scores(name))    
    fig = matplotlib.pyplot.figure(figsize =(10, 7))
    ax = fig.add_subplot(111)
    bp = ax.boxplot(plot_data, patch_artist = True, vert = 0)
    ax.set_yticklabels(managers)
    matplotlib.pyplot.xlabel("Z-Scores")
    matplotlib.pyplot.ylabel("Managers")
    matplotlib.pyplot.title("All Opponent performances for " + str(number_of_gws) + " GWs")
    matplotlib.pyplot.show()
    
def plot_gw_performances(database):
    number_of_gws = database.get_number_of_gws()
    plot_data = list()
    gws = reversed(range(1, number_of_gws+1))
    for gw in reversed(range(number_of_gws)):
        plot_data.append(database.get_gw_z_scores(gw))    
    fig = matplotlib.pyplot.figure(figsize =(10, 7))
    ax = fig.add_subplot(111)
    bp = ax.boxplot(plot_data, patch_artist = True, vert = 0)
    ax.set_yticklabels(gws)
    matplotlib.pyplot.xlabel("Z-Scores")
    matplotlib.pyplot.ylabel("GWs")
    matplotlib.pyplot.title("All GW performances for " + str(number_of_gws) + " GWs")
    matplotlib.pyplot.show()
