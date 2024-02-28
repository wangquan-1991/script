import os

def fix_silent(silent):
    '''
    simple_cyc_pep app的silent输出功能有bug。会额外引入.00这个字符串。
    '''
    print('FIXing output Silent File')
    with open(silent, 'r') as f, open('tmp.silent', 'w') as f1:
        lines = f.readlines()
        # print(lines)
        for line in lines:
            line = line.replace(' .00', '    ')
            line = line.replace(' 3.0    ', '        ')
            line = line.replace(' 2.0    ', '        ')
            line = line.replace(' 4.0    ', '        ')
            line = line.replace(' 5.0    ', '        ')
            line = line.replace(' 6.0    ', '        ')
            line = line.replace(' 7.0    ', '        ')
            line = line.replace(' 8.0    ', '        ')
            line = line.replace(' 9.0    ', '        ')
            line = line.replace(' 1.0    ', '        ')
            f1.write(line)

    os.system('mv -f tmp.silent out.silent')


for i in os.listdir():
    if os.path.isdir(i):
        os.chdir(i)
        os.system('cat *.silent >> ../final_result.silent')
        os.chdir('../')

fix_silent('final_result.silent')
os.system('mv out.silent final_result.silent')

# MV all pdbfile here;
for i in os.listdir():
    if os.path.isdir(i):
        os.chdir(i)
        os.system('mv *.pdb ../')
        os.chdir('../')
