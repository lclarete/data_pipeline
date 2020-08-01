# functions to calculate Empirical Cumulative Distribution Function
# based on a datacamp tutorial: https://campus.datacamp.com/courses/statistical-thinking-in-python-part-1/graphical-exploratory-data-analysis?ex=11

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def ecdf_save_image(data, xlabel):
    # importing seaborn style
    sns.set()
    # calculating the number of data elements
    n = len(data)
    # sort the data
    x_vers = np.sort(data)
    # creating the y label with an axis with the proportion of each element
    y_vers = np.arange(1, n+1)/n
    # creating the chart
    _ = plt.plot(x_vers, y_vers, marker=".", linestyle="none")
    # naming the labels 
    x = plt.xlabel(xlabel)
    y = plt.ylabel("OCDF")
    # exporting the image to a png file
    plt.savefig(str(xlabel+".png"))
    return(plt.show())

def ecdf(data):
    sns.set()
    n = len(data)
    x = np.sort(data)
    y = np.arange(1, n+1)/n
    _ = plt.plot(x, y, marker=".", linestyle="none")
    # naming the labels 
    _ = plt.ylabel("ECDF")
    return(_)