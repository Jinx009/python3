import pymysql
try:
    conn = pymysql.connect(host='56f34b014db7d.sh.cdb.myqcloud.com', user='root', passwd='JinxQ007008', db='base', port=5492, charset='utf8')
    cur = conn.cursor()
    cur.execute("UPDATE HOME_USER SET USER_NAME = 'JINX007' WHERE ID = 1")
    conn.commit()
    cur.close()
    conn.close()
except BaseException:
    print('更新失败')