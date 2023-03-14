import glob
import os
import pandas as pd

# Transfer multiple .csv files to one single Dataframe
os.chdir('./TERI/J_del_CD4')
data_files = glob.glob('*.csv')

result_df = pd.DataFrame()
for data_file in data_files:
    df_new = pd.read_csv(data_file, sep=',')

    df_1 = df_new.set_index(['j_deletions']).sort_index()

    for mut, group in df_1.groupby(['j_deletions']):
        new_row_1 = pd.DataFrame({'average': f">{mut}"}, index=[0])
        df_2 = pd.concat([new_row_1, group.loc[:]]).reset_index(drop=True)
        result_df = result_df.append(df_2, ignore_index=True)

        result_df = result_df[result_df['average'].str.contains('>-1') == False]
        result_df.to_csv('E:/Document/08_03_mutations/TERI/J_del/J_del_CD4.csv', sep='\t', index=False, header=False)
        # print(result_df)
