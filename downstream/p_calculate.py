import glob
from mpmath import *
import pandas as pd
import os
import numpy as np

os.chdir('E:/Document/TERI_baseline_normalized')
data_files = glob.glob('*_CD4.tsv')
for data_file in data_files:
    print(data_file)
    file_name = data_file[:data_file.index(".")].split("_")
    subject_id = file_name[0]

    file_name_cd4 = f'{subject_id}_CD4.tsv'
    file_name_cd8 = f'{subject_id}_CD8.tsv'

    # import sample sequences
    df_cd4 = pd.read_csv(file_name_cd4, sep='\t')
    df_cd8 = pd.read_csv(file_name_cd8, sep='\t')
    df = pd.concat([df_cd4, df_cd8], ignore_index=True, sort=False)
    sum = len(df_cd4) + len(df_cd8)
    p_exact = len(df_cd4) / sum
    print(p_exact)
    #df = df_cd4.copy()

    # structure sample dataframe
    df = df[df['frame_type'].str.contains('Out') == False].reset_index()
    df = df[df['frame_type'].str.contains('Stop') == False].reset_index()
    df1 = df[['cdr3_length', 'v_gene', 'j_gene', 'v_deletions', 'j_deletions']]


    # P(J_CD4)
    df_2 = pd.read_csv('E:/Document/22_02_emerson/data/csv_files/P(J_CD4).csv', sep='\t')
    df2 = df_2[['j_segment', 'average']]
    df2.columns = ['j_gene', 'P(J_CD4)']
    #df2['P(J_CD4)'] = np.round(df2['P(J_CD4)'], decimals=6)

    new_df_2 = pd.merge(df1, df2, on='j_gene')

    # P(J_CD8)
    df_3 = pd.read_csv('E:/Document/22_02_emerson/data/csv_files/P(J_CD8).csv', sep='\t')
    df3 = df_3[['j_segment', 'average']]
    df3.columns = ['j_gene', 'P(J_CD8)']
    #df3['P(J_CD8)'] = np.round(df3['P(J_CD8)'], decimals=6)

    new_df_3 = pd.merge(new_df_2, df3, on='j_gene')

    # P(V_CD4)
    df_4 = pd.read_csv('E:/Document/22_02_emerson/data/csv_files/P(V_CD4).csv', sep='\t')
    df4 = df_4[['v_segment', 'average']]
    df4.columns = ['v_gene', 'P(V_CD4)']
    #df4['P(V_CD4)'] = np.round(df4['P(V_CD4)'], decimals=6)

    new_df_4 = pd.merge(new_df_3, df4, on='v_gene')

    # P(V_CD8)
    df_5 = pd.read_csv('E:/Document/22_02_emerson/data/csv_files/P(V_CD8).csv', sep='\t')
    df5 = df_5[['v_segment', 'average']]
    df5.columns = ['v_gene', 'P(V_CD8)']
    #df5['P(V_CD8)'] = np.round(df5['P(V_CD8)'], decimals=6)

    new_df_5 = pd.merge(new_df_4, df5, on='v_gene')

    # P(J_CDR3_CD4)
    df_6 = pd.read_csv('E:/Document/22_02_emerson/data/csv_files/cd4_j_cdr3.csv', sep=',')
    df_6.columns = ['j_gene', 'cdr3_length', 'P(J_CDR3_CD4)']
    #df_6['P(J_CDR3_CD4)'] = np.round(df_6['P(J_CDR3_CD4)'], decimals=6)

    new_df_6 = pd.merge(new_df_5, df_6, on=['j_gene', 'cdr3_length'])

    # P(J_CDR3_CD8)
    df_7 = pd.read_csv('E:/Document/22_02_emerson/data/csv_files/cd8_j_cdr3.csv', sep=',')
    df_7.columns = ['j_gene', 'cdr3_length', 'P(J_CDR3_CD8)']
    #df_7['P(J_CDR3_CD8)'] = np.round(df_7['P(J_CDR3_CD8)'], decimals=6)

    new_df_7 = pd.merge(new_df_6, df_7, on=['j_gene', 'cdr3_length'])

    # P(V_CDR3_CD4)
    df_8 = pd.read_csv('E:/Document/22_02_emerson/data/csv_files/cd4_v_cdr3.csv', sep=',')
    df_8.columns = ['v_gene', 'cdr3_length', 'P(V_CDR3_CD4)']
    #df_8['P(V_CDR3_CD4)'] = np.round(df_8['P(V_CDR3_CD4)'], decimals=6)

    new_df_8 = pd.merge(new_df_7, df_8, on=['v_gene', 'cdr3_length'])

    # P(V_CDR3_CD8)
    df_9 = pd.read_csv('E:/Document/22_02_emerson/data/csv_files/cd8_v_cdr3.csv', sep=',')
    df_9.columns = ['v_gene', 'cdr3_length', 'P(V_CDR3_CD8)']

    new_df_9 = pd.merge(new_df_8, df_9, on=['v_gene', 'cdr3_length'])

    # P(V_DEL_CD4)
    df_10 = pd.read_csv('E:/Document/08_03_mutations/Emerson/P(V_DEL_CD4)_1.csv', sep=',')
    df_10.columns = ['v_gene', 'v_deletions', 'P(V_DEL_CD4)']

    new_df_10 = pd.merge(new_df_9, df_10, on=['v_gene', 'v_deletions'])

    # P(V_DEL_CD8)
    df_11 = pd.read_csv('E:/Document/08_03_mutations/Emerson/P(V_DEL_CD8)_1.csv', sep=',')
    df_11.columns = ['v_gene', 'v_deletions', 'P(V_DEL_CD8)']

    new_df_11 = pd.merge(new_df_10, df_11, on=['v_gene', 'v_deletions'])

    # P(J_DEL_CD4)
    df_12 = pd.read_csv('E:/Document/08_03_mutations/Emerson/P(J_DEL_CD4)_1.csv', sep=',')
    df_12.columns = ['j_gene', 'j_deletions', 'P(J_DEL_CD4)']

    new_df_12 = pd.merge(new_df_11, df_12, on=['j_gene', 'j_deletions'])

    # P(J_DEL_CD8)
    df_13 = pd.read_csv('E:/Document/08_03_mutations/Emerson/P(J_DEL_CD8)_1.csv', sep=',')
    df_13.columns = ['j_gene', 'j_deletions', 'P(J_DEL_CD8)']

    new_df_13 = pd.merge(new_df_12, df_13, on=['j_gene', 'j_deletions'])

    final_df = new_df_13.copy()
    #print(final_df)
    #pd.set_option('display.max_columns', None)
    #pd.set_option('display.max_rows', None)

    #final_df.to_csv('./data/csv_files/trained/p_value.csv', sep='\t', index=False)

