#子文件夹生成silent文件
for i in os.listdir():
    if os.path.isdir(i):
        os.chdir(i)
        os.system('cat *.silent >> ../final_result_{}.silent'.format(i))
        os.chdir('../')