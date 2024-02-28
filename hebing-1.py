import pandas
import numpy


# 读取不同的csv
df1 = pandas.read_csv('score2.csv')

df2 = pandas.read_csv('score3.csv')

#合并产出新CSV
df = pandas.concat([df1],[df2] )

df.to_csv('final-all.csv')
