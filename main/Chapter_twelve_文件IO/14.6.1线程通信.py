
import threading

'''
    为了实现线程间的通讯，可以借助于 Condition 对象来保持协调。使用 Condition 可以让那些已经得到 Lock 对象却无法继续执行的线程释放 Lock
    对象， Condition 对象也可以唤醒其他处于等待状态的线程
    
    将 Condition 对象与 Lock 对象组合使用，可以为每个对象提供多个等待集（wait-set）。因此 Condition 对象总是需要有对应的 Lock 对象。
    从 Condition 的构造器 __init__(self, lock=None) 可以看出，程序在创建 Condition 时可通过 lock 参数传入要绑定的 Lock 对象；
    如果不指定 lock 参数，在创建 Condition 时它会自动创建一个与之绑定的 Lock 对象。
    Condition 类提供以下几个方法：
    
    acquire([timeout])/release(): 调用 Condition 关联的 Lock 的 acquire() 或 release() 方法。
    
    wait([timeout]): 导致当前线程进入 Condition 的等待池等待通知并释放锁，知道其他线程调用该 Condition 的 notify() 或 notify_all()
                    方法来唤醒该线程。在调用该 wait() 方法时可传入一个 timeout 参数，指定线程最多等待多少秒
                    
    notify(): 唤醒在该 Condition 等待池中的单个线程并通知它，收到通知的线程将自动调用 acquire() 方法尝试加锁。如果所有线程都在该 Condition
            等待池中等待，则会选择唤醒其中一个线程，选择是任意性的。 
            
    notify_all(): 唤醒在该 Condition 等待池中等待的所有线程并通知它们

'''


class Account:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self._balance = balance
        self.cond = threading.Condition()
        # 定义是否已经存钱的标识
        self._flag = False

    # 因为账户余额不允许随便更改，所以只为 self._balance 提供 getter 方法
    def getBalance(self):
        return self._balance
    # 提供一个线程安全的 draw() 方法来完成取钱操作
    def draw(self, draw_amount):
        # 加锁，相当于调用 Condition 绑定的 Lock 的 acquire()
        self.cond.acquire()
        try:
            # 如果 self._flag 为 False ，表明账户中还没有人存钱进去，取钱方法被阻塞
            if not self._flag:
                self.cond.wait()
            else:
                # 执行取钱操作
                print(threading.current_thread().name + '取钱：' + str(draw_amount))
                self._balance -= draw_amount
                print('账户余额为：' + str(self._balance))
                # 将表明账户中是否已有存款的标识设为 False
                self._flag = False
                # 唤醒其他线程
                self.cond.notify_all()
        # 使用 finall 块来释放锁
        finally:
            self.cond.release()
    def deposit(self, deposit_amount):
        # 加锁，相当于调用 Condition 绑定的 Lock 的 acquire()
        self.cond.acquire()
        try:
            # 如果 self._flag 为 True， 表明中中已有人存钱进去，存款方法被阻塞
            if self._flag:
                self.cond.wait()
            else:
                # 执行存款操作
                print(threading.current_thread().name + '存钱：' + str(deposit_amount))
                self._balance += deposit_amount
                print('账户余额为：' + str(self._balance))
                # 将表明账户中是否已有存款的标识设为 True
                self._flag = True
                # 唤醒其他线程
                self.cond.notify_all()
        finally:
            self.cond.release()

# 定义一个函数，模拟重复 max 次执行取钱操作
def draw_many(account, draw_amount, max):
    for i in range(max):
        account.draw(draw_amount)

# 定义一个函数，模拟重复 max 次执行存款操作
def deposit_many(account, deposit_amount, max):
    for i in range(max):
        account.deposit(deposit_amount)

if __name__ == '__main__':
    # 创建一个账户
    acct = Account('1234567', 0)
    # 创建并启动一个 "取钱" 线程
    threading.Thread(name='取钱者', target=draw_many, args=(acct, 800, 2)).start()
    # 创建并启动一个 "存钱" 线程
    threading.Thread(name='存钱者甲', target=deposit_many, args=(acct, 800, 2)).start()
    # threading.Thread(name='取钱者乙', target=deposit_many, args=(acct, 800, 100)).start()
    # threading.Thread(name='取钱者丙', target=deposit_many, args=(acct, 800, 100)).start()