
import threading
import time


'''
    join 线程
    Thread 提供了让一个线程等待另一个线程完成的方法—————— join() 方法。当在某个程序执行流中调用其他线程的 join() 方法调用线程将被阻塞，
    直到被 join() 方法加入的 join 线程执行完成。
    join() 方法通常由使用线程的程序调用，以将大问题划分成许多小问题，并为每个小问题分配一个线程。当所有的小问题都得到处理后，再调用主线程来进一步操作
    join() 方法中有一个参数 timeout 参数，该参数指定等待 join 的线程的时间最长为 timeout 秒，如果在 timeout 秒内被 join 的线程还没有执行结束，则不再等待
    
    后台线程
    有一种线程，他是在后台运行的，他的任务是为其他线程提供服务，这种线程被称为"后台线程（Daemon Thread）"， 又称为"守护线程"或"精灵线程"。
    Python 解析器的垃圾回收线程就是典型的后台线程
    后台线程有一个特征：如果所有的前台线程都死亡了，那么后台线程会自动死亡
    调用 Thread 对象的 Daemon 属性可以将指定线程设置为后台线程
    
    
    线程睡眠： sleep
    如果需要让当前正在执行的线程暂停一段时间，并进入阻塞状态，则可以通过调用 time 模块的 sleep(secs) 函数来实现。该函数指定一个 secs 参数，
    用于指定线程阻塞多少秒
    当当前线程调用 sleep() 函数进入阻塞状态后，在其睡眠时间段内，该线程不会获得执行的机会，即使系统中没有其他可执行的线程，处于 sleep() 中
    的线程也不会执行，因此 sleep() 函数常用来状态线程的运行
    
    线程同步
      
    同步锁（Lock）
'''

def action(max):
    for i in range(max):
        # 当直接调用 run() 方法时， Thread 的 name 属性返回的是该对象的名字而不是当前线程的名字
        # 使用 threading.current_thread().name 总是获取当前线程的名字
        print(threading.current_thread().name + " " + str(i))


# 模拟使用在线程安全
class Account:
    # 定义构造器
    def __init__(self, account_no, balance):
        # 封装账户编号和账户余额两个成员变量
        self.account_no = account_no
        self._balance = balance
        self.lock = threading.RLock()
    # 因为账户余额不允许随便修改，所以只为 self._balance 提供 getter 方法
    def getBalance(self):
        return self._balance
    # 提供一个线程安全的 draw() 方法来完成取钱操作
    def draw(self, draw_amount):
        # 加锁
        self.lock.acquire()
        try:
            if self._balance >= draw_amount:
                # 吐出钞票
                print(threading.current_thread().name + "取钱成功！吐出钞票:" + str(draw_amount))
                time.sleep(0.001)
                # 修改余额
                self._balance -= draw_amount
                print('\t余额为：' + str(self._balance))
            else:
                print(threading.current_thread().name + "取钱失败！余额不足！")
        finally:
            # 修改完成，释放锁
            self.lock.release()


# 定义一个函数来模拟取钱操作
def draw(account, draw_amount):
    # 账户余额大于取钱数目
    # if account.balance >= draw_amount:
    #     # 吐出钞票
    #     print(threading.current_thread().name + "取钱成功！吐出钞票:" + str(draw_amount))
    #     time.sleep(0.001)
    #     # 修改余额
    #     account.balance -= draw_amount
    #     print('\t余额为：' + str(account.balance))
    # else:
    #     print(threading.current_thread().name + "取钱失败！余额不足！")

    # 调用新的，加了锁的 Account 类的方法
    account.draw(draw_amount)




if __name__ == '__main__':
    # join 线程例子
    # # 启动子线程
    # threading.Thread(target=action, args=(100,), name='子线程').start()
    # for i in range(100):
    #     if i == 20:
    #         jt = threading.Thread(target=action, args=(100,), name='被 join 的线程')
    #         jt.start()
    #         # 主线程调用来 jt 线程的 join() 方法
    #         # 主线程必须等 jt 执行结束才会向下执行
    #         jt.join()
    #     print(threading.current_thread().name + " " + str(i))

    # 后台线程例子
    t = threading.Thread(target=action, args=(100,), name='后台线程')
    # 将此线程设置成后台线程
    # 也可以在创建 Thread 对象时通过 daemon 参数将其设置为后台线程
    t.daemon = True
    # 启动后台线程
    t.start()
    for i in range(10):
        print(threading.current_thread().name + " " + str(i))
    # ————————程序执行到此处结束，前台线程（主线程）结束————————————————
    # 后台线程也应该随之结束


    # 模拟取钱，实现线程安全
    acct = Account('1234567', 1000)
    #使用两个线程模拟从同一个账户取钱
    threading.Thread(target=draw, args=(acct, 800), name='甲').start()
    threading.Thread(target=draw, args=(acct, 800), name='乙').start()