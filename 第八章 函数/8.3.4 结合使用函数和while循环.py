# coding:gbk
# 形参age为可选参数
def get_formatted_name(first_name,last_name,age=''):
    # 如果有年龄
    if age:
      full_name = first_name + ' ' + last_name + ' ' + age
      return full_name
    # 没有年龄
    else:
        full_name = first_name + ' ' + last_name
        return full_name

# while循环获取实参值
while True:
    print('\nPlease input your name')
    f_name = input('First_name:')
    if f_name == 'q':
        break

    l_name = input('Last_name:')
    if l_name == 'q':
        break

    age = input('age:')
    if age == 'q':
        break

    # 存储返回的值
    musician = get_formatted_name(f_name,l_name)
    print('Hello' + ' ' + musician + '!','you have' + ' ' + age)
