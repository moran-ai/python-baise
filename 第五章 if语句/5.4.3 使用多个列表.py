# coding:gbk
avaliable_toppings = ['mushrooms','olvies','green pepoers','pepperoni','pineapple',
                      'extra cheese']
requestedzz_toppings = ['mushrooms','frensh fries','extra cheese']

for requestedzz_topping in requestedzz_toppings:  # ����requestedzz_topping�е�����Ԫ��
    if requestedzz_topping in avaliable_toppings: # �ж�requestedzz_topping�е�Ԫ���Ƿ���avaliable_topping��
        print('Adding  ' + requestedzz_topping)
    else:
        print("Sorry, we don't have" + requestedzz_topping)
