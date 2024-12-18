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
        plot_data.append(database.get_manager_gw_scores(name))        
    fig = matplotlib.pyplot.figure(figsize =(10, 7))
    ax = fig.add_subplot(111)
    bp = ax.boxplot(plot_data, patch_artist = True, vert = 0)
    ax.set_yticklabels(managers)
    matplotlib.pyplot.title("All Manager scores for " + str(number_of_gws) + " GWs")
    matplotlib.pyplot.show()
    
def plot_opponent_performances(database):
    number_of_gws = database.get_number_of_gws()
    plot_data = list()
    managers = database.get_managers()
    for name in managers:
        plot_data.append(database.get_opponent_gw_scores(name))    
    fig = matplotlib.pyplot.figure(figsize =(10, 7))
    ax = fig.add_subplot(111)
    bp = ax.boxplot(plot_data, patch_artist = True, vert = 0)
    ax.set_yticklabels(managers)
    matplotlib.pyplot.title("All Opponent scores for " + str(number_of_gws) + " GWs")
    matplotlib.pyplot.show()
    
def plot_gw_performances(database):
    number_of_gws = database.get_number_of_gws()
    plot_data = list()
    gws = reversed(range(1, number_of_gws+1))
    for gw in reversed(range(number_of_gws)):
        plot_data.append(database.get_gw_scores(gw))    
    fig = matplotlib.pyplot.figure(figsize =(10, 7))
    ax = fig.add_subplot(111)
    bp = ax.boxplot(plot_data, patch_artist = True, vert = 0)
    ax.set_yticklabels(gws)
    matplotlib.pyplot.title("All GW scores for " + str(number_of_gws) + " GWs")
    matplotlib.pyplot.show()
