# coding:gbk
"""
将列表传递给函数后，函数可对其进行修改，在函数中对这个列表所做的任何修改 都是永久性的
"""
# 打印函数print_models有两个形参，一个是需要打印的设计列表,一个是打印好的列表
# 函数体内描述的是函数该怎样去完成工作
def print_modles(unprinted_designs,completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models中
    :param unprinted_designs:
    :param completed_models:
    :return:
    """
    # while 循环模拟打印的过程
    while unprinted_designs:
        # 将未打印的设计存变量current_design中,pop方法从列表末尾删除一个元素
        current_design = unprinted_designs.pop()

        # 模拟根据设计制作3D打印模型的过程
        # 指出正在打印当前的设计
        print('Printing model:' + current_design)
        # print(unprinted_designs[:],current_design)
        # 使用切片表示法unprinted_designs[:]，用来创建列表的副本,使得函数不会修改掉原来的列表
        # 将变量current_design存入打印好的空列表中
        completed_models.append(current_design)

# 显示函数show_completed_models有一个形参，completed_models,用来存放打印好的设计的结果
def show_completed_models(completed_models):
    """
    显示打印好的所有模型
    :param completed_models:
    :return:
    """
    print('\nThe folling models have benn printed')
    # 遍历打印好的列表
    for completed_model in completed_models:
        print(completed_model)

# 给定两个列表,一个是未打印设计的列表，一个是已经打印好设计的空列表
unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []

# 调用函数，将列表传入函数中作为实参
print_modles(unprinted_designs,completed_models)
show_completed_models(completed_models)
