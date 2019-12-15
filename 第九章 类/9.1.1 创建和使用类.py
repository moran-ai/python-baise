# coding:gbk
"""
面向对向编程是最有效的软件编写方法之一
基于类创建对象时，每个对像都自动具备这种通用行为.
然后可根据需要赋予每个对象独特的个性
根据类创建对象称为实例化
使用类几乎可以模拟任何东西
在python中首字母大写的指的是类
"""

# 创建Dog类
class Dog():
    """
    一次模拟小狗的简单尝试
    """
    def __init__(self,name,age):
        """ 初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over")

"""
方法__init__,在这个方法的名称中，开头和末尾都有两个下划线，这是一种约定，旨在避免与python中
默认方法与普通方法发生名称冲突.
将方法定义成了包括三个形参self,name,age,在这个方法的定义中，形参self必不可少，还必须位于其他形参的前面
包含self的原因：python调用这个__init__()方法来创建实例时，将自动传入实参self，每个与类相关联的方法
都自动传递实参self，它是一个指向实例本身的引用，让实例能够访问类中的属性和方法.

self.name=name 获取存储在形参name中的值，并将其存储在变量name中
self.age=age 与其作用相似

"""
