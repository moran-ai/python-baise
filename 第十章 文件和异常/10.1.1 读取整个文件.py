# coding:gbk

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
    # print(contents.rstrip())  rstrip() ɾ��ĩβ�Ŀհ�
    """
    ����open()���ļ�
    ������,open('pi_digits.txt')����һ����ʾ�ļ�pi_digits.txt�Ķ���
    python ���������洢���ں���Ҫ�õ��ı�����
    �ؼ���with�ڲ���Ҫ�����ļ�����ر�
    ���Ե���open��close���򿪺͹ر��ļ�
    �������close�����ܻ����bug
    ʹ�÷���read ��ȡ����ļ�����������
    ��������Ϊһ���������ַ����洢�ڱ���contents��
    
    """