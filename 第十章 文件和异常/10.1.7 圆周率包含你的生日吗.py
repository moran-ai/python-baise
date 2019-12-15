# coding:gbk
filename = 'pi_digits.txt'
with open(filename) as f:
    lines = f.readlines()

pi_string =  ''
for line in lines:
    pi_string += line.rstrip()

birthday = input('Enter you birthday,in the mmddyy:')
if birthday in pi_string:
    print('Your birthday appears in the first millon digtits of pi!')
else:
    print('Your birthday does not appers in the fisrt milloin digits of pi!')
    