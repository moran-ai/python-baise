# coding:gbk
"""
���е�ÿ�����Զ������г�ʼֵ���������ֵ��0���߿��ַ�����������Ĭ��ֵʱ���ڷ���__init__��ָ��
���ֳ�ʼֵ�ǿ��еģ�������ĳ�������������ˣ����������Ϊ���ṩ��ʼ���β�

"""
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
my_new_car.read_odometer()
