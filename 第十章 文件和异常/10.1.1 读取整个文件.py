# coding:gbk

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
    # print(contents.rstrip())  rstrip() 删除末尾的空白
    """
    函数open()打开文件
    在这里,open('pi_digits.txt')返回一个表示文件pi_digits.txt的对象
    python 将这个对象存储到在后面要用到的变量中
    关键字with在不需要访问文件后将其关闭
    可以调用open和close来打开和关闭文件
    如果调用close，可能会出现bug
    使用方法read 读取这个文件的整个内容
    并将其作为一个长长的字符串存储在变量contents中
    
    """