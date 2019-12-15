# coding:gbk
def count_words(filename):
    """计算一个文件中大致包含多少个单词"""
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        msg = "Sorry,the file " + filename + "does not exit"
        print(msg)
    # 失败时一声不吭
    # except FileNotFoundError:
    #     pass
    # 将except代码块的内容改为pass即可

    else:
        "计算文件中有多少个单词"
        words = contents.split()
        num_words = len(words)
        print("The file" + filename + "has about " + str(num_words) + "words's")


filenames = 'alice.txt'
# 使用多个文件,将filenames改为列表即可

count_words(filenames)