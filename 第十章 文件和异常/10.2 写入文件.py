# coding:gbk
filename = 'programming.txt'
"""
������
w:д��ģʽ
r:��ȡģʽ
a:����ģʽ
r+:��ȡд��ģʽ
���ʡ����ģʽʵ�Σ�python����Ĭ�ϵ�ֻ��ģʽ��
����open��������ʵ��
"""

"""
�����Ҫд����ļ������ڣ�python���Զ������������ǣ������д��ģʽ('w')���ļ�ʱ
Ҫǧ��С�ģ���Ϊ���ָ�����ļ��Ѿ����ڣ�python���ڷ����Ķ���ǰ����ļ�
"""
with open(filename,'w') as f:
    f.write('I love programming')

# д�����ļ�
    f.write('I love creating new games')

# with open(filename,'w') as f:
    # f.write('agfg')