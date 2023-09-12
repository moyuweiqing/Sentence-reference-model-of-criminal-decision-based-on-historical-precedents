import pandas as pd

file1 = pd.read_excel('./3.1特征_判决.xlsx')
file2 = pd.read_excel('./3.2特征_头部.xlsx')
file3 = pd.read_excel('./3.3特征_法院认定.xlsx')
file4 = pd.read_excel('./2.4判决日期.xlsx')

# 选定只涉及到一个被告人的判决书
tmpfile = file1.groupby(['文件']).count()
tmpfile.reset_index(inplace=True)
filelist = list(tmpfile[tmpfile['被告人'] == 1]['文件'])

# 文件选择
file1 = file1[file1['文件'].isin(filelist) == True]
file2 = file2[file2['文件'].isin(filelist) == True]
file3 = file3[file3['文件'].isin(filelist) == True]
file4 = file4[file4['文件名'].isin(filelist) == True]

file = pd.merge(left=file1, right=file2, left_on='文件', right_on='文件')
file = pd.merge(left=file, right=file3, left_on='文件', right_on='文件')
file = pd.merge(left=file, right=file4, left_on='文件', right_on='文件名')
file.to_excel('./4.1合并后数据.xlsx', index=False, encoding='gb18030')