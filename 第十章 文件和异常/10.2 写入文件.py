# coding:gbk
filename = 'programming.txt'
"""
参数：
w:写入模式
r:读取模式
a:附加模式
r+:读取写入模式
如果省略了模式实参，python将以默认的只读模式打开
调用open，有两个实参
"""

"""
如果你要写入的文件不存在，python将自动创建它，但是，如果以写入模式('w')打开文件时
要千万小心，因为如果指定的文件已经存在，python将在返回文对象前清空文件
"""
with open(filename,'w') as f:
    f.write('I love programming')

# 写入多个文件
    f.write('I love creating new games')

# with open(filename,'w') as f:
    # f.write('agfg')