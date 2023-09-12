import re
import os

filelist = os.listdir('./rename_file')
for filename in filelist:
    file = open(f'./rename_file/{filename}', encoding='utf-8').read()
    if '本院认为，' in file:
        considerations = re.findall('本院认为，[\s\S]*判决如下', file)

        if len(considerations) == 1:
            new_file_name = filename.split('.')[0] + '_法院认定'
            with open(f'./2.3法院认定/{new_file_name}.txt', encoding='utf-8', mode='w') as f:
                f.write(considerations[0])
                f.close()

            print('finished', filename)