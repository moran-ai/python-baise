# coding:gbk
# ��ʹ��whileѭ����ʾ�û�����������������Ϣ

# ����һ�����ֵ�
reponses = {}

# ����һ����־��ָ���Ƿ����
polling_active = True

while polling_active:
    # ��ʾ���뱻�����ߵ����ֺͻش�
    name = input('\nWhat is your name:')
    reponse = input('\nWhich mountain would you like to climb someday?')

    # ������䵽�ֵ���
    reponses[name] = reponse

    # �����Ƿ�����Ҫ�������
    repeat = input('\nWould you like to anthoner person repond?(yes/no)')
    if repeat == 'no':
        polling_active = False

# �����������ʾ������
print('\n---Poll Results')
for reponse in reponses.items():
    print(reponse)

