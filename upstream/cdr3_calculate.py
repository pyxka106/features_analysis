import fnmatch
import glob
import os
import pandas as pd

# Transfer compared .txt files to one single Dataframe
os.chdir('./data/txt_files')
data_files = glob.glob("*.txt")
#print(data_files)

data = {}
final_df = pd.DataFrame()

for files in data_files:
    with open(files) as f:
        subject_data = f.read().split('#')[1:]
    data = {}
    for sd in subject_data:
        subject = sd.split('\n')[0].strip()
        data[subject] = {}
        for line in sd.split('\n')[1:]:
            l = line.strip().split()
            if l:
                muts, count = float(l[0]), float(l[1])
                data[subject][muts] = count

    # calculate gene usage frequency within each sample
    df = pd.DataFrame(data).fillna(0)
    norm_df = df / df.sum()

    # calculate the mean value within subjects(cd4 & cd8)
    test_df = norm_df.copy()
    test_df['average'] = test_df.mean(numeric_only=True, axis=1)

    # mean_df = new_df.mean()
    # std_df = new_df.std()
    test_df['cdr3_length'] = test_df.index.values

    # sorted by cd4 or cd8
    file_name = files[:files.index(".")].split("_")
    subject_id = file_name[0]
    new_row = pd.DataFrame({'cdr3_length': f"#{subject_id}"}, index=[0])

    df2 = pd.concat([new_row, test_df.loc[:]]).reset_index(drop=True)
    # print(df2)
    final_df = final_df.append(df2, ignore_index=False)
    #print(final_df)


    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    header = ['cdr3_length', 'average']
    final_df.to_csv('../csv_files/cdr3_resorted.csv', index=False, columns=header)

# manually transfer .csv to .txt
