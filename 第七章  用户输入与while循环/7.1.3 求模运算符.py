# coding:gbk
#  ��ģ�����(%)�������������������
# ��ģ���������ָ��һ��������һ�����Ķ��ٱ�����ָ�������Ƕ���
# ����Ϊ0Ϊż��������Ϊ1Ϊ����

number = input("Enter a number,and I'll tell you id it's even odd:")
number = int(number)

# �ж��Ƿ�Ϊ������ż��
if number%2 == 0:
    print('\nThe number ' +  str(number)  + ' is even ')
else:
    print('\nThe number ' +  str(number)  + ' is odd')

#  ��Python2�汾�У�Ӧʹ��raw_input()����ȡ����
