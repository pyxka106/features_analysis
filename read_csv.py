import os
import pandas as pd


# read the exported csv file
df = pd.read_csv('./data/cd4_v_nofil.csv', sep='\t')

df.columns = ['subject_id', 'v_gene_segment', 'number']

df = df[df.number > 0]
new_df = df.reset_index(drop=True)

# sort data based on subject_id
new_df_1 = new_df.set_index(['subject_id']).sort_index()


# save files separately
for i, x in new_df_1.groupby('subject_id'):

    p = os.path.join('E:/Document/22_02/data/cd4_v_nofil', "{}.csv".format(i.lower()))
    x.to_csv(p, index=False)




