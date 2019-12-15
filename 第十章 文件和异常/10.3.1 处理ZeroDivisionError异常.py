# coding:gbk
# 如果try中的代码块运行没有问题，python将跳过except代码块
# 如果try代码块中的代码引发了问题，python将运行except 代码块，并运行其中的代码，
# 即其中指定的错误与引发的错误相同
try:
    print(5/0)
except:
    print("You can't divide by zero!")
