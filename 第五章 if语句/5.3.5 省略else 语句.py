# coding:gbk
#  并不要求if-elif-else结构后面必须要有else代码块,在某些特定的情况下，可以省略else语句

age = 180

if age < 4:
    print('price=0')
elif age < 18:
    print('price=5')
elif age < 65:
    print('price=10')
elif age >= 65:
    print('price=5')
