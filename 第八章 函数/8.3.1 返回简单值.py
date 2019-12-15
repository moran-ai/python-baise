# coding:gbk
def get_formattmed_name(first_name,last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    # 将结果返回函数调用行
    return full_name.title()
# #
#用于存储返回的值
musician = get_formattmed_name('jimi','hendrix')
print(musician)

# 也可以直接输出
# print('jimi','hendrix')
