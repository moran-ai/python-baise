# coding:gbk
# ��Ҫ��ȡ���ļ����洢�ڱ���filename��
filename = 'pi_digits.txt'

with open(filename) as file_object:
    # ���ж�ȡ,ʹ��forѭ��
    for line in file_object:
        print(line)
