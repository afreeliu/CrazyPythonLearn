
import sqlite3

'''
    SQLite 数据库模块的游标对象还包含了一个 executescript() 方法，这不是一个标准的 API 方法，这意味着在其他数据库 API 模块中可能没有
    这个方法。但是这个方法却很实用，他可以执行一段 SQL 脚本
'''

if __name__ == '__main__':

    # 1 打开或者创建数据库
    conn = sqlite3.connect('first.db')
    # 2 获取游标
    c = conn.cursor()
    # 3 调用 executescript() 方法执行一段 SQL 脚本
    c.executescript('''
        insert into user_tb values (null, '武松', '3444', 'male');
        insert into user_tb values (null, '林冲', '4444', 'male');
        create table item_tb(_id integer primary key autoincrement, name , price);
    ''')
    conn.commit()
    c.close()
    conn.close()