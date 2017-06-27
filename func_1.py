# 定义函数
def print_me(value):
    print(value)
    return


# 调用函数
print_me('我要调用用户自定义函数!')
print_me('再次调用同一函数')


def change_int(value):
    value = 10
    return value

b = 2
change_int(b)
print(b)



