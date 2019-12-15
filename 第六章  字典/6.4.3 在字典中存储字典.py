# coding:gbk
# 字典嵌套,只能有一个键，可以包含多个值
# 下面的示例中，创建了aeinstenin和mcuile两个键
user = {
    'aeinstenin':{
        'first':'albert',
        'last':'einstenin',
        'location':'princetion'
    },
    'mcuile':{
        'first':'marie',
        'last':'cuire',
        'location':'parits'
    }
}

# 遍历字典
for user_name,user_info in user.items():
    print(user_name,user_info)

