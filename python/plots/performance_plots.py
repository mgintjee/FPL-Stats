# Add the libraies path to python
import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
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

def plot_race_to_the_bottom(db):
    number_of_gws = db.get_number_of_gws()
    managers = db.get_managers()

    manager_rank_scores = dict()
    manager_ranks_over_time = dict()

    for name in managers:
        manager_ranks_over_time[name] = list()
        manager_rank_scores[name] = list()
        manager_scores = db.get_manager_gw_scores(name)

        for gw in range(number_of_gws):
            if(gw == 0):
                rank_score = 0
            else:
                rank_score = manager_rank_scores[name][gw - 1]
            manager_score = db.get_gw_score(name, gw)
            opponent_score = db.get_opponent_score(name, gw)

            # Calculate the result score
            result_score = 30000 if manager_score > opponent_score else 10000 if manager_score == opponent_score else 0
            rank_score += result_score + manager_score
            manager_rank_scores[name].append(rank_score)

    for gw in range(number_of_gws):
        manager_rank_scores_for_gw = dict()

        for name in managers:
            manager_rank_scores_for_gw[name] = manager_rank_scores[name][gw]

        manager_ranks_for_gw = sorted(manager_rank_scores_for_gw.items(), key=lambda item: item[1])
        manager_ranks = list()
        for sorted_managers in manager_ranks_for_gw:
            name = sorted_managers[0]
            manager_ranks.append(name)

        for name in managers:
            manager_ranks_over_time[name].append(manager_ranks.index(name))

    df = pd.DataFrame(data=manager_ranks_over_time)
    df.head()    
    df.plot(title = db.get_season() + ' Race to the Bottom')
    plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))