class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0    # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)

    def count2(self):
        print(self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)

try:
    print(counter.__secretCount)
except AttributeError:
    print('不能调用非公有属性!')
else:
    print('ok!')
