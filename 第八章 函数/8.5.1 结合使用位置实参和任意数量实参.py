# coding:gbk
def make_pizza(size,*toppings):
    """
    �����������β�,һ����С��һ��Ԫ��
    �����յ��ĵ�һ��ֵ�洢��size�У�����ֵ�洢��*topping��
    param size:
    :param topping:
    :return:
    """
    # ����Ҫ����������
    print('\nMaking a ' + str(size) +
          " -inch pizza with the following toppings:")
#   �������ϵ�ֵ
    for topping in toppings:
        print(topping)

# ���ú���
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')
