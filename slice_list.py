import glob
import os
import shutil


# 创建不存在的目录，以免报错
def create_floder_safely(floder_name):
    if not os.path.exists(floder_name):
        os.makedirs(floder_name)
    else:
        print(f"{floder_name} exists. \n")

        
# 文件目录
floder_path = "./match"

# 文件后缀名
target_file = "*.0"

# 份数
subset_size = 300

# 结果目录
results_floder_path = "./matchinput"

# 在文件目录筛选指定文件后缀名的文件并保存至列表
file_list = glob.glob(f"{floder_path}/{target_file}")

# 按照份数将列表均分
'''
file_set=list()
for i in range(0, len(file_list), subset_size):
    subset = file_list[i:i + subset_size]
    file_set.append(subset)
'''
# 列表解析式提高运行效率
file_set = [file_list[i:i + subset_size] for i in range(0, len(file_list), subset_size)] 

# 将每个列表的文件保存至各自目录
for index, subset_files in enumerate(file_set):
    # 创建子目录
    subset_floder_path = f"{results_floder_path}/{index}" # python3 f-string 方便编写字符串
    create_floder_safely(subset_floder_path)
    # 逐个保存文件到子目录
    for single_file in subset_files:
        shutil.move(single_file, subset_floder_path)

