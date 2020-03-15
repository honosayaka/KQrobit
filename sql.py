# 导入pymysql模块
import pymysql
# 连接database
def getStat():
    conn = pymysql.connect(host='49.234.98.122', user='root', password='123456789a', database='foruse')
    # 得到一个可以执行SQL语句的光标对象
    cursor = conn.cursor()
    # 定义要执行的SQL语句  UPDATE runoob_tbl
    #         SET runoob_title="学习 Python"
    #         WHERE runoob_id=3';
    sql2 = '''SELECT times FROM suyi WHERE id = 1;'''
    cursor.execute(sql2)
    r = cursor.fetchall()
    # 关闭光标对象
    cursor.close()
    # 关闭数据库连接
    conn.close()
    return r[0][0]




def mi1(setNub):
    conn = pymysql.connect(host='49.234.98.122', user='root', password='123456789a', database='foruse')
    # 得到一个可以执行SQL语句的光标对象
    cursor = conn.cursor()
    # 定义要执行的SQL语句  UPDATE runoob_tbl
    #         SET runoob_title="学习 Python"
    #         WHERE runoob_id=3';
    sql = 'UPDATE suyi SET times ='+str(setNub)+' WHERE id=1;'
    # 执行SQL语句
    cursor.execute(sql)
    r = cursor.fetchall()
    # 关闭光标对象
    conn.commit()
    cursor.close()
    # 关闭数据库连接
    conn.close()
    return r
#
#'''
'''
INSERT INTO table_name (列1, 列2,...) VALUES (值1, 值2,....)
'''
def add_uuid(uuid):
    conn = pymysql.connect(host='49.234.98.122', user='root', password='123456789a', database='foruse')
    # 得到一个可以执行SQL语句的光标对象
    cursor = conn.cursor()
    # 定义要执行的SQL语句  UPDATE runoob_tbl
    #         SET runoob_title="学习 Python"
    #         WHERE runoob_id=3';
    sql = 'INSERT INTO uuids (uuid) VALUES (' + str(uuid) + ');'
    # 执行SQL语句
    cursor.execute(sql)
    # 关闭光标对象
    conn.commit()
    cursor.close()
    # 关闭数据库连接
    conn.close()



def get_uuids():
    conn = pymysql.connect(host='49.234.98.122', user='root', password='123456789a', database='foruse')
    # 得到一个可以执行SQL语句的光标对象
    cursor = conn.cursor()
    # 定义要执行的SQL语句  UPDATE runoob_tbl
    #         SET runoob_title="学习 Python"
    #         WHERE runoob_id=3';
    sql = 'SELECT uuid FROM uuids;'
    # 执行SQL语句
    cursor.execute(sql)
    t = cursor.fetchall()
    l = []
    for i in range(0, len(t)):
        l.append(t[i][0])
    # 关闭光标对象
    conn.commit()
    cursor.close()
    # 关闭数据库连接
    conn.close()
    return l
# while True:
#     now = getStat()
#     a = input()
#     print('now is ', now)
#     print(mi1(now - 1))
def insert_msg(who, msg):
    conn = pymysql.connect(host='49.234.98.122', user='root', password='123456789a', database='foruse')
    # 得到一个可以执行SQL语句的光标对象
    cursor = conn.cursor()
    sql = '''INSERT INTO chatlog (TIME,who,msg) VALUES (NOW(),%s,%s);''' % (who, msg)
    # 执行SQL语句
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    # 关闭数据库连接
    conn.close()