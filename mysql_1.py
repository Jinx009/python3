import pymysql
try:
    conn = pymysql.connect(host='56f34b014db7d.sh.cdb.myqcloud.com', user='root', passwd='JinxQ007008', db='base', port=5492, charset='utf8')
    cur = conn.cursor()
    cur.execute('SELECT  * FROM HOME_USER')
    data = cur.fetchall()
    for d in data:
        print("id: "+str(d[0])+' 密码：'+d[2])
    cur.close()
    conn.close()
except BaseException:
    print('查询失败')
