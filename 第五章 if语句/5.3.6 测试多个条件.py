# coding:gbk
# if-elif-else结构功能强大，但是只适合只有一个条件满足的情况。
# 想要有多个条件满足，应使用一系列不包含elif和else的代码块

requested_toppings = ['mushrooms','extra cheese']

if 'mushrooms' in requested_toppings:
    print('Adding mushrooms')
if 'pepperoni' in requested_toppings:
    print('Adding popperoni')
if 'extra' in requested_toppings:
    print('Adding extra cheese')

