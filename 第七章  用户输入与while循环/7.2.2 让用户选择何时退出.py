# coding:gbk
prompt = '\nTell you me something, and I will repeat it back to you:'
prompt += "\nEnter 'quit' to end the program."
message = ''  # �������ַ����������洢�û������ֵ
# python �״�ִ��while���ʱ����Ҫ��message��ֵ��quit ���бȽϣ�����ʱ�û���û�����롣
# ���û�пɹ��ȽϵĶ�����python�޷��������г���Ϊ���������⣬���������messageָ��һ����ʼֵ
# ��Ȼ�����ʼֵֻ��һ���ַ��������Ƿ���Ҫ��
# ֻҪmessage��ֵ����quit,�������ͻ᲻������

while message != 'quit':
    message = input(prompt)
    print(message)
    # if message != 'quit':
    #     #     print(message)
