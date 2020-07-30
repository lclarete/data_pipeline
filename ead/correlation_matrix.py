import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def correlation_matrix(df, figsize=(11,9)):
    # define the correlation matrix
    corr = df.corr()
    # create a mask of boolean values
    mask = np.triu(np.ones_like(corr, dtype=np.bool))
    # define the subplots
    f, ax = plt.subplots(figsize=(figsize))
    # define the colors
    cmap = sns.diverging_palette(220, 10, as_cmap=True)
    #plot the heatmap
    sns.heatmap(corr, 
                annot=True, 
                cmap=cmap,
                mask=mask, 
                linewidth=1.5, 
                cbar_kws={"shrink": .5}
    );
    return plt.show()