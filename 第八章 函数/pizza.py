# coding:gbk
def make_pizza(size,*toppings):
    """
    ����Ҫ����������
    :param size:
    :param toppings:
    :return:
    """
    print('\nMaking a ' + str(size) + '-inch pizza with the following toppings:')

    for topping in toppings:
        print('-'+ topping)

