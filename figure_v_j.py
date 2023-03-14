import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv('./data/txt_files/v_nofil_resorted_2.txt', sep='\t')
#print(df)

# order by gene name
df_sort = df.sort_values('v_gene')

ax = sns.barplot(data=df_sort,
                 x='v_gene', y='frequency', hue='subject_id',
                 errorbar='sd', capsize=.01, errcolor=".5",
                 palette='pastel')
plt.xticks(rotation=45)
ax.figure.set_size_inches(25, 10)
#plt.show()
plt.savefig('E:/Document/22_02/figure/v_nofil_bar.pdf')

# resorted_2 as using drop_OR.py

