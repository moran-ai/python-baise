# coding:gbk
# 可使用while循环提示用户输入任意数量的信息

# 创建一个空字典
reponses = {}

# 设置一个标志，指出是否继续
polling_active = True

while polling_active:
    # 提示输入被调查者的名字和回答
    name = input('\nWhat is your name:')
    reponse = input('\nWhich mountain would you like to climb someday?')

    # 将答案填充到字典中
    reponses[name] = reponse

    # 看看是否还有人要参与调查
    repeat = input('\nWould you like to anthoner person repond?(yes/no)')
    if repeat == 'no':
        polling_active = False

# 调查结束，显示调查结果
print('\n---Poll Results')
for reponse in reponses.items():
    print(reponse)

