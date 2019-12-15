# coding:gbk
prompt = '\nTell you me something, and I will repeat it back to you:'
prompt += "\nEnter 'quit' to end the program."
message = ''  # 创建空字符串，用来存储用户输入的值
# python 首次执行while语句时，需要将message的值与quit 进行比较，但此时用户还没有输入。
# 如果没有可供比较的东西，python无法继续运行程序，为解决这个问题，必须给变量message指定一个初始值
# 虽然这个初始值只是一个字符串，但是符合要求
# 只要message的值不是quit,这个程序就会不断运行

while message != 'quit':
    message = input(prompt)
    print(message)
    # if message != 'quit':
    #     #     print(message)
