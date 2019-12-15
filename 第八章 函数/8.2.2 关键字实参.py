# coding:gbk
# 关键字形参是传递给函数的名称-值对
def describe_pet(anmail_type,pet_name):
    "显示宠物的信息"
    print('\nI have a ' + anmail_type +'.')
    print("\nMy" + anmail_type +"'s name is "+pet_name + '.')

# 关键字形\实参
describe_pet(anmail_type='hamster',pet_name='harry')
describe_pet(anmail_type='dog',pet_name='jd')
