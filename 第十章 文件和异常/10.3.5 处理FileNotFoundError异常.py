# coding:gbk
filename = 'alice.txt'

with open(filename,'w')as f:
    f.write('jkfkdskjnasdfkl\n')
    f.write('huajkl;asdfqweryuoasdfasdfds')
try:
  with open(filename) as f:
      contents = f.read()
except FileNotFoundError:
    msg = "Sorry ,the file " + filename + 'does not exit'
    print(msg)

# ȷ���ļ��а������ٸ�����
else:
    # �����ļ��а������ٸ�����
    words = contents.split()  # �ָ�
    # print(words)
    num_words = len(words)
    print("The file" + filename + "has about " + str(num_words) + ' words')

