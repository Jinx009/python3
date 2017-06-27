# 打开一个文件
fo = open('/Users/jinx/Downloads/temp.txt', 'wb')
all_the_text = 'hello python'
fo.write(bytes(all_the_text, encoding='utf-8'))
print('文件名: ', fo.name)
print('是否已关闭 : ', fo.closed)
print('访问模式 : ', fo.mode)
