import os

import pandas as pd
import numpy as np

# read the exported csv file
df = pd.read_csv('./data/csv_files/trained/P(V_CDR3_CD4)_1.csv', sep=',')

df.columns = ['v_gene_segment', 'cdr3_length', 'average']

new_df = df.pivot_table('average', ['v_gene_segment'], 'cdr3_length')

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

new_df.to_csv('./data/csv_files/trained/P(V_CDR3_CD4).csv', index=True, header=True)

# manually change _final.csv to P(X_CDx).csv
