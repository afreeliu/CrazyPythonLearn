import time
'''
    time 模块主要包含各种提供日期、时间功能的类和函数。该模块提供了把日期、时间格式化为字符串的功能，也提供了从字符串恢复日期时间的功能
'''

if __name__ == '__main__':
    print([e for e in dir(time) if not e.startswith('_')])
    # time 模块中提供了一个time.struct_time类，该类代表一个时间对象，她主要包含9个属性，
    # stm = time.struct_time
    # stm.tm_year: 年
    # stm.tm_mon: 月
    # stm.tm_mday: 日
    # stm.tm_hour: 时
    # stm.tm_min: 分
    # stm.tm_sec: 秒
    # stm.tm_wday: 周，周一为0，范围为0-6
    # stm.tm_yday: 一年内第几天，范围为1～366
    # stm.tm_isdst: 夏令时 0、1或-1

    # 将时间元组或struct_time转换为时间字符串。如果不指定参数t，则默认转换当前时间
    print(time.asctime())
    # 将以秒数代表的时间转换为时间字符串
    print(time.ctime(30))