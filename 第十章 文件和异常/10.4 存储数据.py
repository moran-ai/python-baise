# coding:gbk
# 10.4.1 ʹ��json.dump()��json.load()
"""
����json��������������Ҫ�洢�������Լ��洢���ݵ��ļ�����
"""
import json

# ���������б�
numbers = [2,3,5,7,11,13]

# �洢���ݵ��ļ�����
filename = 'numbers.json'

# ��д��ķ�ʽ���ļ�
with open(filename,'w') as json_f:
    # ʹ�ú���json.dump()�����ݴ洢��numbers.json��
    json.dump(numbers,json_f)

with open(filename) as json_f:
    # ʹ��json.load()������б��ȡ���ڴ���
    number = json.load(json_f)
    print(number)
