import os
import re
import pandas as pd

info_table = pd.DataFrame(columns=['文件', '自首', '坦白', '立功', '认罪', '认罚', '悔罪', '谅解', '偶犯', '初犯', '中止', '未遂', '情节, 严重', '情节, 轻', '社会, 危害性, 严重', '恶劣', '被害人, 过错'])

def cut_sentences(content):
    # 指定切分标点
    pattern = r'\。|\！|\;|\；'
    sentences = re.split(pattern, content)
    return sentences

# 判断是否有这些行为，简单的文本判断
def if_have_behavior(sentence, keywords):
    for keyword in keywords:
        if keyword not in sentence:
            return ''
    if '不' in sentence:
        return 0
    else:
        return 1

filelist = os.listdir('./2.3法院认定')
for filename in filelist:
    file = open(f'./2.3法院认定/{filename}', encoding='utf-8').read()
    sentences = cut_sentences(file)

    judgewords = {'自首': '', '坦白': '', '立功': '', '认罪': '', '认罚': '', '悔罪': '', '谅解': '', '偶犯': '', '初犯': '',
                 '中止': '', '未遂': '', '情节,严重': '', '情节,轻': '', '社会,危害性,严重': '', '恶劣': '', '被害人,过错': ''}

    for sentence in sentences:
        for judgeword in judgewords:
            if judgewords[judgeword] == '':
                para_words = judgeword.split(',')
                judgewords[judgeword] = if_have_behavior(sentence, para_words)

    alist = list(judgewords.values())
    new_file_name = filename.split('_法院')[0]
    alist.insert(0, new_file_name)
    info_table.loc[len(info_table)] = alist

info_table.to_excel('./3.3特征_法院认定.xlsx', encoding='gb18030', index=False)