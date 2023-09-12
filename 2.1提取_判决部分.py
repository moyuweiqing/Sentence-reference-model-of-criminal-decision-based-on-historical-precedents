import os
import re

filelist = os.listdir('./rename_file')
for filename in filelist:
    file = open(f'./rename_file/{filename}', encoding='utf-8').read()
    panjue = re.findall('判决如下[\s\S]*如不服', file)
    if len(panjue) > 0:
        if len(panjue[0]) > 0:
            judgement = panjue[0][:len(panjue[0]) - len('如不服')]

            new_file_name = filename.split('.')[0] + '_判决部分'
            with open(f'./2.1判决部分/{new_file_name}.txt', encoding='utf-8', mode='w') as f:
                f.write(judgement)
                f.close()

            print('finished', filename)