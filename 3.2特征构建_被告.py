import re
import os
import pandas as pd

info_table = pd.DataFrame(columns=['文件', '被告人', '生日', '性别', '学历', '前科次数'])

filelist = os.listdir('./2.2头部部分')
for filename in filelist:
    file = open(f'./2.2头部部分/{filename}', encoding='utf-8').read()
    defendants = re.findall('被告人.*，.*?\n', file)
    for defendant in defendants:

        # 被告人姓名
        try:
            name = re.findall('被告人(.*)?[,。，]', defendant)[0]
            name = name.split(',')[0].split('，')[0].split('。')[0].split('(')[0].split('（')[0].split('被告人')[-1]
        except:
            name = ''

        # 生日
        try:
            birthday = re.findall('\d{4}年\d{1,2}月\d{1,2}日[出]?生', defendant)[0]
            birthday = birthday.split('生')[0].split('出')[0]
        except:
            birthday = ''

        # 性别
        if '男' in defendant:
            gendar = '男'
        elif '女' in defendant:
            gendar = '女'
        else:
            gendar = ''

        # 文化水平
        try:
            education = re.findall('.*文化', defendant)[0]
            education = education.split('，')[-1].split(',')[-1].split('文化')[0]
        except:
            try:
                education = re.findall('.*肄业', defendant)[0]
                education = education.split('，')[-1].split(',')[-1].split('肄业')[0]
            except:
                education = ''

        if len(education) > 10:
            education = ''

        # 前科
        criminal_record = defendant.count('判处')

        id = filename.split('_头部')[0]
        if birthday != '' and gendar != '':
            alist = [id, name, birthday, gendar, education, criminal_record]
            info_table.loc[len(info_table)] = alist

info_table.to_excel('./3.2特征_头部.xlsx', index=False, encoding='gb18030')