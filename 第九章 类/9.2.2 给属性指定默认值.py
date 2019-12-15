# coding:gbk
"""
类中的每个属性都必须有初始值，哪怕这个值是0或者空字符串，如设置默认值时，在方法__init__内指定
这种初始值是可行的，如果你对某个属性这样做了，就无需包含为它提供初始的形参

"""
class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        # 设置的默认值，无须提供初始形参
        self.odometer_reading=0

    def get_descritive_name(self):
        long_time = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_time

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print('This is car has ' + str(self.odometer_reading) + ' miles on it')

my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descritive_name())
my_new_car.read_odometer()
