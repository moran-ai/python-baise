# coding:gbk
"""
重写父类的方法：子类中定义一个与父类相同的方法，即它与要重写的父类方法同名.
"""
class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def get_descritive_name(self):
        long_time = str(self.year) + ' ' + self.make + ' ' + self.model + ' .'
        return  long_time

    def fill_gas_tank(self):
        """电动汽车有油箱"""
        print("This car x need a gas tank!")

# 创建子类,父类必须包含在当前文件夹中
class ELectriCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)

    # 重写父类
    def fill_gas_tank(self):
        """电动车没有油箱"""
        print("This is car doesn't nedd a gas tank!")

my_car = ELectriCar('tesla','model',2006)
print(my_car.get_descritive_name())
my_car.fill_gas_tank()
