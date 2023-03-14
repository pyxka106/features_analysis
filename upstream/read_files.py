import pandas as pd
import os

df = pd.read_csv('E:/Document/08_03_mutations/TERI/P(J_DEL_CD4)_1.csv', sep=',')
df_1 = df.set_index(['j_gene_segment']).sort_index()

new_df = pd.DataFrame()

for gene, group in df_1.groupby(['j_gene_segment']):

    new_row_1 = pd.DataFrame({'average': f"#{gene}", 'j_deletions': -1}, index=[0])
    df_2 = pd.concat([new_row_1, group.loc[:]]).reset_index(drop=True)
    # print(df_2)
    p = os.path.join('E:/Document/08_03_mutations/TERI/J_del_CD4', "{}.csv".format(gene))
    df_2.to_csv(p, index=False)







