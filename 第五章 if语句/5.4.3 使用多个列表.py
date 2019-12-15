# coding:gbk
avaliable_toppings = ['mushrooms','olvies','green pepoers','pepperoni','pineapple',
                      'extra cheese']
requestedzz_toppings = ['mushrooms','frensh fries','extra cheese']

for requestedzz_topping in requestedzz_toppings:  # 遍历requestedzz_topping中的所有元素
    if requestedzz_topping in avaliable_toppings: # 判断requestedzz_topping中的元素是否在avaliable_topping中
        print('Adding  ' + requestedzz_topping)
    else:
        print("Sorry, we don't have" + requestedzz_topping)
