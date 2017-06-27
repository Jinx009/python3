# 自定义异常错误
class myError(ValueError):
    ERROR = ("-1", "没有该用户！")


# 抛出异常测试函数
def check(level):
    if level > 1:
        raise myError(myError.ERROR[0],  # 异常错误参数1
                  myError.ERROR[1])  # 异常错误参数2


try:
    check(2)
except myError as msg:
    print("errCode:", msg.args[0])  # 获取异常错误参数1
    print("errMsg:", msg.args[1])  # 获取异常错误参数2
