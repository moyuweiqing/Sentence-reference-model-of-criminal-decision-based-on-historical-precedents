import re
import os

filelist = os.listdir('./result')
# filelist = ['姜志会故意杀人罪一审刑事判决书.txt']
for filename in filelist:
    try:
        file = open(f'./result/{filename}', encoding='utf-8').read()
        t = re.findall('(.*?)\n', file)
        sp = t[0]
        tt = re.findall(f'{sp}[\s\S]*{sp}', file)
        if len(tt) == 1:
            newtt = tt[0]
            newfile = newtt[:len(newtt)-len(sp)]
        elif len(tt) == 0:
            newfile = file
        else:
            continue

        with open(f'./result2/{filename}', encoding='utf-8', mode='w') as f:
            f.write(newfile)
            f.close()
        print('finished', filename)
    except Exception as e:
        print(e, filename)