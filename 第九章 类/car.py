# coding:gbk
"""一个可用于表示汽车的类"""
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

