# coding:gbk
# break�����˳�whileѭ��,��������ѭ�������µĴ���,Ҳ�����������ԵĽ�����
prompt = "\nPlease enter the name of a city you have visited"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)
    # if������û�����
    if city == 'q':
        break
    else:
        print("I'd love to go to " + city.title() + '!')

