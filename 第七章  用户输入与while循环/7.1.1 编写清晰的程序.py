# coding:gbk
# 当使用函数input()时，都应清晰而易于明白的提示
name = input('Please enter to me: ')
print('Hello,' + name + '!')
print('*'*50)

#  创建多行字符串的方式
#  运算符+=在存储在promt中的字符串末尾附加一个字符串
promt = 'If you tell us who you are,we can personalize the message you see: '
promt += '\nwhat is your first name'
name = input(promt)
print('Hello,'+ name + '!')

