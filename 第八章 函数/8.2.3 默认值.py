# coding:gbk

'''��д����ʱ���ɸ�ÿ���β�ָ��Ĭ��ֵ��
�ڵ��ú����и��β��ṩ��ʵ�Σ�python��ʹ��ָ����ʵ��ֵ������ʹ���βε�Ĭ��ֵ
���β�ָ��Ĭ��ֵ�󣬿��ں���������ʡ����Ӧ��ʵ�Ρ�
ʹ��Ĭ��ֵ�ɼ򻯺������ã��������ָ�������ĵ����÷�
����������У���animal_type����β�ָ����Ĭ��ֵ,�ڵ��ú���ʱ�����û�и�animal_typeָ��ʵ��,��ʹ��Ĭ��ֵ
'''
"""
����������޸����βε�����˳��,���ڸ�animal_typeָ����Ĭ��ֵ������ͨ��ʵ����ָ���������ͣ�
�ں�������ʱ��ֻ����һ��ʵ��-��������֡�Ȼ����python��Ȼ�����ʵ����Ϊλ��ʵ�Σ�����������������ֻ
������������֣����ʵ�ν���������������ĵ�һ���βΣ��������Ҫ��pet_name �����β��б�ͷ��ԭ������
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