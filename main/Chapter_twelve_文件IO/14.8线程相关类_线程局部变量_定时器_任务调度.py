
from concurrent.futures import ThreadPoolExecutor
import threading
import time
'''
    Python 还为线程并发提供了一些工具函数，如 threading.local() 函数deng。
    
    线程局部变量
    
    Python 在 threading 模块下提供了一个 local() 函数，该函数可以返回一个线程局部变量，通过使用线程局部变量可以很简捷地隔离多线程访问
    的竞争资源，从而简化多线程并发访问的编程处理。
    线程局部变量（Thread Local Variable）的功用其实非常简单，就是为每一个使用该变量的线程都提供一个变量的副本，使每一个线程都可以独立地
    改变自己的副本，而不会和其他线程的副本冲突。从线程的角度看，就好像每一个线程都完全拥有该变量一样



    定时器
    
    Thread 类有一个 Timer 子类，该子类可用于控制指定函数在特定时间内执行一次
    
    
    任务调度
    
    如果需要执行更复杂的任务调度，则可用 Python 提供的 sched 模块。该模块提供了 sched.scheduler 类，该类代表一个任务调度器
    
'''

# 定义线程局部变量
# my_data = threading.local()
# # 定义准备作为线程执行体使用的函数
# def action(max):
#     for i in range(max):
#         try:
#             my_data.x += i
#         except:
#             my_data.x = i
#         # 访问 my_data 的 x 的值
#         print('%s my_data.x 的值为： %d' % (threading.currentThread().getName(), my_data.x))
#
# # 使用线程池启动两个子线程
# with ThreadPoolExecutor(max_workers=2) as pool:
#     pool.submit(action, 10)
#     pool.submit(action, 10)


# 定时器
# def hello():
#     print('hello world !')
#
# # 指定 10s 后执行 hello 函数
# t = threading.Timer(10.0, hello)
# t.start()

# 如果程序想取消 Timer 的调度，则可调用 Timer 对象的 calcel() 函数

# 定义总共输出几次的计数器
count = 0
def print_time():
    print('当前时间： %s' % time.ctime())
    global t, count
    count += 1
    # 如果 count 小于 10，开始下一次调度
    if count < 10:
        t = threading.Timer(1, print_time)
        t.start()
# 指定 1s 后执行 print_time 函数
t = threading.Timer(1, print_time)
t.start()