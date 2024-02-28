from pyrosetta import init, pose_from_pdb
from pyrosetta.rosetta.core.pack.task.operation import ReadResfile
from pyrosetta.rosetta.core.pack.task import TaskFactory
from pyrosetta.rosetta.protocols.denovo_design.movers import FastDesign
from pyrosetta import create_score_function
init()
init_cmd = '-use_input_sc -corrections::beta_nov16 -corrections::beta_nov16_cart' #开启beta打分函数
init(init_cmd)


pose = pose_from_pdb('C18_PROTEIN.pdb')#输入文件，将此脚本与输入文件放入同一文件夹则不需要添加路径
resfile_type = ReadResfile('C18_368.resfile') #读取resfile
beta_nov16 = create_score_function('beta_nov16') #设置打分函数
pack_tf = TaskFactory() #设置任务工厂
pack_tf.push_back(resfile_type)
final_design = FastDesign(beta_nov16, 5)  #选择打分函数，以及重复次数
final_design.set_task_factory(pack_tf)
final_design.set_default_movemap()
 # final_design.max_iter(200) #最大迭代次数，如果计算时间太长可选择开启此选项
final_design.apply(pose) #开始计算
pose.dump_pdb('debug_final_design22_beta_nov16.pdb') #储存计算结果












