# coding:gbk
filename = 'pi_digits.txt'
with open(filename) as f:
    lines = f.readlines( )   # �����б�

pi_string =''    # ����һ�������������洢Բ���ʵ�ֵ

# ʹ��forѭ�������м��뵽����pi_string��
for line in lines:
    pi_string += line.rstrip()   # ����rstrip()ɾ��ĩβ�Ŀո�
    # pi_string += line.strip()    # ����strip()ɾ����ߵĿո�
print(pi_string)
print(len(pi_string))
