# coding:gbk
# 使用方法remove()

# 创建一个宠物列表
pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']

# 使用while循环删除所有重复的元素,使用方法remove
while 'cat' in pets:
    pets.remove('cat')

print(pets)
