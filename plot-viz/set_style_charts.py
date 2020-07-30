import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams

# set the chart's style, whitegrid as a default
def set_style(style='whitegrid'):
    '''Set new style'''

    sns.set_style(style)

    # define the chart size
    rcParams['figure.figsize'] = [15,7]

    # despine charts
    plt.rc('axes.spines', top=False, right=False)
    
    print (sns.axes_style())
