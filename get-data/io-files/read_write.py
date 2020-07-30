# https://medium.com/@kadek/elegantly-reading-multiple-csvs-into-pandas-e1a76843b688

import os

# create a new directory
if not os.path.exists('data'):
    os.mkdir('data')

# read csv files

# using dask
import dask.dataframe as dd
df = dd.read_csv('*.csv')

# using glob
import glob
files = glob.glob('data*.csv')

# using os
import os
files = os.listdir()


# read several files in just one line
df = pd.concat(
    [pd.read_csv(f) 
    for f in glob.glob('data*.csv')],
    ignore_index = True)
