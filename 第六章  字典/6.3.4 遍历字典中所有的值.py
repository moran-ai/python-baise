# coding:gbk
favorite_languages = {'jen':'python',
                      'sarch':'c',
                      'edward':'ruby',
                      'phill':'python'}

# 遍历字典中所有的值,使用方法values()
for v in favorite_languages.values():
    print(v)


print('*'*50)
# 按顺序遍历字典中的所有值，使用方法sorted()
for v in sorted(favorite_languages.values()):
    print(v)

