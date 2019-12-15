# coding:gbk
request_toppings = []   # 给定一个空列表
if request_toppings:   # 进行检查
    for request_topping in request_toppings:
        print('Adding' + request_topping + '.')   # 检查不为空，返回的值
else:
    print('Are you sure you want a plain pizza!')  # 为空，返回的值
