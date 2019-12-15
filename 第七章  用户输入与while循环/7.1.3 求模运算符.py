# coding:gbk
#  求模运算符(%)，两个数相除返回余数
# 求模运算符不会指出一个数是另一个数的多少倍，而指出余数是多少
# 余数为0为偶数，余数为1为奇数

number = input("Enter a number,and I'll tell you id it's even odd:")
number = int(number)

# 判断是否为奇数或偶数
if number%2 == 0:
    print('\nThe number ' +  str(number)  + ' is even ')
else:
    print('\nThe number ' +  str(number)  + ' is odd')

#  在Python2版本中，应使用raw_input()来获取输入
