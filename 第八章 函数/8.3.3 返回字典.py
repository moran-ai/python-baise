# coding:gbk
def build_persion(first_name,last_name):
    """返回一个字典，其中包含一个有关一个人的信息"""
    # 将值封装到字典中
    person = {'first':first_name,'last':last_name}
    return person

musician = build_persion('jimi','hendrix')
print(musician)
print('*'*50)

# 修改一下存储年龄
# 增加一个可选参数age
def build_persion(first_name,last_name,age=' '):
    persion = {'first':first_name,'last':last_name}
    if age:
        persion['age'] = age
    return persion

musician = build_persion('john','keer','27')
print(musician)
