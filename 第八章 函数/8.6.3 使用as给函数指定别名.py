# coding:gbk
"""
指定别名的通用语法
from module_name import function_name as fn
"""
# 给函数make_pizza指定别名mp
from pizza import make_pizza as mp

mp(16,'pepperoni')
mp(36,'mushrooms')
