# coding:gbk
# 继承
# 子类的方法_init_
"""
创建子类的实例时，python首先需要完成的任务是给父类的所有属性赋值
"""
class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    # 定义一个获取里程表读数的方法
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name

    # 定义一个读取里程表数的方法
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + "miles on it!")

    # 定义一个方法修改属性的值
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    # 定义一个对属性的进行递增的方法
    def increment_odometer(self,miles):
        self.odometer_reading += miles

# 创建子类
class ELectricCar(Car):
    """
    电动汽车的独特之处
    """
    # 子类的方法_init_
    def _init_(self,make,model,year):
        """
        初始化父类的属性
        :param make:
        :param model:
        :param year:
        :return:
        """
        # super 是一个特殊的函数，这个函数将子类和父类关联起来
        # 这行代码调用父类的方法，并继承父类中所有的属性
        super.__init__(make,model,year)

# 创建实例
# 这行代码首先调用子类中定义的方法_init_,ElectricCar
# 后者调用父类Car类中定义的方法,并提供了三个实参,tesla,model,2016
my_tesla = ELectricCar('tesla','model',2016)
print(my_tesla.get_descriptive_name())
