import fnmatch
import glob
import os
import pandas as pd

# Transfer multiple .txt files to one single Dataframe
os.chdir('./data/txt_files')
data_files = glob.glob("*_v_nofil.txt")

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
                vgene, count = l[0], float(l[1])
                data[subject][vgene] = count

    # calculate gene usage frequency within each subject
    df = pd.DataFrame(data).fillna(0)
    norm_df = df / df.sum()

    new_df = norm_df.transpose()
    new_df['sample_id'] = new_df.index.values
    data = new_df.melt(id_vars='sample_id', value_name='frequency', var_name='v_gene')

    # sorted by cd4 or cd8
    file_name = files[:files.index(".")].split("_")
    subject_id = file_name[0]

    data['subject_id'] = f"{subject_id}"
    final_df = final_df.append(data, ignore_index=False)

    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    final_df.to_csv('../txt_files/v_nofil_resorted.txt', index=False, sep='\t')
    # print(final_df)


