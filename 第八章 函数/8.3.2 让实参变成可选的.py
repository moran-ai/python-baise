# coding:gbk
"""
���������˶����м�������������������ֻ�ṩ���պ���������������ȷ�����У�
Ϊ�����м�����ɿ�ѡ�ģ��ɸ��β�middke_nameָ��Ĭ��ֵ,һ�����ַ���
"""
def get_formatted_name(first_name,last_name,middle_name=''):
    """�������������"""
    # ������м���
    if middle_name:
        full_name = first_name + ' ' + last_name + ' ' + middle_name
    # ���û���м���
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

# �洢���ص�ֵ
musician = get_formatted_name('jimi','hendrix')
print(musician)

musician = get_formatted_name('john','hooker','lee')
print(musician)
