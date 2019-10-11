
import sqlite3


'''
    在标准的 SQL 语句中提供了一个 order by 子句，该子句用于对查询结果进行排序，但这种排序只会按默认的排序规则进行，如果程序需要按业务相关
    规则进行排序，则需要创建自定义的比较函数

    如果程序需要在 SQL 语句中使用与业务相关的比较函数，则可使用数据库连接对象所提供的 create_collation(name, callable) 方法，该方法用于
    注册一个自定义的比较函数。该方法包含两个参数。
    name: 指定自定义比较函数的名字
    callable: 指定自定义比较函数对应的函数。该函数包含两个参数，并对这两个参数进行大小比较，如果该方法返回正整数，系统认为第一个参数更大；
            如果返回负整数，系统认为第二个参数更大；如果返回0，系统认为两个参数相等。
'''

# 比较密码列中的密码的大小，因为第一个字符和倒数第一个字符添加了[]，所以需要排除
def my_collation(st1, st2):
    if st1 == st2:
        return 0
    elif st1 > st2:
        return 1
    else:
        return -1

if __name__ == '__main__':

    # 1 打开或者创建数据库
    conn = sqlite3.connect('first.db')

    # 使用 create_collation() 方法注册自定义比较函数
    conn.create_collation('sub_cmp', my_collation)

    # 2 获取游标
    c = conn.cursor()

    # 3 在 SQL 语句中使用自定义比较函数
    c.execute('select * from user_tb order by pass collate sub_cmp')
    # 采用 for-in 循环遍历游标
    for row in c:
        print(row)
    conn.commit()
    c.close()
    conn.close()