# TRYING TO ELEGRANTLY READ SEVERAL FILES

# returns a list file names from the working directory
import glob
files = glob.glob('*.txt')

# VERSION 1
# concats a list of dataframes
df = pd.concat(
    # reads json file line by line (lines=True)
    # iterates through each file
    [pd.read_json(f, lines=True) for f in glob.glob('*.txt')],   
)

# Version 2

list_dfs = []
for i in files:
    list_dfs.append(pd.read_json(i, lines=True))