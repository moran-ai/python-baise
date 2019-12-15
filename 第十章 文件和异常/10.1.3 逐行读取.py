# coding:gbk
# 将要读取的文件名存储在变量filename中
filename = 'pi_digits.txt'

with open(filename) as file_object:
    # 逐行读取,使用for循环
    for line in file_object:
        print(line)
