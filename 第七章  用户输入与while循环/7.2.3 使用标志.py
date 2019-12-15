# coding:gbk
# 在要求很多条件都满足时才继续运行的程序中，可定义一个变量，用于判断整个程序是否处于活动状态。
# 这个变量被称为标志,充当了程序的交通信号灯
# 程序标志为True时继续运行,程序标志为False时停止运行
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program"   # 在字符串prompt的末尾添加一行

# 使用标志
active = True
while active:
    message = input(prompt)
    #  if语句检查变量message的值
    if message == 'quit':
        active =False
    else:
        print(message)
