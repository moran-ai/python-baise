# coding:gbk
# 10.4.1 使用json.dump()和json.load()
"""
函数json接收两个参数：要存储的数据以及存储数据的文件对象
"""
import json

# 创建数字列表
numbers = [2,3,5,7,11,13]

# 存储数据的文件名称
filename = 'numbers.json'

# 以写入的方式打开文件
with open(filename,'w') as json_f:
    # 使用函数json.dump()将数据存储到numbers.json中
    json.dump(numbers,json_f)

with open(filename) as json_f:
    # 使用json.load()将这个列表读取到内存中
    number = json.load(json_f)
    print(number)
