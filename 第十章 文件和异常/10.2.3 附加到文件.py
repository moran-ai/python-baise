# coding:gbk
filename = 'programming.txt'
"""
实参:
'a':附加到文件末尾，不会覆盖文件原本的内容
"""
with open(filename,'a') as f:
    f.write('I also love finding meaning in large datasets.\n')
    f.write('I love creating apps that can run in a browser.\n')
