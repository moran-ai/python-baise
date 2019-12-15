# coding:gbk
"""
并非所有人都有中间名，如果调用这个函数只提供了姓和名，它将不能正确的运行，
为了让中间名变成可选的，可给形参middke_name指定默认值,一个空字符串
"""
def get_formatted_name(first_name,last_name,middle_name=''):
    """返回整洁的姓名"""
    # 如果有中间名
    if middle_name:
        full_name = first_name + ' ' + last_name + ' ' + middle_name
    # 如果没有中间名
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

# 存储返回的值
musician = get_formatted_name('jimi','hendrix')
print(musician)

musician = get_formatted_name('john','hooker','lee')
print(musician)
