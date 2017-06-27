# 打开一个文件
fo = open('/Users/jinx/Downloads/temp.txt', 'r+')
value = fo.read(128)
print('读取的字符串是 : ', value)
# 关闭打开的文件
fo.close()
