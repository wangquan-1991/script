# load reference and design data.
import os
import rstoolbox as rs
import matplotlib.pyplot as plt
from rstoolbox.plot import multiple_distributions
import seaborn as sns
import pandas as pd
plt.style.use('ggplot')
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['figure.dpi'] = 300
from Bio import PDB
parser = PDB.PDBParser()
pdb_io = PDB.PDBIO()


class Select(PDB.Select):
    def __init__(self, chain_id):
        self.chain_id = chain_id
    def accept_chain(self, chain):
        if chain.id == self.chain_id:
            return True


def get_peptide_structure(pdbfile, peptide_chain):
    selection = Select(peptide_chain)
    structure = parser.get_structure(' ', pdbfile)[0]
    pdb_io.set_structure(structure)
    pdb_io.save(pdbfile, selection)


def extract_pdb_by_tag(tag_list, silent_file, ncaa_list):
    """
    Summary: extract pdbs from silent by tag labels;
    Args:
        tag_label (str): tag list of the description;
        silent_file (str): raw silent file;
    """
    tag_list = ' '.join(tag_list)
    if ncaa_list:
        ncaa_params_list = ' '.join([ncaa+'.params' for ncaa in ncaa_list.split(',')])
        os.system(f'extract_pdbs.static.linuxgccrelease \
                  -in::file::silent {silent_file} \
                  -in:file:tags {tag_list} -extra_res_fa {ncaa_params_list}')
    else:
        os.system(f'extract_pdbs.static.linuxgccrelease \
                  -in::file::silent {silent_file} \
                  -in:file:tags {tag_list}')


# add wt reference sequence.
silent_file = 'final_result.silent'
peptide_chain = 'A'
ncaa_list = ''

# 下面是筛选代码;
rules = {'scores_ignore': [''], 'sequence': ''}
df = rs.io.parse_rosetta_file(silent_file, rules)  # input silent file;
#df.to_csv('all.csv')


# 根据复合物的总能量进行筛选:
#df_selection1 = df.sort_values('score').head(1000)

# 根据5个性质的平均值进行筛选:
'''
df_selection2 = df[(df['score'] < df['score'].mean()) &
                              (df['dG_separated/dSASAx100'] < df['dG_separated/dSASAx100'].mean()) &
                              (df['dSASA_int'] > df['dSASA_int'].mean()) &
                              (df['dSASA_hphobic'] > df['dSASA_hphobic'].mean()) &
                              (df['delta_unsatHbonds'] > df['delta_unsatHbonds'].mean())
                              ]
'''
#df_selection2 = df[(df.sort_values('aploar_cms_').tail(1000)),
#                   (df.sort_values('score').head(300)),
#                   (df.sort_values('InterfaceHoles').head(1000)),
#                   (df.sort_values('sc_value').tail(1000)),
#                   (df.sort_values('dSASA_hphobic').tail(500)),
#                   (df.sort_values('target_interface_sap').tail(500))
#
#                                                                                               ]
#df_selection2

# hydrogen bond count;
#df_selection3 = df.sort_values('hbonds_int').head(1000)

# 根据 HbNet氢键网络得分进行筛选
#df_selection4 = df[(df['hbonds_int'] > df['hbonds_int'].mean())].sort_values('HBNet_Score').head(1000)

#a select by aploar_cms_
df_selection2 = df.sort_values('aploar_cms_').tail(1000)
df_selection3 = df.sort_values('score').head(300)
df_selection4 = df.sort_values('InterfaceHoles').head(1000)
df_selection5 = df.sort_values('sc_value').tail(1000)
df_selection6 = df.sort_values('dSASA_hphobic').tail(500)
df_selection7 = df.sort_values('target_interface_sap').tail(500)
#df_selection8 = df(df_selection2+df_selection3+df_selection4+df_selection5+df_selection6+df_selection7)
# select by target_interface_sap
#df_selection6 = df.sort_values('target_interface_sap').head(1000)

#total_len = len(df_selection2.index)

#total_len = len(df_selection2.index) + len(df_selection3.index) + len(df_selection4.index) + len(df_selection5.index) + len(df_selection6.index) + len(df_selection7.index)
#print(len(df_selection1.index))
#print(len(df_selection8.index))
#print(len(df_selection3.index))
#print(len(df_selection4.index))
#print(len(df_selection5.index))
#print(len(tag_label_list))
#print(len(set(tag_label_list)))
#print(total_len)
#len(tag_label_list)
#len(set(tag_label_list))

#if total_len == 0:
#    exit(0)'
# save output pdb for one selection;
#tag_label_list = [df_selection2['description']]
#tag_label_list = [str(line)for line in tag_label_list]
#tag_label_list = ''.join(tag_label_list)
tag_label_list = list(df_selection2['description']) + list(df_selection3['description']) 
tag_label_list = set(tag_label_list)
extract_pdb_by_tag(tag_label_list, silent_file, ncaa_list)
print(len(tag_label_list))
print(len(set(tag_label_list)))
#if len(tag_label_list1) > 999:
#    n = 999
#    tag_label_lists = [tag_label_list[i: i+n] for i in range(0, len(tag_label_list), n)] # 切片，逐步extract
#    for tag_label_list in tag_label_lists:
#        extract_pdb_by_tag(tag_label_list, silent_file, ncaa_list)
#else:
#extract_pdb_by_tag(tag_label_list, silent_file, ncaa_list)


#tag_label_list1 = [df_selection3['description']]
#tag_label_list1 = [str(line)for line in tag_label_list1]
#tag_label_list1 = ''.join(tag_label_list1)

#if len(tag_label_list1) > 999:
#    n = 999
#    tag_label_lists = [tag_label_list[i: i+n] for i in range(0, len(tag_label_list), n)] # 切片，逐步extract
#    for tag_label_list in tag_label_lists:
#        extract_pdb_by_tag(tag_label_list, silent_file, ncaa_list)
#else:
#extract_pdb_by_tag(tag_label_list, silent_file, ncaa_list)


# 保存多肽的单体构象;
#for pdbfile in os.listdir():
#    os.system('')
#    if pdbfile.endswith('.pdb'):
#        get_peptide_structure(pdbfile, peptide_chain)
