# Library dependencies
import numpy as np

# Constants
MEDIAN_PERCENTILE = 50
Q1_PERCENTILE = 25
Q3_PERCENTILE = 75

def get_mean(data):
    return round(np.mean(data), 2)

def get_median(data):
    return np.percentile(data, MEDIAN_PERCENTILE)

def get_q1(data):
    return np.percentile(data, Q1_PERCENTILE)

def get_q3(data):
    return np.percentile(data, Q3_PERCENTILE)

def get_iqr(data):
    return get_q3(data) - get_q1(data)

def get_std(data):
    return round(np.std(data), 2)

def get_z_score(datum, data):
    mean = get_mean(data)
    std = get_std(data)
    diff = datum - mean
    return diff / std

def print_stats(data):
    print("Points:", len(data))
    print("Min   :", min(data))
    print("Max   :", max(data))
    print("Avg   :", get_avg(data))
    print("Median:", get_median(data))
    print("Q1    :", get_q1(data))
    print("Q3    :", get_q3(data))
    print("Iqr   :", get_iqr(data))