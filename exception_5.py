class GodCheck(ValueError):
    ERROR = ("-1", "这是个傻逼！")


def check(name):
    if name == '俊杰':
        raise GodCheck(GodCheck.ERROR[0],
                       GodCheck.ERROR[1])
    else:
        print('This is a god')


try:
    check('俊杰')
except GodCheck as msg:
    print("errCode:", msg.args[0])
    print("errMsg:", msg.args[1])
