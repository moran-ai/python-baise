# coding:gbk
# �β�ageΪ��ѡ����
def get_formatted_name(first_name,last_name,age=''):
    # ���������
    if age:
      full_name = first_name + ' ' + last_name + ' ' + age
      return full_name
    # û������
    else:
        full_name = first_name + ' ' + last_name
        return full_name

# whileѭ����ȡʵ��ֵ
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

    # �洢���ص�ֵ
    musician = get_formatted_name(f_name,l_name)
    print('Hello' + ' ' + musician + '!','you have' + ' ' + age)
