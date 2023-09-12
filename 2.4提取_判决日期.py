import re
import os
import pandas as pd

filelist = os.listdir('./rename_file')

NUM = {'零': 0, '一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9, '十': 10, '〇': 0, '○': 0, 'Ｏ': 0, 'O': 0}

info_table = pd.DataFrame(columns=['文件名', '审判时间'])

for filename in filelist:
    file = open(f'./rename_file/{filename}', encoding='utf-8').read()
    t = re.findall('二(.*?)日', file)
    if len(t) > 0:
        try:
            time_ch = t[-1]
            year = time_ch.split('年')[0][1:]
            month = time_ch.split('年')[1].split('月')[0]
            day = time_ch.split('年')[1].split('月')[1].split('日')[0]

            year = '20' + ''.join(str(NUM[i]) for i in year)
            month = ''.join(str(NUM[i]) for i in month)
            day = ''.join(str(NUM[i]) for i in day)

            # 月处理(例如"十二"月转换为"102",只取"1"和"2")
            if len(month) == 3:
                month = '1' + month[2]
            # 日处理(例如"二十"日转换为"210",只取"2"和"0")
            if len(day) == 3:
                day = day[0] + day[2]

            # 月处理(例如"十二"月转换为"102",只取"1"和"2")
            if len(month) == 3:
                month = '1' + month[2]
            # 日处理(例如"二十"日转换为"210",只取"2"和"0")
            if len(day) == 3:
                day = day[0] + day[2]
            # 日处理(例如"二十一"日转换为"2101",只取"2"和"1")
            elif len(day) == 4:
                day = day[0] + day[3]

            # 将各部分进行拼接组合
            new_date = (year + '年' + month + '月' + day + '日')

            id = filename.split('.')[0]
            alist = [id, new_date]
            info_table.loc[len(info_table)] = alist
        except Exception as e:
            print(e)
            continue

info_table.to_excel('./2.4判决日期.xlsx', index=False, encoding='gb18030')