# coding:gbk
class Dog():
    def __init__(self,name,age):
        """
        ��ʼ������
        :param name:
        :param age:
        # """
        self.name = name
        self.age = age

    # ���巽��
    def set(self):
        print(self.name.title() + 'is now sitting')
        print('yours is '+ str(self.age)+ 'years old')

    def roll_over(self):
        print(self.name.title() + 'rolled over!')

# ����ʵ��
my_dog = Dog('wille',6)

print("My dog's name is " + my_dog.name.title() + '.')
print("My dog is" + str(my_dog.age) + 'years old')

"""
my_dog = Dog('wille',6),���д��룬pythonʹ��ʵ��'wille'��6�������еķ���__init__().
����__init__()����һ����ʾС����ʵ������ʹ�������ṩ��ֵ����������name��age 
ͨ��������Ϊ����ĸ��д�����Ʊ�ʾ�࣬��Сд�ı�ʾ�����ഴ����ʵ��
"""
"""
1.��������
Ҫ����ʵ�������ԣ���ʹ�þ���ʾ������my_dog.name
����ʾ����python�кܳ��ã������﷨��ʾ��python��λ�Ϥ���Ե�ֵ��
�����python���ҵ�ʵ��my_dog���ٲ��������ʵ�������������name����Dog���������������ʱ��ʹ�õ���self.name

"""
# ���÷���
my_dog.set()
my_dog.roll_over()

print('*'*50)
# �������ʵ��
your_dog = Dog('lucy',3)
print("Your's name is " + your_dog.name.title() + '.')
print('You dog is ' + str(your_dog.age) + 'years old')
print('*'*50)
your_dog.set()
your_dog.roll_over()
