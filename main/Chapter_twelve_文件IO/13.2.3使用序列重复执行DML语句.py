import sqlite3
'''
    使用游标的 execute() 方法也可以执行 DML 的 insert、update、delete 语句，这样即可对数据库执行插入、更新和删除数据操作。
'''

if __name__ == '__main__':
    # 1 打开或创建数据库
    conn = sqlite3.connect('first.db')
    # 2 获取游标
    cursor = conn.cursor()
    # 3 执行 insert 语句插入数据
    cursor.execute('insert into user_tb values (null, ?, ?, ?)', ('孙悟空', '123456', 'male'))
    cursor.execute('insert into order_tb values (null, ?, ?, ?, ?)', ('鼠标', '34.2', '3', 1))

    # 使用 executemany() 方法则可以执行同一条 SQL 语句
    cursor.executemany('insert into user_tb values (null, ?, ?, ?)',
                       (('zhang', '12', 'female'),
                       ('sun', '23', 'male'),
                        ('zai', '34', 'female')))

    cursor.executemany('update user_tb set name=? where _id = ?',
                       (('小白', 2),
                        ('小黑', 3),
                        ('小红', 4)))
    print(cursor.lastrowid)

    # 4 提交事务
    conn.commit()
    # 5 关闭游标
    cursor.close()
    # 6 关闭连接
    conn.close()