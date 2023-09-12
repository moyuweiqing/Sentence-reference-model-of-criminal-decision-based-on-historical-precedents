import os
import pandas as pd

filelist = os.listdir('./result')

def num_format(num):
    if num < 10:
        return str('000' + str(num))
    elif num < 100:
        return str('00' + str(num))
    elif num < 1000:
        return str('0' + str(num))
    elif num < 10000:
        return str(num)

cnt = 1
info_table = pd.DataFrame(columns=['原文件名', '新文件名'])

for filename in filelist:
    file = open(f'./result/{filename}', encoding='utf-8').read()

    new_file_name = 'GYSR_' + num_format(cnt)
    alist = [filename, new_file_name]
    info_table.loc[len(info_table)] = alist

    with open(f'./rename_file/{new_file_name}.txt', encoding='utf-8', mode='w') as f:
        f.write(file)
        f.close()

    cnt += 1

info_table.to_excel('./1.判决书id重定义.xlsx', encoding='gb18030', index=False)