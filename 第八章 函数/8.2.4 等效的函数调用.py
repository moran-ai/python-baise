# coding:gbk
def describle_pet(pet_name,animal_type='dog'):
    print('\nI have a ' + pet_name)
    print('\nMy ' + animal_type + "'s name is " + pet_name.title() + '.')

#  һֻ��Ϊwillie��С��
describle_pet('willie')
describle_pet(pet_name='willie')

# һֻ��ΪHarry�Ĳ���
describle_pet('harry','hamster')
describle_pet(pet_name='harry',animal_type='hamster')

