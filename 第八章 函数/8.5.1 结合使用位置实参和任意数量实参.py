# coding:gbk
def make_pizza(size,*toppings):
    """
    函数有两个形参,一个大小，一个元组
    函数收到的第一个值存储到size中，其他值存储到*topping中
    param size:
    :param topping:
    :return:
    """
    # 概述要制作的披萨
    print('\nMaking a ' + str(size) +
          " -inch pizza with the following toppings:")
#   遍历配料的值
    for topping in toppings:
        print(topping)

# 调用函数
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')
