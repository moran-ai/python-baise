# coding:gbk
# break立即退出while循环,不在运行循环中余下的代码,也不管条件测试的结果如何
prompt = "\nPlease enter the name of a city you have visited"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)
    # if语句检查用户输入
    if city == 'q':
        break
    else:
        print("I'd love to go to " + city.title() + '!')

