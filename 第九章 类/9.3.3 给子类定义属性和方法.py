# coding:gbk
# �̳�
# ����ķ���_init_
"""
���������ʵ��ʱ��python������Ҫ��ɵ������Ǹ�������������Ը�ֵ
"""

class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    # ����һ����ȡ��̱�����ķ���
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name

    # ����һ����ȡ��̱����ķ���
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + "miles on it!")

    # ����һ�������޸����Ե�ֵ
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    # ����һ�������ԵĽ��е����ķ���
    def increment_odometer(self,miles):
        self.odometer_reading += miles

# ��������,�����������ڵ�ǰ�ļ�����
# ����
class ELectricCar(Car):
    """
    �綯�����Ķ���֮��
    """

    # ����ķ���__init__
    def __init__(self,make,model,year):

        """
        ��ʼ�����������
        :param make:
        :param model:
        :param year:
        :return:
        """

        # super() ��һ������ĺ������������������͸����������
        # ���д�����ø���ķ��������̳и��������е�����
        super().__init__(make,model,year)

        # ��ʼ���綯������������
        self.battery_size = 70
        # �����Ը����ʼֵ

        """
        ����ElenctricCar�ഴ��������ʵ����������������� ,
        ��������Carʵ������������
        """

    #  ���ຯ��
    def descirbe_battery(self):

        """
        ��ӡһ��������ƿ��������Ϣ
        :return:
        """
        print("This car has a " + str(self.battery_size) + "-kwh battery")

# ����ʵ��
# ���д������ȵ��������ж���ķ���_init_,ElectricCar
# ���ߵ��ø���Car���ж���ķ���,���ṩ������ʵ��,tesla,model,2016
my_tesla = ELectricCar('tesla','model',2016)
print(my_tesla.get_descriptive_name())

# �������ඨ��ķ���
my_tesla.descirbe_battery()
