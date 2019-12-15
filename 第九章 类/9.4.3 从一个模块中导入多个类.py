# coding:gbk
from my_car import Car,ElectriCar

my_beetle = Car("volkswagen",'beetle',2016)
print(my_beetle.get_descriptive_name())

my_beetle = ElectriCar('tesla','roadster',2016)
print(my_beetle.get_descriptive_name())