# export to likelihood.py calculation
    def func(p, a, b, c, d, e, f, i, n, w, x, y, z):
        return p * a * b * c * d * e * f + (1 - p) * i * n * w * x * y * z


    def main():
        df = final_df
        max_p = 0
        max_liekli = 0

        for p in np.arange(0, 1, 0.01):
            df['likelihood'] = df.select_dtypes(include=['float64']).apply(lambda row: func(p, row['P(V_CD4)'],
                                                                                            row['P(J_CD4)'],
                                                                                            row['P(V_CDR3_CD4)'],
                                                                                            row['P(J_CDR3_CD4)'],
                                                                                            row['P(V_DEL_CD4)'],
                                                                                            row['P(J_DEL_CD4)'],
                                                                                            row['P(V_CD8)'],
                                                                                            row['P(J_CD8)'],
                                                                                            row['P(V_CDR3_CD8)'],
                                                                                            row['P(J_CDR3_CD8)'],
                                                                                            row['P(V_DEL_CD8)'],
                                                                                            row['P(J_DEL_CD8)']
                                                                                            ),
                                                                           axis=1)
            # df['likelihood'].values = df.apply(Decimal)
            pro = fprod(df['likelihood'])

            if pro > max_liekli:
                max_liekli = pro
                max_p = p
        print('+++', max_liekli)
        print('***', max_p)


    if __name__ == '__main__':
        main()
