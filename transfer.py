import fnmatch
import glob
import os
import pandas as pd

# Transfer multiple .csv files to one single Dataframe
os.chdir('./data/cd4_v_nofil')
data_files = glob.glob('*.csv')

df = pd.DataFrame()


for data_file in data_files:
    if fnmatch.fnmatch(data_file, '*subject_*.csv'):
        df_new = pd.read_csv(data_file, sep=',')

        # add new row with respective subject_id
        file_name = data_file[:data_file.index(".")].split("_")
        subject_id = file_name[0] + '_' + file_name[1]
        new_row = pd.DataFrame({'v_gene_segment': f"#{subject_id}"}, index=[0])

        # merge together
        df2 = pd.concat([new_row, df_new.loc[:]]).reset_index(drop=True)
        df = df.append(df2, ignore_index=False)


df.to_csv('../txt_files/cd4_v_nofil.txt', index=False, sep='\t', header=False)

# manually transfer .csv to .txt ---- not necessary
