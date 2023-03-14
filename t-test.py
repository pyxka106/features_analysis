from scipy.stats import ttest_ind
import pandas as pd

df_v = pd.read_csv('./data/txt_files/v_gene_resorted_2.txt', sep='\t')

# must be the data sets that are to be compared, not the means of the data sets
for i, df in df_v.groupby('v_gene'):
    p_value = []
    cd4 = df[df['subject_id'] == 'cd4']
    cd8 = df[df['subject_id'] == 'cd8']

    t_test = ttest_ind(cd4['frequency'], cd8['frequency'], nan_policy='omit')
    result = f"{i, t_test}"
    p_value.append(result)
    print(p_value)
