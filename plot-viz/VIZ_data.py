# returns a frequency table and a chart for a categorical variable
'''Goals:
- Return a three types of charts: bars, boxplots, heatmaps
- Differenciate between counts and percentages
- Plot the values, axis labels and titles
- Set the colors and style of each element: charts, legend, axis, etc.
- Set the size
- Plot a table with values and a chart
- Describe variables and its crosstables (with mean, median, etc.)

'''

import matplotlib.pyplot as plt
import seaborn as sns

def chart_var(var, label):
    sns.set(style="ticks")

    if type(var[1]) == str:
        percent = round(var.value_counts()
                            /len(var)*100).to_frame()
        percent.plot.barh(color="C", legend=False)
        sns.despine(offset=15, trim=True, left=True)
        plt.xlabel(label, fontsize=12)
        plt.ylabel("%", fontsize=12)
        plt.title(str(label)+" de prefeitos(as) em 2016", 
                      fontsize=18)
        plt.figure(figsize=(20,10))
        return(plt.show())
    else:
        descriptive = var.describe().to_frame()
        bins = int(np.sqrt(len(var)))
        var.hist(bins=bins, color="C")
        sns.despine(offset=15, trim=True, left=True)
        plt.xlabel("label", fontsize=12)
        plt.ylabel("%", fontsize=12)
        plt.title("Distribuição de "+ str(label).lower()+" de prefeitos(as) em 2016", 
                      fontsize=18)
        plt.figure(figsize=(20,10))
        return(descriptive,plt.show())

        
        
        


def quanti_var(var):
descriptive = round(var.describe())
_ = var.hist(color="C")
_ = plt.ylabel("Count")
plt.show()
return(_, descriptive)

def crosstab(var):    
    pd.crosstab(total.age_rec, total.rec_pop_3, 
                normalize='columns'
            ).round(4)


