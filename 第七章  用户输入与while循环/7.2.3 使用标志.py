# coding:gbk
# ��Ҫ��ܶ�����������ʱ�ż������еĳ����У��ɶ���һ�������������ж����������Ƿ��ڻ״̬��
# �����������Ϊ��־,�䵱�˳���Ľ�ͨ�źŵ�
# �����־ΪTrueʱ��������,�����־ΪFalseʱֹͣ����
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program"   # ���ַ���prompt��ĩβ���һ��

# ʹ�ñ�־
active = True
while active:
    message = input(prompt)
    #  if��������message��ֵ
    if message == 'quit':
        active =False
    else:
        print(message)
