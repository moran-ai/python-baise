# coding:gbk
# 用while循环来处理列表和字典
# 在列表之间移动元素,使用方法pop和append

# 首先，创建一个待验证用户列表
# 和一个用于存储已验证用户的列表
unconfirmed_users = ['alice','brain','candace']
confrimed_users = []

# 验证每个用户，直到没有未验证用户为止
# 将每个经过验证的列表都移到已验证用户列表中
# while循环
while unconfirmed_users:
    current_users = unconfirmed_users.pop()
    confrimed_users.append(current_users)

# 显示所有已验证用户
for confirmed_user in confrimed_users:
    print(confirmed_user)
