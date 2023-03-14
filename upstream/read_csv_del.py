import pandas as pd

# read the exported csv file
df = pd.read_csv('./TERI/cd8_v_del.csv', sep='\t')

df.columns = ['sample_id', 'v_gene_segment', 'v_deletions', 'del_count']

df = df[df['v_gene_segment'].str.contains('OR') == False]
new_df = df.reset_index(drop=True)

# sort data based on subject_id
new_df_1 = new_df.set_index(['sample_id']).sort_index()

# calculate gene/del proportion within each sample
test_df = pd.DataFrame()
for i, x in new_df_1.groupby('sample_id'):
    x['freq'] = x['del_count'] / x.groupby('v_gene_segment')['del_count'].transform('sum')

    test_df = test_df.append(x)

    # transform to two index vs. samples_id
    norm_df = test_df.pivot_table('freq', ['v_gene_segment', 'v_deletions'], 'sample_id')
    # calculate mean value within cd4 or cd8
    norm_df['average'] = norm_df.mean(numeric_only=True, axis=1)

    # export finished .csv file
    # pd.set_option('display.max_columns', None)
    # pd.set_option('display.max_rows', None)
    header = ['average']
    norm_df.to_csv('./TERI/P(V_DEL_CD8)_1.csv', index=True, header=True, columns=header)

# following process in read_cdr3_2.py ---- mainly for table transformation


