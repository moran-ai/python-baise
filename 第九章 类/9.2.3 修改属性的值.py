# coding:gbk
# 1.直接修改属性的值
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
# my_new_car.read_odometer()
print('*'*50)
# 直接修改属性的值，最简单的方式是通过实例直接访问，使用句点表示法
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# 2.通过方法修改属性的值
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

#     定义方法修改属性的值
    def update_odometer(self,mileage):
        """将里程读数设为指定的值"""
        self.odometer_reading = mileage
        # 修改属性检查读数是否合理
        if mileage>= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")

my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descritive_name())
# my_new_car.read_odometer()
print("*"*50)
my_new_car.update_odometer(23)
my_new_car.read_odometer()


# 3.通过方法对属性的值进行递增
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

    def update_odometer(self,mileage):
        """将里程读数设为指定的值"""
        self.odometer_reading = mileage

    def increment_odometer(self,miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles

my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descritive_name())
print('*'*50)
my_new_car.update_odometer(23500)
my_new_car.read_odometer()

my_new_car.increment_odometer(100)
my_new_car.read_odometer()

