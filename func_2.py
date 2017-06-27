# 可写函数说明
def change_value(my_list):
    my_list.append([1, 2, 3, 4])
    print('函数内取值: ', my_list)
    return


# 调用changeme函数
my_list = [10, 20, 30]
change_value(my_list)
print('函数外取值: ', my_list)
