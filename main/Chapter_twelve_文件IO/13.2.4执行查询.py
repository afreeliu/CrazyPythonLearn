import sqlite3


if __name__ == '__main__':

    # 1 打开或者创建数据库
    conn = sqlite3.connect('first.db')
    # 2 获取游标
    c = conn.cursor()
    # 3 执行查询语句
    c.execute('select * from user_tb where _id > 2')
    print('查询返回的记录数：', c.rowcount)
    # 4 通过游标的 description 属性获取列信息
    print(c.description)
    for col in (c.description):
        print(col[0], end='\t')
    print('\n---------------------')
    # while True:
    #     # 获取一条记录，每行数据都是一个元组
    #     row = c.fetchone()
    #     # 如果获取的 row 为 None，则退出循环
    #     if not row:
    #         break
    #     print(row)
    #     print(row[1] + '-------->' + row[2])

    while True:
        # 每次获取多条数据记录
        rows = c.fetchmany(3)
        # 如果获取的 rows 为 None，则退出循环
        if not rows:
            break
        # 再次使用循环遍历所获取的列表
        for row in rows:
            print(row)

    # 一般经历避免使用 fetchall() 方法获取所有查询的结果，因为不知道查询的结果有多少条数据，如果查询的结果过大，内存的开销将很大

    c.close()
    conn.close()
