import os

from magine.data.experimental_data import load_data

# location of data file
file_path = os.path.join(os.path.dirname(__file__), 'Data',
                         'bendamustine_data.csv.gz')


""" 
This loads the ExperimentalData Class instance.
You can load it into any file with the line

'from exp_data import exp_data'

"""
exp_data = load_data(file_path, low_memory=False, index_col=0)
