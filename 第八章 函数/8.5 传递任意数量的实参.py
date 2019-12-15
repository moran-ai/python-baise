# coding:gbk

def make_pizza(*toppings):
    """
    函数只有一个形参*toppings,其中*是让python创建一个名为topping的元组,
    并将收到的所有的值都装在这个元组中
    :param toppings:
    :return:
    """
    # 打印顾客点的所有配料
    print(toppings)

# 调用函数
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')
