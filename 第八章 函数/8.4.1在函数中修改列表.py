# coding:gbk
"""
���б��ݸ������󣬺����ɶ�������޸ģ��ں����ж�����б��������κ��޸� ���������Ե�
"""
# ��ӡ����print_models�������βΣ�һ������Ҫ��ӡ������б�,һ���Ǵ�ӡ�õ��б�
# ���������������Ǻ���������ȥ��ɹ���
def print_modles(unprinted_designs,completed_models):
    """
    ģ���ӡÿ����ƣ�ֱ��û��δ��ӡ�����Ϊֹ
    ��ӡÿ����ƺ󣬶������Ƶ��б�completed_models��
    :param unprinted_designs:
    :param completed_models:
    :return:
    """
    # while ѭ��ģ���ӡ�Ĺ���
    while unprinted_designs:
        # ��δ��ӡ����ƴ����current_design��,pop�������б�ĩβɾ��һ��Ԫ��
        current_design = unprinted_designs.pop()

        # ģ������������3D��ӡģ�͵Ĺ���
        # ָ�����ڴ�ӡ��ǰ�����
        print('Printing model:' + current_design)
        # print(unprinted_designs[:],current_design)
        # ʹ����Ƭ��ʾ��unprinted_designs[:]�����������б�ĸ���,ʹ�ú��������޸ĵ�ԭ�����б�
        # ������current_design�����ӡ�õĿ��б���
        completed_models.append(current_design)

# ��ʾ����show_completed_models��һ���βΣ�completed_models,������Ŵ�ӡ�õ���ƵĽ��
def show_completed_models(completed_models):
    """
    ��ʾ��ӡ�õ�����ģ��
    :param completed_models:
    :return:
    """
    print('\nThe folling models have benn printed')
    # ������ӡ�õ��б�
    for completed_model in completed_models:
        print(completed_model)

# ���������б�,һ����δ��ӡ��Ƶ��б�һ�����Ѿ���ӡ����ƵĿ��б�
unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []

# ���ú��������б��뺯������Ϊʵ��
print_modles(unprinted_designs,completed_models)
show_completed_models(completed_models)
