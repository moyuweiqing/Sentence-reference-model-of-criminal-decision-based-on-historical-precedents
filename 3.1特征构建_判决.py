import os
import re
import pandas as pd

filelist = os.listdir('./2.1判决部分')
info_table = pd.DataFrame(columns=['文件', '被告人', '罪名', '主刑', '时长'])

def split_penalty(penelty):
    if '死刑' in penelty:
        return '死刑', ''
    elif '无期徒刑' in penelty:
        return '无期徒刑', ''
    elif '有期徒刑' in penelty:
        return '有期徒刑', str(penelty).split('刑')[1].split('（')[0]
    else:
        return '', ''

for filename in filelist:
    file = open(f'./2.1判决部分/{filename}', encoding='utf-8').read()
    ts = re.findall('被告人(.*?)犯(.*?)罪[,，]判处(.*?)[,，。；]', file)
    for t in ts:
        id = filename.split('_判决')[0]
        penalty, dutation = split_penalty(t[2])
        alist = [id, t[0], t[1], penalty, dutation]
        info_table.loc[len(info_table)] = alist

info_table.to_excel('./3.1特征_判决.xlsx', index=False, encoding='gb18030')