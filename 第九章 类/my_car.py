# coding:gbk
"""一组用于表示燃油汽车和电动汽车的类"""
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
        """打印一条信息，指出汽车的里程"""
        print("This Car has "+str(self.odometer_reading)+" miles on it")

    def update_odometer(self,mileag):
        """
        将里程表读数设置为指定的值
        拒绝将里程表往回放
        :return:
        """
        if mileag >= self.odometer_reading:
            self.odometer_reading = mileag
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self,miles):
        """将里程增加至指定的值"""
        self.odometer_reading += miles

class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""
    def __init__(self,battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的信息"""
        print("This car has a" + str(self.battery_size) + "-kwh battery")

    def get_range(self):
        """打印一条描述电瓶续航里程的信息"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 70

        message = 'This car can go approximatly' + str(range)
        message+="miles on a full change"
        print(message)

class ElectriCar(Car):
    """模拟电动车的独特之处"""
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

        super().__init__(make,model,year)
        self.battery = Battery()