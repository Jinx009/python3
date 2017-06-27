import os
try:
    os.rename('/Users/jinx/Downloads/temp.txt', '/Users/jinx/Downloads/test.txt')
    print('操作成功')
except IOError:
    print('操作失败')
else:
    print('else')