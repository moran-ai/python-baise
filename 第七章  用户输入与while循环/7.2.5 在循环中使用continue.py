# coding:gbk
# continue���ص�ѭ����ͷ,�������������Ծ����Ƿ����ִ��ѭ��,��ʹ��continue���
# ����break�����������ִ�����µĴ��벢�˳�����ѭ��

current_number = 0
while current_number < 10:
    current_number += 1
    #  ������Ϊ0,pythonִ��continue���,���ص�ѭ����ͷ
    # �����Ϊ0,����continue���
    if current_number %2 ==0:
        continue
    print(current_number)

