# coding:gbk
requested_toppings = ['mushrooms','green peppers','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':  # 青椒已卖完
        print('Sorry, we are out of green peppers right now')
    else:
      print('Adding ' + requested_topping + '.')

print('\nFinised making your pizza!')
