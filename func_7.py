globvar = 0

def set_globvar_to_one():
    global globvar    # 使用 global 声明全局变量
    globvar = 1

def print_globvar():
    print(globvar)     # 没有使用 global

set_globvar_to_one()
print(globvar)        # 输出 1
print_globvar()       # 输出 1，函数内的 globvar 已经是全局变量