# coding:gbk

'''编写函数时，可给每个形参指定默认值。
在调用函数中给形参提供了实参，python将使用指定的实参值；否则将使用形参的默认值
给形参指定默认值后，可在函数调用中省略相应的实参。
使用默认值可简化函数调用，可清楚的指出函数的典型用法
下面的例子中，给animal_type这个形参指定了默认值,在调用函数时，如果没有给animal_type指定实参,将使用默认值
'''
"""
下面的例子修改了形参的排列顺序,由于给animal_type指定了默认值，无需通过实参来指定动物类型，
在函数调用时，只包含一个实参-宠物的名字。然而，python依然将这个实参视为位置实参，因此如果函数调用中只
包含宠物的名字，这个实参将关联到函数定义的第一个形参，这就是需要将pet_name 放在形参列表开头的原因所在
"""

def describle_pet(pet_name,animal_type='dog'):
    print('\nI have a ' + pet_name)
    print('\nMy ' + animal_type +"'s name is " + pet_name.title() + '.')

describle_pet('wille')

# def describle_pet(animal_type='dog',pet_name):
#
#     print('\nI have a ' + pet_name)
#     print('\nMy ' + animal_type + "'s name is " + pet_name.title() + '.')
#