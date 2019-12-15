# coding:gbk
"""һ�����ڱ�ʾȼ�������͵綯��������"""
class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_time = str(self.year) + self.make + ' ' + self.model  +  ' .'
        return long_time

    def read_odometer(self):
        """��ӡһ����Ϣ��ָ�����������"""
        print("This Car has "+str(self.odometer_reading)+" miles on it")

    def update_odometer(self,mileag):
        """
        ����̱��������Ϊָ����ֵ
        �ܾ�����̱����ط�
        :return:
        """
        if mileag >= self.odometer_reading:
            self.odometer_reading = mileag
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self,miles):
        """�����������ָ����ֵ"""
        self.odometer_reading += miles

class Battery():
    """һ��ģ��綯������ƿ�ļ򵥳���"""
    def __init__(self,battery_size=70):
        """��ʼ����ƿ������"""
        self.battery_size = battery_size

    def describe_battery(self):
        """��ӡһ��������ƿ��������Ϣ"""
        print("This car has a" + str(self.battery_size) + "-kwh battery")

    def get_range(self):
        """��ӡһ��������ƿ������̵���Ϣ"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 70

        message = 'This car can go approximatly' + str(range)
        message+="miles on a full change"
        print(message)

class ElectriCar(Car):
    """ģ��綯���Ķ���֮��"""
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

        super().__init__(make,model,year)
        self.battery = Battery()