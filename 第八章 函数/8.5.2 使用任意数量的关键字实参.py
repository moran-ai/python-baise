# coding:gbk
def bulid_profile(fisrt,last,**user_info):
    """
    ����һ���ֵ䣬���а�������֪�����й��û���һ��
    �β�**user_info�������Ǻ���python����һ����Ϊuser_info�Ŀ��ֵ�,
    ���������յ������ƺ�ֵ����װ������ֵ���
    �ں������ڣ�����һ����Ϊprogfile�Ŀ��ֵ䣬

    :param fisrt:
    :param last:
    :param user_info:
    :return:
    """
    profile = {}
    # �������ռ��뵽���ֵ�profile��
    profile['first_name'] = fisrt
    profile['last_name'] = last

    # �����ֵ�user_info�ļ�ֵ�ԣ�����ÿ����ֵ�Լ��뵽�ֵ�profile��
    for key,value in user_info.items():
        # print('key:'+ key)
        # print('value:' + value)
      profile[key] = value
    return profile

user_profile = bulid_profile('albert','einstein',
                             location='princeton',filed='physics')
print(user_profile)
