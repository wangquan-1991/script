#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import rstoolbox as rs
import matplotlib.pyplot as plt
from rstoolbox.plot import multiple_distributions
import seaborn as sns
import pandas as pd
import numpy as np
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


# In[2]:


silent_file = 'final_result-2.silent'
peptide_chain = 'A'
ncaa_list = ''


# In[3]:


rules = {'scores_ignore': [''], 'sequence': ''}
df = rs.io.parse_rosetta_file(silent_file, rules)


# In[4]:


df


# In[6]:


df3 = df.sort_values('score').head(300)
df3


# In[7]:


df4 = df[(df['packstat'] >= 0.60) & (df['sc_value'] >= 0.65)]
df4


# In[8]:


df1 = df.sort_values('shape').head(200)
df1


# In[9]:


df2 = df.sort_values('InterfaceDdg').head(300)
df2


# In[10]:


df_list=[df2,df3,df4]
intersected_df = df1
for df in df_list:
    intersected_df = pd.merge(intersected_df, df, how='inner')
  


# In[11]:


intersected_df


# In[ ]:




