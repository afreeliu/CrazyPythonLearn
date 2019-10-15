
import os

'''
    Python 的 os 模块提供了一个 fork() 方法，该方法可以 fork 出来一个进程。简单来说，fork() 方法的作用在于：程序会启动两个进程（一个
    是父进程，一个是 fork 出来的子进程）来执行从 os.fork() 开始的所有代码。 fork() 方法不需要参数，他有一个返回值，该返回值表明是哪个
    进程在执行。
    如果 fork() 方法返回 0，则表明是 fork 出来的子进程在执行。
    如果 fork() 方法返回非 0，则表明是父进程在执行， 该方法返回 fork() 出来的子进程的进程 ID
    
    注意： os.fork() 在 Windows 系统上是无效的
'''


print(' 父进程（%s）开始执行' % os.getpid())

# 开始 fork 一个子进程
# 从这行代码开始，下面的代码都会被两个进程执行
pid = os.fork()
print('进程进入： %s', os.getpid())
# 如果 pid 为 0，则表明是子进程
if pid == 0:
    print('子进程，其 ID 为（%s）， 父进程 ID 为（%s）' % (os.getpid(), os.getppid()))
else:
    print('我（%s）创建的子进程ID 为（%s）' % (os.getpid(), pid))

print('进程结束 %s' % os.getpid())