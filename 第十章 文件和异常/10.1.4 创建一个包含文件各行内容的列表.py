# coding:gbk
filename = 'pi_digits.txt'

with open(filename) as file_object:
    # ����readlines()���ļ��ж�ȡÿһ��,������洢��һ���б�
    lines = file_object.readlines()
    # print(lines)

for line in lines:
    print(line)
