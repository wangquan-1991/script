#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import rstoolbox as rs
import matplotlib.pyplot as plt
from rstoolbox.plot import multiple_distributions
import seaborn as sns
import pandas as pd
plt.style.use('ggplot')
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['figure.dpi'] = 300


# In[ ]:


df = pd.read_csv('all-18.csv')
#df.head()


# In[ ]:

'''
def plot_df(df_, metrics_, outname_):
    # 分析优化后的得分区间:
    fig = plt.figure(figsize=(20, 20))
    axes = rs.plot.multiple_distributions(df_, fig, [3, 5],  showfliers=False, values=metrics_)
    fig.savefig(f'{outname_}.png')


# In[ ]:


if __name__ == '__main__':
    # read silents;
    csv_file = 'all-18.csv'
    #df = pd.read_csv(all.csv)
    #df.to_csv('raw_data.csv')
    list(df.columns)
# fold指标:
    folding_metrics = ['ScorePerResFilter', 'AlaCount', 'Buried_non_polar_SASA_per_res', 'CavityVolume',
                       'ExposedHydrophobics_on_TotalSASAPercent', 'GeometryScore', 'netcharge', 'DisulfideBondSpanHotspot',
                       'PackStat', 'ss4pred_mismatch_rate', 'SSShapeComplementarity', 'VBUNS', 'SBUNS']
    plot_df(df, folding_metrics, 'folding_metrics')
    
    binding_metrics = ['aploar_cms_', 'InterfaceHoles', 'dG_cross', 'dG_cross/dSASAx100',
                       'dSASA_int', 'sc_value', 'target_interface_sap', 'InterfaceAverageDegree',
                       'InterfaceDAlphaBallBuriedUnsatHbondFilter', 'delta_unsatHbonds']
    plot_df(df, binding_metrics, 'binding_metrics')
'''

# In[ ]:


#单项根据排序来选，注意正负号
#df.sort_values(by='score').head(20)


# In[ ]:


#单项根据值来筛选
#df5 = df[df.aploar_cms_>= 300]
#df5.to_csv('300.csv')


df_selection = df[(df.InterfaceHoles < 0.5 ) &
         (df.sc_value >= 0.65) &
         (df.aploar_cms_ >= 210) &
          (df.dSASA_int >= 1200)&
          (df.CavityVolume <= 10) &
          (df.PackStat > 0.63) &
          (df.ss4pred_mismatch_rate < 0.1) &
      #    (df['delta_unsatHbonds'] <= 5)&
          (df['Buried_non_polar_SASA_per_res'] > 50)
          ]
#df_selection
df_selection.to_csv('final_select-18.csv')

# In[ ]:


#取交集
#df_selection1 = df[(df['InterfaceHoles']<10)&
#     (df['score']< -300)             ]
#df_selection1

