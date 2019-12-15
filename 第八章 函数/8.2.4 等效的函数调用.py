# coding:gbk
def describle_pet(pet_name,animal_type='dog'):
    print('\nI have a ' + pet_name)
    print('\nMy ' + animal_type + "'s name is " + pet_name.title() + '.')

#  一只名为willie的小狗
describle_pet('willie')
describle_pet(pet_name='willie')

# 一只名为Harry的仓鼠
describle_pet('harry','hamster')
describle_pet(pet_name='harry',animal_type='hamster')

