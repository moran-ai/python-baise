# coding:gbk
# 检查超过两个的情形，可使用if-else-elif结构，python只执行if-elif-else中的一个代码块。
age = 12

if age < 4:
    print('You admission cost is $0')
elif age<18:
    print('You admission cost is $5')
else:
    print('You admission cost is $10')
