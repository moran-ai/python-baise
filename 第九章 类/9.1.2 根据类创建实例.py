# coding:gbk
class Dog():
    def __init__(self,name,age):
        """
        初始化属性
        :param name:
        :param age:
        # """
        self.name = name
        self.age = age

    # 定义方法
    def set(self):
        print(self.name.title() + 'is now sitting')
        print('yours is '+ str(self.age)+ 'years old')

    def roll_over(self):
        print(self.name.title() + 'rolled over!')

# 创建实例
my_dog = Dog('wille',6)

print("My dog's name is " + my_dog.name.title() + '.')
print("My dog is" + str(my_dog.age) + 'years old')

"""
my_dog = Dog('wille',6),这行代码，python使用实参'wille'和6调用类中的方法__init__().
方法__init__()创建一个表示小狗的实例，并使用我们提供的值来设置属性name和age 
通常可以认为首字母大写的名称表示类，而小写的表示根据类创建的实例
"""
"""
1.访问属性
要访问实例的属性，可使用句点表示法，如my_dog.name
句点表示法在python中很常用，这种语法演示了python如何获悉属性的值。
在这里，python先找到实例my_dog，再查找与这个实例相关联的属性name，在Dog类中引用这个属性时，使用的是self.name

"""
# 调用方法
my_dog.set()
my_dog.roll_over()

print('*'*50)
# 创建多个实例
your_dog = Dog('lucy',3)
print("Your's name is " + your_dog.name.title() + '.')
print('You dog is ' + str(your_dog.age) + 'years old')
print('*'*50)
your_dog.set()
your_dog.roll_over()
