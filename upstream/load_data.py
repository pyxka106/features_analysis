import os
import json

output_dir = './TERI/J_del'
# os.mkdir(diversity_output_dir)

# input data location
data_path = './TERI/J_del/'
data_filename = 'J_del_CD4.csv'
data_file = os.path.join(data_path, data_filename)


# read data file
data = {}
with open(data_file) as f:
    subject_samples = f.read().split('#')[1:]
    for ss in subject_samples:
        gene = ss.split('\n')[0]
        # print(gene)
        data[gene] = {}
        mut_set = '\n'.join(ss.split('\n'))[1:].split('>')
        for mutation in mut_set[1:]:
            muts = float(mutation.split('\n')[0])
            # print(muts)
            # print(type(muts))
            # print(muts)
            # data[gene][muts] = []
            vals = mutation.split('\n')[1:]
            for val in vals:
                if not val.split():
                    continue
                freq = float(val)
                data[gene][muts] = freq
                # print(data)
                # data[gene][muts].append(freq)
        # print(data)
        out_file = os.path.join(output_dir, 'J_del_CD4.json')
        with open(out_file, 'w') as f:
            json.dump(data, f)

