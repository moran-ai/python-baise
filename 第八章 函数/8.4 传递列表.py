#coding:gbk
def greet_users(names):
    """���б��е�ÿλ�û������򵥵��ʺ�"""
    #  �����б�,����ӡ���б��Ԫ��
    for name in names:
        msg = 'Hello' + ' ' +  name.title() + ' '+ '!'
        print(msg)

# ����һ���б�
usernames = ['hannah','ty','margot']

# ���ú��������б��ݸ�����
greet_users(usernames)
