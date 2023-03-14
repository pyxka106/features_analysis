import os
import json
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt

# adapted from https://github.com/briney/grp_paper/blob/master/make_figures/07_sequence-diversity.ipynb

with open('subjects_J.txt') as f:
    subjects = sorted(f.read().split())

# colors
colors = sns.hls_palette(15, s=0.9)
colors[3] = sns.hls_palette(11, s=0.9)[3]
colors[4] = sns.hls_palette(12, s=0.9)[5]

# input data location
data_path = './TERI/J_del/'

# read CD4 data
cd4file = os.path.join(data_path, 'J_del_CD4.json')
with open(cd4file) as f:
    cd4_diversity = json.load(f)

# read CD8 data
cd8_file = os.path.join(data_path, 'J_del_CD8.json')
with open(cd8_file) as f:
    cd8_diversity = json.load(f)

# initialize the plot
sns.set_style('white')
plt.figure(figsize=(4.75, 4))
plots = []

# plot the mut_frequency
for color, subject in zip(colors, subjects):
    x_1 = cd4_diversity[subject]
    print(x_1)
    cd4_diversity_conv = {float(k): v for k, v in x_1.items()}
    cd4_x_1 = cd4_diversity_conv.keys()
    cd4_x = [n for n in cd4_x_1 if n < 26.0]
    print(cd4_x)

    cd4_ys = [cd4_diversity_conv[k] for k in cd4_x if k < 26.0]
    # print(cd4_ys)
    # print(cd4_diversity[subject])
    # print(list(cd4_diversity[subject].values()))

    x_1 = cd8_diversity[subject]
    cd8_diversity_conv = {float(k): v for k, v in x_1.items()}
    cd8_x_1 = cd8_diversity_conv.keys()
    cd8_x = [n for n in cd8_x_1 if n < 26.0]
    cd8_ys = [cd8_diversity_conv[k] for k in cd8_x]
    # print(x_1)
    # cd8_ys = sum(cd8_ys_1, [])
    # print(cd8_ys)

    plot = plt.plot(cd4_x, cd4_ys, c=color, alpha=0.9, linewidth=2, label=subject)
    plt.plot(cd8_x, cd8_ys, c=color, linestyle='dashed', linewidth=2)
    plots.append(plot)

# style the plot
ax = plt.gca()
# axis limits and scale
ax.set_xlim(0, 26)
ax.set_ylim((0, 0.40))  # ((0, 0.45)) --cd8
# style ticks
ax.set_xticks(np.arange(0, 26, 1))
ax.tick_params(axis='x', labelsize=12)
ax.tick_params(axis='y', which='major', labelsize=12, length=6, width=1.25, pad=12, left=True)
# hide top, left and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(True)
# axis lables
ax.set_ylabel('Frequency', size=14)
ax.set_xlabel('Number of mutations', size=14, labelpad=8)
# plot the legend
cd4_proxy = mpl.lines.Line2D([0], [0], color='grey', linewidth=2)
cd8_proxy = mpl.lines.Line2D([0], [0], linestyle='dashed', color='grey', linewidth=2)
legend_1 = ax.legend([cd4_proxy, cd8_proxy], ['CD4', 'CD8'],
                     loc='lower right', fontsize=11.5, handlelength=3.75)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right', fontsize=11.5)
ax.add_artist(legend_1)

# save or show
plt.show()
# plt.tight_layout()
# plt.savefig('./sequence-diversity-estimation_lineplot_chao2-vs-recon.pdf')

# plot stripplot of CD4 and CD8
cd4_maxes = [{'subject': subject,
              'Mean frequency of Mutations': np.mean(list(cd4_diversity[subject].values())),
              'Cells': 'CD4'} for subject in subjects]

cd8_maxes = [{'subject': subject,
              'Mean frequency of Mutations': np.mean(list(cd8_diversity[subject].values())),
              'Cells': 'CD8'} for subject in subjects]

max_df = pd.DataFrame(cd4_maxes + cd8_maxes)

# initialize the plot
sns.set_style('white')
plt.figure(figsize=(1.5, 4))

# plot the data
sns.stripplot(data=max_df,
              x='Cells',
              y='Mean frequency of Mutations',
              hue='subject',
              order=['CD4', 'CD8'],
              size=8,
              palette={s: c for s, c in zip(subjects, colors)},
              jitter=True,
              alpha=0.8)

# style the plot
ax = plt.gca()
# remove legend
ax.legend_.remove()
# set axis scales, limits and labels
ax.set_ylim((0.035, 0.070))  # ((0.03, 0.075)) --j gene
ax.set_xlabel('Cells', size=14, labelpad=8)
ax.set_ylabel('Mean frequency of Mutations', size=14, labelpad=8)
# style ticks
ax.tick_params(axis='x', labelsize=12)
ax.tick_params(axis='y', which='major', labelsize=12, length=6, width=1.25, pad=8, right=False)
# remove top, left and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(True)

# save or show
plt.show()
# plt.tight_layout()
# plt.savefig('./figure/max-scatter_.pdf')
