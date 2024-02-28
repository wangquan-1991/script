import os
import glob
# 指定要标记为FIXED的残基编号  
fixed_residues = [1, 2, 3, 4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,26,27,28,29] 
pdb_dir = '/data/wq/glp-1/fa_MP/G3_20_25/R1_AF2/AF2_pdb/'
#pdb_list = os.listdir(pdb_dir) 
pdb_list = glob.glob(os.path.join(pdb_dir, '*.pdb'))  

#for pdb in pdb_list:
for pdb in pdb_list:  
    # 打开PDB文件并删除以REMARK开头的行  
    with open(pdb, 'r') as file:  
        lines = file.readlines()  
        filtered_lines = [line for line in lines if not line.startswith('REMARK')]  
      
    # 生成固定标签并追加到文件末尾  
    remarks = []  
    for res_id in fixed_residues:  
        remark = f"REMARK PDBinfo-LABEL:{res_id: >5} FIXED"  
        remarks.append(remark)  
    remarks_str = '\n'.join(remarks)  
    filtered_lines.append(remarks_str)  
      
    # 写入更新后的内容到文件  
    with open(pdb, 'w') as file:  
        file.writelines(filtered_lines)
  # 生成固定标签
#  remarks = []
#  for res_id in fixed_residues:
#    remark = f"REMARK PDBinfo-LABEL:{res_id: >5} FIXED"
 #   remarks.append(remark)
  
 # remarks_str = '\n'.join(remarks)

  # 打开PDB文件追加标签 
 # with open(pdb) as f:
 #   content = f.read()
 #   content += '\n'
 #   content += remarks_str
#
#  with open(pdb, 'w') as f:
 #   f.write(content) 

print('DONE')

