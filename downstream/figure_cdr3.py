from __future__ import print_function

import inline as inline
import matplotlib
import seaborn as sns
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd

with open('./data/subjects.txt') as f:
    subjects = sorted(f.read().split())

colors = sns.hls_palette(20, s=0.9)
colors[3] = sns.hls_palette(11, s=0.9)[3]
colors[4] = sns.hls_palette(12, s=0.9)[5]

color_dict = {s: c for s, c in zip(subjects, colors)}

sns.palplot(colors)


def cdr3_length_histogram(df, color_dict, figfile=None, figsize=(6.5, 4),
                          style='white', legend_location='upper right',
                          shade=False, shade_alpha=0.1, legend=True,
                          ylim=(0, 0.16), xlim=(0, 40),
                          label_fontsize=14, tick_fontsize=12, legend_fontsize=11):
    # initialize the plot
    sns.set_style(style)
    plt.figure(figsize=figsize)

    # plot the data
    for subject in subjects:
        color = color_dict[subject]
        xs = df.index.values
        ys = df[subject]
        plt.plot(xs, ys, c=color, alpha=0.8, label=subject)
        if shade:
            shade_lower = [0] * len(xs)
            plt.fill_between(x=xs, y1=shade_lower, y2=ys, color=color, alpha=shade_alpha)

    # style the plot
    ax = plt.gca()
    # set axis limits and labels
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_ylabel('Frequency', fontsize=label_fontsize, labelpad=6)
    ax.set_xlabel('CDR3 length (AA)', fontsize=label_fontsize)

    # style ticks
    ax.set_yticks(np.arange(0, 0.30, 0.05))
    ax.set_xticks(np.arange(9, 72, 3))
    ax.tick_params(top=False, labeltop=False, bottom=True, labelbottom=True)
    ax.tick_params(axis='x', which='major', labelsize=tick_fontsize)
    ax.tick_params(axis='y', which='major', labelsize=tick_fontsize, length=6, width=1.25, pad=6, left=True)
    # hide top, left and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(True)
    # configure the legend
    if legend:
        handles, labels = ax.get_legend_handles_labels()

        ax.legend(handles, labels, loc=legend_location, fontsize=legend_fontsize)

    # save or show
    if figfile is not None:
        plt.tight_layout()
        plt.savefig(figfile)
    else:
        plt.show()


# load the data
with open('./data/txt_files/cdr3_resorted.txt') as f:
    cdr3_data = f.read().split('#')[1:]
data = {}
for d in cdr3_data:
    subject = d.split('\n')[0].strip()
    data[subject] = {}
    for line in d.split('\n')[1:]:
        l = line.strip().split()
        if l:
            muts, count = float(l[0]), float(l[1])
            data[subject][muts] = count

# convert to a DataFrame and normalize
cdr3_df = pd.DataFrame(data).fillna(0)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# make the plot
cdr3_length_histogram(cdr3_df.sort_index(), color_dict,
                      ylim=(0, .25), xlim=(10, 75.99),
                      shade=True, figsize=(7.5, 4.45),
                      legend=True,
                      figfile='E:/Document/22_02/figure/cdr3_length.pdf'
                      )
