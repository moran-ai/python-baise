# coding:gbk
# 1.ֱ���޸����Ե�ֵ
class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        # ���õ�Ĭ��ֵ�������ṩ��ʼ�β�
        self.odometer_reading=0

    def get_descritive_name(self):
        long_time = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_time

    def read_odometer(self):
        """��ӡһ��ָ��������̵���Ϣ"""
        print('This is car has ' + str(self.odometer_reading) + ' miles on it')

my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descritive_name())
# my_new_car.read_odometer()
print('*'*50)
# ֱ���޸����Ե�ֵ����򵥵ķ�ʽ��ͨ��ʵ��ֱ�ӷ��ʣ�ʹ�þ���ʾ��
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# 2.ͨ�������޸����Ե�ֵ
class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        # ���õ�Ĭ��ֵ�������ṩ��ʼ�β�
        self.odometer_reading=0

    def get_descritive_name(self):
        long_time = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_time

    def read_odometer(self):
        """��ӡһ��ָ��������̵���Ϣ"""
        print('This is car has ' + str(self.odometer_reading) + ' miles on it')

#     ���巽���޸����Ե�ֵ
    def update_odometer(self,mileage):
        """����̶�����Ϊָ����ֵ"""
        self.odometer_reading = mileage
        # �޸����Լ������Ƿ����
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


# 3.ͨ�����������Ե�ֵ���е���
class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        # ���õ�Ĭ��ֵ�������ṩ��ʼ�β�
        self.odometer_reading=0

    def get_descritive_name(self):
        long_time = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_time

    def read_odometer(self):
        """��ӡһ��ָ��������̵���Ϣ"""
        print('This is car has ' + str(self.odometer_reading) + ' miles on it')

    def update_odometer(self,mileage):
        """����̶�����Ϊָ����ֵ"""
        self.odometer_reading = mileage

    def increment_odometer(self,miles):
        """����̱��������ָ������"""
        self.odometer_reading += miles

my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descritive_name())
print('*'*50)
my_new_car.update_odometer(23500)
my_new_car.read_odometer()

my_new_car.increment_odometer(100)
my_new_car.read_odometer()

