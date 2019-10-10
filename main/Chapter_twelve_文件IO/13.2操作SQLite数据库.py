import sqlite3




if __name__ == '__main__':
    print(sqlite3.apilevel)
    print(sqlite3.paramstyle)


    # # 使用 connect() 方法打开或创建一个数据库
    # conn = sqlite3.connect('first.db')
    # # 使用 :memory: 特殊名称即可创建内存中的数据库
    # conn1 = sqlite3.connect(":memory:")
    # print(conn, conn1)


    # 1 打开或创建数据库
    # 也可以使用特殊名称 :memory: 创建内存数据库
    conn = sqlite3.connect('first.db')
    # 2 获取游标
    c = conn.cursor()
    # 3 执行 DDL 语句创建数据表
    c.execute('''create table user_tb(
        _id integer primary key autoincrement,
        name text,
        pass text,
        gender text)''')
    # 执行 DDL 语句创建数据表
    c.execute('''create table order_tb(
        _id integer primary key autoincrement,
        item_name text,
        item_price real,
        item_number real,
        user_id integer,
        foreign key(user_id) references user_tb(_id))''')
    # 4 关闭游标
    c.close()
    # 5 关闭连接
    conn.close()

    '''
        注意： SQLite 数据库所支持的 SQL 语句与 MySQL 大致相同，需要指出的是， SQLite 内部只支持 NULL、INTEGER、REAL（浮点数）、TEXT
        和 BLOB（大二进制对象）这5中数据类型，实际上 SQLite 完全可以接受 varchar(n)、char(n)、decimal(p, s)等数据类型，只不过 SQLite
        会在运算或保存时将它们转换为上面5种数据类型中相应的类型。
    '''

    # 由于 SQLite 允许在存入数据时忽略底层数据列世纪的数据类型，因此在编写建表语句时可以省略数据列后面的类型声明（除关键字外），例如：
    '''create table test_tb(
        _id integer primary key autoincrement,
        name ,
        pass ,
        gender
        )'''