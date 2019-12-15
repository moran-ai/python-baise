# coding:gbk
def bulid_profile(fisrt,last,**user_info):
    """
    创建一个字典，其中包含我们知道的有关用户的一切
    形参**user_info中两个星号让python创建一个名为user_info的空字典,
    并将所有收到的名称和值都封装这个空字典中
    在函数体内，创建一个名为progfile的空字典，

    :param fisrt:
    :param last:
    :param user_info:
    :return:
    """
    profile = {}
    # 将名和姓加入到空字典profile中
    profile['first_name'] = fisrt
    profile['last_name'] = last

    # 遍历字典user_info的键值对，并将每个键值对加入到字典profile中
    for key,value in user_info.items():
        # print('key:'+ key)
        # print('value:' + value)
      profile[key] = value
    return profile

user_profile = bulid_profile('albert','einstein',
                             location='princeton',filed='physics')
print(user_profile)
