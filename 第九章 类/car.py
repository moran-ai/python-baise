# coding:gbk
"""һ�������ڱ�ʾ��������"""
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

