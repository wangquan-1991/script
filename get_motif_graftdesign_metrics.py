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


def read_silent(silent_file):
    prefix = silent_file.split('.')[0]
    print(prefix)
    # add wt reference sequence.
    rules = {'scores_ignore': [''], 'sequence': ''}
    df = rs.io.parse_rosetta_file(silent_file, rules)  # input silent file;
    df = rs.utils.add_column(df, 'condition', prefix)
    df = df.dropna()
    return df


def plot_df(df_, metrics_, outname_):
    # 分析优化后的得分区间:
    fig = plt.figure(figsize=(20, 20))
    axes = rs.plot.multiple_distributions(df_, fig, [3, 5], x='condition', showfliers=False, values=metrics_)
    fig.savefig(f'{outname_}.png')


def extract_pdb_by_tag(tag_list, silent_file):
    """
    Summary: extract pdbs from silent by tag labels;
    Args:
        tag_label (str): tag list of the description;
        silent_file (str): raw silent file;
    """
    tag_list = ' '.join(tag_list)
    # os.system(f'extract_pdbs.mpi.linuxgccrelease \
    #           -in::file::silent {silent_file} \
    #           -in:file:tags {tag_list}')
    os.system(f'extract_pdbs.static.macosclangrelease \
              -in::file::silent {silent_file} \
              -in:file:tags {tag_list}')


if __name__ == '__main__':
    # read silents;
    silent_file = 'result.silent'
    df = read_silent(silent_file)
    df.to_csv('raw_data.csv')
    list(df.columns)

    # fold指标:
    folding_metrics = ['ScorePerResFilter', 'AlaCount', 'Buried_non_polar_SASA_per_res', 'CavityVolume',
                       'ExposedHydrophobics_on_TotalSASAPercent', 'GeometryScore', 'netcharge', 'DisulfideBondSpanHotspot',
                       'PackStat', 'ss4pred_mismatch_rate', 'SSShapeComplementarity', 'VBUNS', 'SBUNS']
    plot_df(df, folding_metrics, 'folding_metrics')

    # bind指标:
    binding_metrics = ['aploar_cms_', 'InterfaceHoles', 'dG_cross', 'dG_cross/dSASAx100',
                       'dSASA_int', 'sc_value', 'target_interface_sap', 'InterfaceAverageDegree',
                       'InterfaceDAlphaBallBuriedUnsatHbondFilter', 'delta_unsatHbonds']
    plot_df(df, binding_metrics, 'binding_metrics')

    # selection(可选);
    df_selection = df[(df['InterfaceHoles']<0) &
                      (df['sc_value'] >= 0.65) &
                      (df['aploar_cms_'] >= 300) &
                      (df['dSASA_int'] >= 1200) &
                      (df['CavityVolume'] <= 50) &
                      (df['PackStat'] > 0.6) &
                      (df['ss4pred_mismatch_rate'] < 0.05) &
                      (df['delta_unsatHbonds'] <= 5) &
                      (df['Buried_non_polar_SASA_per_res'] > 45)
                      ]
    df_selection
    df_selection.to_csv('final_selection.csv')

    # 没有筛选到合适的结构;
    if len(df_selection.index) == 0:
        exit(0)

    # 输出pdb结构;
    # save output pdb for one selection;
    tag_label_list = list(df_selection['description'])

    if len(tag_label_list) > 999:
        n = 999
        tag_label_lists = [tag_label_list[i: i+n] for i in range(0, len(tag_label_list), n)] # 切片，逐步extract
        for tag_label_list in tag_label_lists:
            extract_pdb_by_tag(tag_label_list, silent_file)
    else:
        extract_pdb_by_tag(tag_label_list, silent_file)
