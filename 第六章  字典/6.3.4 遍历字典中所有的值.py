# coding:gbk
favorite_languages = {'jen':'python',
                      'sarch':'c',
                      'edward':'ruby',
                      'phill':'python'}

# �����ֵ������е�ֵ,ʹ�÷���values()
for v in favorite_languages.values():
    print(v)


print('*'*50)
# ��˳������ֵ��е�����ֵ��ʹ�÷���sorted()
for v in sorted(favorite_languages.values()):
    print(v)

