# coding:gbk
# ����Car��
class Car():
    """
    һ��ģ�������ļ򵥳���
    """
    def __init__(self,make,model,year):
        """��ʼ����������������"""
        self.make=make
        self.model=model
        self.year=year

    def get_descriptive_name(self):
        """���������������Ϣ"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name

# ����ʵ��
my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())
