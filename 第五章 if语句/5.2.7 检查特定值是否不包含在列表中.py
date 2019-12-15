# coding:gbk
banned_user = ['andrew','caroies','david']
user = 'marice'

# 使用关键字not in
if  user not in banned_user:
    print(user.title() + ', you can post a response if you wish')

