# coding:gbk
# ��whileѭ���������б���ֵ�
# ���б�֮���ƶ�Ԫ��,ʹ�÷���pop��append

# ���ȣ�����һ������֤�û��б�
# ��һ�����ڴ洢����֤�û����б�
unconfirmed_users = ['alice','brain','candace']
confrimed_users = []

# ��֤ÿ���û���ֱ��û��δ��֤�û�Ϊֹ
# ��ÿ��������֤���б��Ƶ�����֤�û��б���
# whileѭ��
while unconfirmed_users:
    current_users = unconfirmed_users.pop()
    confrimed_users.append(current_users)

# ��ʾ��������֤�û�
for confirmed_user in confrimed_users:
    print(confirmed_user)
