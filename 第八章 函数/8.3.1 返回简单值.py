# coding:gbk
def get_formattmed_name(first_name,last_name):
    """�������������"""
    full_name = first_name + ' ' + last_name
    # ��������غ���������
    return full_name.title()
# #
#���ڴ洢���ص�ֵ
musician = get_formattmed_name('jimi','hendrix')
print(musician)

# Ҳ����ֱ�����
# print('jimi','hendrix')
