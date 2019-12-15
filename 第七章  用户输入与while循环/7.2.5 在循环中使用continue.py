# coding:gbk
# continue返回到循环开头,并根据条件测试决定是否继续执行循环,可使用continue语句
# 不像break语句那样不在执行余下的代码并退出整个循环

current_number = 0
while current_number < 10:
    current_number += 1
    #  如果结果为0,python执行continue语句,并回到循环开头
    # 结果不为0,跳过continue语句
    if current_number %2 ==0:
        continue
    print(current_number)

