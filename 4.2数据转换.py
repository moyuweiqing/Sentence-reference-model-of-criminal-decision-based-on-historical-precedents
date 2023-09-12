import pandas as pd
from datetime import datetime

file = pd.read_excel('./4.1合并后数据.xlsx')

del file['被告人_x']
del file['被告人_y']
del file['文件名']

def date_change(date):
    try:
        date = str(date)
        year = date.split('年')[0]
        month = date.split('年')[1].split('月')[0]
        day = date.split('月')[1].split('日')[0]
        new_date = year + '-' + month + '-' + day
        date_obj = datetime.strptime(new_date, '%Y-%m-%d')
        return date_obj
    except:
        return ''

file['t1'] = file['审判时间'].apply(date_change)
file['t2'] = file['生日'].apply(date_change)
file['t1'] = pd.to_datetime(file['t1'])
file['t2'] = pd.to_datetime(file['t2'])
file['判决时被告人年龄'] = (file['t1'].dt.year - file['t2'].dt.year)

gendar_dic = {'男': 1, '女': 0}
education_dic = {'无': 0,
                 '小学': 1, '小学一年级': 1, '小学肄业': 1,
                 '初小': 2, '初中': 2,
                 '中专': 3, '中技': 3, '高中': 3,
                 '大专': 4, '专科': 4, '大学专科': 4,
                 '大学': 5, '大学本科': 5,
                 '硕士研究生': 6}

del file['t1']
del file['t2']
del file['审判时间']
del file['生日']

file['性别'] = file['性别'].map(gendar_dic)
file['学历'] = file['学历'].map(education_dic)

file.to_excel('./4.2转化后数据.xlsx', index=False, encoding='gb18030')