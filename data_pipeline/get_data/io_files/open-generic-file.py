"""
Open csv, txt and xls.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# reading data using a class
class ExploreData:
    def __init__(self, filePath, sheetName):
        # type of data that will be read - csv or xlx
        typeData = filePath.split('.')[1]
        self.typeData = typeData
        if typeData == 'csv':
            self.data = pd.read_csv(filePath, encoding='latin1', sep='|')
        if typeData == ('xls'):
            data = pd.read_excel(filePath, sheet_name=sheetName)
            self.data = data

def col_counts(col, col_categories):
    col = pd.Categorical(col,
                    categories=col_categories,
                    ordered=True)
    col_counts = round(col.value_counts().reindex(col_categories).div(len(col)/100))
    col_counts = col_counts.sort_values(ascending=False)
    return(col_counts)


def chart_barh(col, xlabel, ylabel, title):
    plt.figure(figsize=(10,5))
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title, fontsize=17)
    col.plot(kind='barh')
    sns.set_style('ticks')
    sns.despine(trim=True, offset=10)
    return(plt.show())