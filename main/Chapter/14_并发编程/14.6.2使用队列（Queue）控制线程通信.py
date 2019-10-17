
import queue
import threading
import time
'''
    在 queue 模块下提供了几个阻塞队列，这些队列主要用于实现线程通信。在 queue 模块下主要提供了三个类，分别代表三种队列，它们的主要区别就在
    于进队列、出队列的不同。
    
    queue.Queue(maxsize = 0): 代表 FIFO （先进先出）的常规队列，maxsize 可以限制队列的大小。如果队列的大小达到队列的上限，就会加锁，
                              再次加入元素时会被阻塞，知道队列中的元素被消费。如果将 maxsize 设置为 0 或负数，则队列大小为无限大
                              
    queue.LifoQueue(maxsize = 0): 代表 LIFO （后进先出）的队列，与 Queue 的区别就是出队列的顺序不同。
    
    PriorityQueue(maxsize = 0): 代表优先级队列，优先级最小的元素先出队列。
    
    Queue.qsize(): 返回队列的实际大小，也就是该队列中包含几个元素。
    
    Queue.empty(): 判断队列是否为空。
    
    Queue.full(): 判断队列是否为满。
    
    Queue.put(item, block=True, timeout=None): 向队列放入元素。如果队列已满，且 block 参数为 True（阻塞），当前线程被阻塞，timeout
                                               指定阻塞时间，如果将 timeout 设置为 None，则代表一直阻塞，直到该队列元素被消费；如果
                                               队列已满，且 block 参数为 False（不阻塞），则直接引发 queue.FULL 异常。
                                               
    Queue.put_nowait(item): 向队列放入元素，不阻塞。相当于在上一个方法中将 block 参数设置为 False
    
    Queue.get(item, block=True, timeout=None): 从队列中取出元素（消费元素）。如果队列已满，且 block 参数为 True（阻塞），当前线程被
                                               阻塞，timeout 指定阻塞时间，如果将 timeout 设置为 None，则代表一直阻塞，直到有元素
                                               被放入队列中；如果队列已空，且 block 参数为 False（不阻塞），则直接引发 queue.EMPTY 异常
                                               
    Queue.get_nowait(item): 从队列中取出元素，不阻塞。相当于在上一个方法中将 block 设置为 False
    
'''

def getItem(bq):
    print('执行获取队列元素')
    time.sleep(2)
    print(bq.get())

def test():
    bq = queue.LifoQueue(2)
    bq.put("bPython")
    bq.put("aPython")
    print('111111111')
    threading.Thread(target=getItem, args=(bq,), name='获取队列元素线程').start()
    bq.put("Python") # 阻塞线程
    print(bq)
    print('222222222')

test()


def product(bq):
    str_tuple = ("Python", "Kotlin", "Swift")
    for i in range(99999):
        print(threading.current_thread().name + '生产者准备生成组元素！')
        time.sleep(0.2)
        # 尝试放入元素，如果队列已满，则线程被阻塞
        bq.put(str_tuple[i % 3])
        print(threading.current_thread().name + '生产者生成元组元素完成')

def consume(bq):
    while True:
        print(threading.current_thread().name + '消费者准备消费元素！')
        time.sleep(0.2)
        t = bq.get()
        print(threading.current_thread().name + '消费者消费[%s]元素完成' % t)

# 创建一个容量为 1 的 Queue
bq = queue.Queue(maxsize=1)
# 启动三个生产者线程
threading.Thread(target=product, args=(bq,), name='生产者甲').start()
threading.Thread(target=product, args=(bq,), name='生产者乙').start()
threading.Thread(target=product, args=(bq,), name='生产者丙').start()
# 启动一个消费者线程
threading.Thread(target=consume, args=(bq,), name='消费者').start()



