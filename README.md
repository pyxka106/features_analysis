# read the exported csv file
**read_csv.py** sort data based on subject_id and save files separately

# transfer multiple .csv files to one single Dataframe
**transfer.py** read each subject file and concatenate all files to one Dataframe, then saved as .txt files

# calculate for each features
**cdr3_calculate.py** calculate CDR3_length for CD4 and CD8 together and resorted to one single .csv file\
**v_j_calculate.py** calculate gene usage frequency within each subject and resorted CD4 and CD8 to one single .csv file\
**read_cdr3.py** read cdr3/gene files and alculate gene/cdr3 proportion within each subject in the same time\
**read_cdr3_2.py** transform the exported file from **read_cdr3.py**\
**read_csv_del.py** read and calculate gene/del proportion within each sample\
**read_files.py** add label of gene segment\
**read_files.py** add label of mutations number\
**load_data.py** tranfer .csv file to .json for each **gene segment**

# plotting the figures for each feature
**figure_cdr3.py** CDR3 length histogram\
**figure_v_j.py** V/J gene usage frequency barplot\
**make_figure.py** plot v_gene/mut frequency and its stripplot\
**make_figure_j.py** plot j_gene/mut frequency and its stripplot

# CD4/8 ratio and other calculation
**p_calculation.py**\
**t_test.py**
