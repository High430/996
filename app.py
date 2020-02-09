用户名 = input('')

if len(用户名) < 3:
    print('用户名必须大于三位')
elif len(用户名) > 10:
    print('用户名不得大于十位')
else:
    print('这名字不错！')

