import pandas as pd

######################### ----- Export CSV Functions ----- ##################################

def export_one_csv(data, file_name):
    """
    Export data to a csv.
    Be careful about the directory to save the files,
    specially when you're save the results in a different directory 
    where your python functions are located.
    """
    data.to_csv('../tables/' + file_name + '.csv', index=False)
    pass
    
def export_several_csv(dict_data):
    """
    Loop over a dictionary of data and export to a csv
    """
    for k, v in dict_data.items():
        export_one_csv(pd.DataFrame(dict_data[k]), k)
    pass


