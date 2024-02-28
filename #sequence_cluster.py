#本脚本用于读取建库序列，按照长度分类，并且同一长度进行聚类，保存输出
import pandas as pd
from Bio import pairwise2
# 读取Excel文件
df = pd.read_excel("0-HA1-建库序列.xlsx")

# 获取不同长度的序列
unique_lengths = df["插入序列"].str.len().unique()

# 创建新列，以序列长度命名，并将相应长度的序列填入新列
for length in unique_lengths:
    col_name = f"sequence_{length}"
    df[col_name] = df[df["插入序列"].str.len() == length]["插入序列"].reset_index(drop=True)

# 删除原始的插入序列列
df = df.drop(columns=["插入序列"])

# 保存DataFrame到Excel文件
df.to_excel("0-HA-设计总清单_with_sequences.xlsx", index=False)

#由于之前脚本存在某些数据值存在nan问题，手动清理


# 获取sequence_18列的数据，可修改对其他列进行计算
sequences = df["sequence_52"].astype(str).tolist()

# 用于存储相似序列的组
sequence_groups = []

# 定义相似度阈值（70%）
similarity_threshold = 70.0

# 用于标记哪些序列已经被分配到了一个组中
assigned = [False] * len(sequences)

# 遍历所有序列
for i, seq1 in enumerate(sequences):
    if assigned[i]:
        continue  # 如果序列已经被分配到组中，跳过
    
    # 创建一个新的组，默认包含当前序列
    group = [seq1]
    assigned[i] = True  # 标记当前序列已经被分配
    
    # 遍历其余的未分配序列进行比对
    for j, seq2 in enumerate(sequences):
        if not assigned[j] and seq1 != seq2:  # 仅处理未分配且不是同一序列的序列
            # 使用Biopython的pairwise2模块计算相似度
            alignments = pairwise2.align.globalxx(seq1, seq2, one_alignment_only=True)
            similarity = (alignments[0].score / len(seq1)) * 100  # 计算相似度百分比

            # 如果相似度大于等于阈值，将序列添加到当前组并标记为已分配
            if similarity >= similarity_threshold:
                group.append(seq2)
                assigned[j] = True

    # 将当前组添加到sequence_groups
    sequence_groups.append(group)

# 将结果写入文件    
with open("sequence_clusters_52.txt", "w") as output_file:
    for i, group in enumerate(sequence_groups):
        output_file.write(f"Group {i + 1}:\n")
        for seq in group:
            output_file.write(seq + "\n")
        output_file.write("=" * 30 + "\n")

print("结果已写入 sequence_clusters_18.txt 文件")
'''
# 打印结果，或按需进一步处理
for i, group in enumerate(sequence_groups):
    print(f"Group {i + 1}:")
    for seq in group:
        print(seq)
    print("=" * 30)
'''