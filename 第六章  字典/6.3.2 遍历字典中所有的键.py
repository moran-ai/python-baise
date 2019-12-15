# coding:gbk
favorite_languags = {'jen':'python',
                     'sarah':'c',
                     'edward':'ruby',
                     'phill':'python'}

# 遍历所有的键使用方法keys()
# 遍历字典时，会默认遍历所有的键
for k in favorite_languags.keys():
    print('\nkey:' + k)
