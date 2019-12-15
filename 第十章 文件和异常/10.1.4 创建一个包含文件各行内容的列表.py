# coding:gbk
filename = 'pi_digits.txt'

with open(filename) as file_object:
    # 方法readlines()从文件中读取每一行,并将其存储在一个列表
    lines = file_object.readlines()
    # print(lines)

for line in lines:
    print(line)
