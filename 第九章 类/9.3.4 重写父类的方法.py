# coding:gbk
"""
��д����ķ����������ж���һ���븸����ͬ�ķ�����������Ҫ��д�ĸ��෽��ͬ��.
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
        """�綯����������"""
        print("This car x need a gas tank!")

# ��������,�����������ڵ�ǰ�ļ�����
class ELectriCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)

    # ��д����
    def fill_gas_tank(self):
        """�綯��û������"""
        print("This is car doesn't nedd a gas tank!")

my_car = ELectriCar('tesla','model',2006)
print(my_car.get_descritive_name())
my_car.fill_gas_tank()
