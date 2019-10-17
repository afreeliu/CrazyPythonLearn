
from concurrent.futures import ThreadPoolExecutor
import threading
import time
import sched
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
    sched.scheduler(timefunc=time.monotionic, delayfunc=time.sleep) 构造器支持两个参数
        timefunc: 该参数指定生成时间戳的时间函数，默认使用 time.monotionic 来生成时间戳。
        delayfunc: 该参数指定阻塞程序的函数，默认使用 time.sleep 函数来阻塞程序。
    
    sched.scheduler 调度器支持如下常用属性和方法
    scheduler.enterabs(time, priority, action, argument=(), kwargs={}): 指定在 time 时间点执行 action 函数，argument 和 kwargs 
        都用于向 action 函数传入参数，其中 argument 使用位置参数的形式传入参数； kwargs 使用关键字参数的形式传入参数。该方法返回一个 event，
        它可作为 cancel() 方法的参数用于取消调度。priority 参数指定该任务的优先级，当在同一个时间点有多个任务需要执行时，优先级高（值越小
        表示优先级越高）的任务会优先执行。
    scheduler.enter(delay, priority, action, argument=(), kwargs={}): 该方法和上一个方法基本相同，只是 delay 参数用于指定多少秒
        后执行 action() 函数
    scheduler.cancel(event): 取消任务。如果传入的 event 参数不是当前调度队列中的 event， 程序将会引发 ValueError 异常。
    scheduler.empty(): 判断当前该调度器的调度队列是否为空。
    scheduler.run(blocking=True): 运行所有需要调度的任务。如果调用该方法的 blocking 参数为 True，该方法将会阻塞线程，知道所有被调度的
        任务都执行完成
    scheduler.queue: 该只读属性返回该调度器的调度队列。 
    
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


# # 定义总共输出几次的计数器
# count = 0
# def print_time():
#     print('当前时间： %s' % time.ctime())
#     global t, count
#     count += 1
#     # 如果 count 小于 10，开始下一次调度
#     if count < 10:
#         t = threading.Timer(1, print_time)
#         t.start()
# # 指定 1s 后执行 print_time 函数
# t = threading.Timer(1, print_time)
# t.start()

# 定义线程调度器
s = sched.scheduler()

# 定义被调度的函数
def print_time(name='default'):
    print("%s 的时间： %s" % (name, time.ctime()))

print('主线程：', time.time())
# 指定 10 秒后执行 print_time 函数
s.enter(10, 1, action=print_time, argument=('10 秒后执行',))
# 指定 5 秒后执行 print_time 函数 优先级为 2
s.enter(5, priority=6, action=print_time, argument=('5 秒后执行的优先级为2',))
# 指定 5 秒后执行 print_time 函数 优先级为 1
s.enter(5, priority=1, action=print_time, argument=('5 秒后执行的优先级为1',))

# 执行调度任务
s.run()
print('主线程：', time.monotonic())


