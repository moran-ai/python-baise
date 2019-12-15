# coding:gbk

def describle_pet(animal_type,pet_name):
    "显示宠物的信息"
    print('\nI have a ' + animal_type + '.')
    print("\nMy " + animal_type + "'s name is " + pet_name + '.')

describle_pet('hamster','harry')

#  调用函数多次
describle_pet('dog','willie')

# 位置实参的顺序很重要
