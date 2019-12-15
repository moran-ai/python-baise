numbers  = list(range(1,6))
print(numbers)

# 指定步长，打印1-10内的偶数
even_number = list(range(2,11,2))   # 第三个2为指定的步长
print(even_number)

# 使用range计算平方和
squers = []  # 先创建一个空列
for value in range(1,11):
    squer = value**2  # 将数字列表中的每一个数的平方赋给变量value
    squers.append(squer)  # 将变量value的值添加到空列表squers中
    squers.append(value**2)
print(squers)   # 打印squers



