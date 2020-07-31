import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

def histogram(data):
    sns.set()
    n_bins = int(np.sqrt(len(data)))
    _ = plt.hist(data, bins=n_bins)
    _ = plt.ylabel("count")
    return(_)

def histogram_porcentage(data):
    sns.set()
    data = pd.DataFrame(data)
    if float(data.loc[1][0]) is float:
        n_bins = int(np.sqrt(len(data)))
    else: 
        data = pd.DataFrame(data)
        n_bins = len(data[0].value_counts())
    _ = plt.hist(data, bins=n_bins)
    _ = plt.ylabel("count")
    return(_, n_bins)