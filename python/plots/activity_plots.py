# Add the libraies path to python
import sys
import os
sys.path.append(os.path.join(os.getcwd(), '..\\python\\data'))
sys.path.append(os.path.join(os.getcwd(), '..\\python\\data\\common'))

# Import libraries
import matplotlib.pyplot

def plot_manager_activity_lineup_changes(database):
    number_of_gws = database.get_number_of_gws()
    managers = database.get_managers()
    manager_activity = dict()
    for name in managers:
        manager_activity[name] = list()
    x_axis = list()
    for gw in range(number_of_gws):
        x_axis.append(gw + 1)
        for name in managers:
            if(gw > 0):
                print()
            else:
                manager_activity[name].append()
            
            
    plot_data = list()
    plot_data.append(database.get_manager_gw_scores(name))        
    fig = matplotlib.pyplot.figure(figsize =(10, 7))
    ax = fig.add_subplot(111)
    bp = ax.boxplot(plot_data, patch_artist = True, vert = 0)
    ax.set_yticklabels(managers)
    matplotlib.pyplot.xlabel("Scores")
    matplotlib.pyplot.ylabel("Managers")
    matplotlib.pyplot.title("All Manager scores for " + str(number_of_gws) + " GWs")
    matplotlib.pyplot.show()