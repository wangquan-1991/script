import pandas
import glob


file_list = glob.glob("*csv")
save_file_name = "all.csv"

if save_file_name in file_list:
    file_list.remove(save_file_name)

df_all = []
for file_s in file_list:
    df = pandas.read_csv(file_s, index_col=False)
    df_all = df_all + [df]
df_finalfinal = pandas.concat(df_all)
df.to_csv(save_file_name, index=False) 
