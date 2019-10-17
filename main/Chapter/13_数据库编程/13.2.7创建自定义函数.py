
import sqlite3

'''
    数据库连接对象还提供了一个 create_function(name, num_params, func) 方法，该方法用于注册一个自定义函数，接下来程序就可以在 SQL 语句中
    实用该自定义函数。该方法包含了 3 个参数。
    
    name： 指定注册的自定义函数的名字
    num_params： 指定自定义函数所需参数的个数
    func： 指定自定义函数对应的函数

'''

# 先定义一个普通函数，准备注册为 SQL 语句中的自定义函数
def reverse_ext(st):
    # 对字符串反转，前后添加方括号
    return '[' + st[::-1] + ']'

if __name__ == '__main__':
    # 1 打开数据库或者创建数据库
    conn = sqlite3.connect('first.db')
    # 调用 create_function 注册自定义函数: enc
    conn.create_function('enc', 1, reverse_ext)

    # 2 获取游标
    c = conn.cursor()
    # 3 在 SQL 语句中实用 enc 自定义函数
    c.execute('insert into user_tb values (null, ?, enc(?), ?)', ('贾宝玉', '123456789', 'male'))
    # 4 提交事务
    conn.commit()
    # 5 关闭游标
    c.close()
    # 关闭数据库连接
    conn.close()
