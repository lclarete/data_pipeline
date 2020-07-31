import matplotlib.pyplot as plt
import seaborn as sns


def swarmchart(var_category, var_numeric, data_data):
# setting the chart design with seaborn style
    sns.set()
    sns.swarmplot(x=var_category, y=var_numeric, data=data_data)
#    _ = plt.xlabel(data_data[var_category].name)
#    _ = plt.ylabel(str(data_data.var_numeric.name))
#    plt.savefig(str("swarnchart_"+var_category+".png"))
    return(_)