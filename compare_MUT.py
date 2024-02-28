from pyrosetta import *
import rstoolbox as rs
from rstoolbox.io import parse_rosetta_file
init()

silent_file = 'final_result_all.silent'

#读取规则：全读取，并读取H，L链序列
rules = {'sequence': 'HL'}
df = parse_rosetta_file(silent_file, rules)

#输入WT的重链，轻链序列
WT_H = 'QVQLQQSGAELVKPGASVKLSCTASGFNIKDTYMHWVKQRPEQGLEWIGRIDPANGNTKYDPKFQGKATITADTSSNTAYLQLSSLTSEDTAVYYCASYYGIYWGQGTTLTVSSASTKGPSVFPLPPSSKSTSGGTAALGCLVKDYFPEPVTVSWNSGALTSGVHTFPAVLQPSGLYSLSSVVTVPSSSLGTQTYICNVNHKPSNTKVDKKVEPKSC'
WT_L = 'DIQMTQSPSSLSASLGERVSLTCRASQEISGYLSWLQQKPDGYIKRLIYAASTLDSGVPKRFSGSRSGSDYSLTISSLESEDFADYYCLQYASYPRTFGGGTKVEIKRTVAAPSVFIFPPPDEILKSGTAVVVCLLNNFYPREAKVQWKVDNALQSGNSQESVTEQDSKDSTYSLSSTLFLSKADYEKHKVYACEVTHQGLSSPVTKSFNRGEC'


#比较重链：
df['diff_info_H'] = ''

# 定义函数来比较"sequence_L"与"WT_L"的差异并更新新列
def compare_sequence(seq):
    diff_positions = []
    diff_values = []
    for i in range(len(WT_H)):
        if seq[i] != WT_H[i]:
            diff_positions.append(i + 1)  # 加1是因为位点从1开始计数
            diff_values.append(f"{WT_H[i]}{i+1}{seq[i]}")
    if diff_positions:
        diff_info = ', '.join(diff_values)
        return diff_info
    else:
        return '无突变'

# 使用apply函数将函数应用到"sequence_L"列的每一行，生成新的列
df['diff_info_H'] = df['sequence_H'].apply(compare_sequence)

# 输出包含差异信息的新列
print(df['diff_info_H'])


#比较轻链，并将突变输出

# 假设您的DataFrame为df，"sequence_L"列为seqL，"WT_L"为WT_L
# 创建一个新列来存储差异
df['diff_info_L'] = ''

# 定义函数来比较"sequence_L"与"WT_L"的差异并更新新列
def compare_sequence(seq):
    diff_positions = []
    diff_values = []
    for i in range(len(WT_L)):
        if seq[i] != WT_L[i]:
            diff_positions.append(i + 1)  # 加1是因为位点从1开始计数
            diff_values.append(f"{WT_L[i]}{i+1}{seq[i]}")
    if diff_positions:
        diff_info = ', '.join(diff_values)
        return diff_info
    else:
        return '无突变'

# 使用apply函数将函数应用到"sequence_L"列的每一行，生成新的列
df['diff_info'] = df['sequence_L'].apply(compare_sequence)

# 输出包含差异信息的新列
print(df['diff_info'])

#保存CSV
df.to_csv('raw_data_MUT.csv')



