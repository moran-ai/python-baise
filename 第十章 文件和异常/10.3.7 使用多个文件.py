# coding:gbk
def count_words(filename):
    """����һ���ļ��д��°������ٸ�����"""
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        msg = "Sorry,the file " + filename + "does not exit"
        print(msg)
    # ʧ��ʱһ������
    # except FileNotFoundError:
    #     pass
    # ��except���������ݸ�Ϊpass����

    else:
        "�����ļ����ж��ٸ�����"
        words = contents.split()
        num_words = len(words)
        print("The file" + filename + "has about " + str(num_words) + "words's")


filenames = 'alice.txt'
# ʹ�ö���ļ�,��filenames��Ϊ�б���

count_words(filenames)