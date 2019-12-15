#coding:gbk
def greet_users(names):
    """向列表中的每位用户发出简单的问候"""
    #  遍历列表,并打印出列表的元素
    for name in names:
        msg = 'Hello' + ' ' +  name.title() + ' '+ '!'
        print(msg)

# 定义一个列表
usernames = ['hannah','ty','margot']

# 调用函数，将列表传递给函数
greet_users(usernames)
