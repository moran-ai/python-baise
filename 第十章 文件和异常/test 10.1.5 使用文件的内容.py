# coding:gbk
filename = 'pi_digits.txt'
with open(filename) as f:
    lines = f.readlines( )   # 存入列表

pi_string =''    # 创建一个变量，用来存储圆周率的值

# 使用for循环将各行加入到变量pi_string中
for line in lines:
    pi_string += line.rstrip()   # 方法rstrip()删除末尾的空格
    # pi_string += line.strip()    # 方法strip()删除左边的空格
print(pi_string)
print(len(pi_string))
