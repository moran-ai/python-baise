# coding:gbk
def build_persion(first_name,last_name):
    """����һ���ֵ䣬���а���һ���й�һ���˵���Ϣ"""
    # ��ֵ��װ���ֵ���
    person = {'first':first_name,'last':last_name}
    return person

musician = build_persion('jimi','hendrix')
print(musician)
print('*'*50)

# �޸�һ�´洢����
# ����һ����ѡ����age
def build_persion(first_name,last_name,age=' '):
    persion = {'first':first_name,'last':last_name}
    if age:
        persion['age'] = age
    return persion

musician = build_persion('john','keer','27')
print(musician)
