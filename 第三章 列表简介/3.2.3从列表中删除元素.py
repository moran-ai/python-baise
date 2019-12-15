# 1.使用del语句删除元素
motorcyles = ['honda','yamda','suzuki']
print(motorcyles)

# del根据索引删除元素
del motorcyles[0]  # 删除列表的第一个元素
print(motorcyles)
print('*'* 50)

# 2.使用方法pop()删除元素
motorcyles = ['handa','yamaha','suzuki']
print(motorcyles)

# pop()方法删除列表末尾的元素
# 列表可以看成是一个栈，pop方法就是找出栈顶元素
popped_motorcyles = motorcyles.pop()
print(motorcyles)   # 删除后的列表
print(popped_motorcyles)   # 打印出删除的值

# 实际上，可以使用pop方法删除任意位置的值,指定删除索引即可
print(motorcyles.pop(0))
print('*'* 50)

# 3.根据值删除元素,使用方法remove()
motorcyles = ['honda','suzuki','ducati']
print(motorcyles)

motorcyles.remove('ducati')
print(motorcyles)

