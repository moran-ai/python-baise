# coding:gbk
"""
调用模块之前先运行一遍模块文件
将所创建的pizza模块导入进来

import pizza 让python打开pizza 文件，并将其中的所有函数都复制到这个程序中
要调用被导入模块中的函数，可指定导入的名称和函数名
"""
import pizza
# from pizza import  make_pizza
# 调用模块中的函数
pizza.make_pizza(26,'pepprtoni')
pizza.make_pizza(4,'mushrooms','green_peppers','extra_cheese')
