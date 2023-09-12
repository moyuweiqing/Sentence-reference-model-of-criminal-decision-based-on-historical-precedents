import os
import re

filelist = os.listdir('./rename_file')
for filename in filelist:
    file = open(f'./rename_file/{filename}', encoding='utf-8').read()
    if '审理终结' in file:
        defandants = re.findall('[\s\S]*审理终结', file)

        new_file_name = filename.split('.')[0] + '_头部部分'
        with open(f'./2.2头部部分/{new_file_name}.txt', encoding='utf-8', mode='w') as f:
            f.write(defandants[0])
            f.close()

        print('finished', filename)