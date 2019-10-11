import sqlite3

'''
    标准的 SQL 语句提供了如下 5 个标准的聚集函数
    sum(): 统计总和
    avg(): 统计平均值
    count(): 统计记录条数
    max(): 统计最大值
    min(): 统计最小值
    
    如果程序需要在 SQL 语句中使用与其他业务相关的聚集函数，则可使用数据库连接对象所提供的 create_aggregate(name, num_params, aggregate_class)
    方法，该方法用于注册一个自定义的聚集函数。该方法包含了 3 个参数。
    name: 指定自定义聚集函数的名字
    num_params: 指定聚集函数所需的参数
    aggregate_class: 指定聚集函数的实现类。该类必须实现 step(self, params...) 和 finalize(self) 方法，其中 step()方法对于查询所
    返回的每条记录各执行一次； finalize(self) 方法只在最后执行一次，该方法的返回值将作为聚集函数最后的返回值
'''

# 需要自定义聚集函数，需要先定义一个普通类
class MinLen:
    def __init__(self):
        self.min_len = None

    def step(self, value):
        print('执行了step')
        # 如果 self.min_len 还没有赋值，则直接将当前的 value 赋值给 self.min_len
        if self.min_len is None:
            self.min_len = value
            return
        # 找到一个长度更短的 value， 用 value 代替 self.min_len
        if len(self.min_len) > len(value):
            self.min_len = value

    def finalize(self):
        print('执行了finalize')
        return self.min_len




if __name__ == '__main__':
    # 1 打开或者创建数据库
    conn = sqlite3.connect('first.db')
    # 调用 create_aggregate() 方法创建自定义聚集函数
    conn.create_aggregate('min_len', 1, MinLen)
    # 2 获取游标
    c = conn.cursor()
    # 3 在 SQL 语句中使用 min_len 自定义聚集函数
    c.execute('select min_len(pass) from user_tb')
    print(c.fetchone())
    conn.commit()
    c.close()
    conn.close()
