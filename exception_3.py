try:
    fh = open('testfile', 'w', encoding='utf-8')
    try:
        fh.write('这是一个测试文件，用于测试异常!!')
    finally:
        print('关闭文件')
        fh.close()
except IOError:
    print('Error: 没有找到文件或读取文件失败')
