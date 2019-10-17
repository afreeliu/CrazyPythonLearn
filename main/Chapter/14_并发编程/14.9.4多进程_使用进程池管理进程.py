import os, time
import multiprocessing

'''
    与线程池类似的是，如果程序需要启动多个进程，也可以使用进程池来管理进程。线程可以通过 multiporcessing 模块的 Pool() 函数创建进程，进程
    实际上是 multiprocessing.pool.Pool 类。

    进程池具有如下常用方法：

    apply(func[, args[,kwds]]): 将 func 函数提及哦啊给进程池处理。其中 args 代表传给 func 的位置参数， kwds 代表传给 func 的关键字
                                参数。该方法会被阻塞直到 func 函数执行完成

    apply_async(func[, args[, kwds[, callback[, error_callback]]]]): 这是 apply() 方法的异步版本，该方法不会被阻塞。其中
                            callback 指定 func 函数完成后的回调函数，error_callback 指定 func 函数出错后的回调函数

    map(func, iterable[, chunksize]): 类似于 Python 的 map() 全局函数，只不过此处使用新进程对 iterable 的每一个元素执行 func 函数

    map_async(func, iterable[, chunksize[, callback[, error_callback]]]): 这是 map() 方法的异步版本，该方法不会被阻塞。其中
            callback 指定 func 函数完成后的回调函数， error_callback 指定 func 函数出错后的回调函数

    imap(func, iterable[, chunksize]): 这是 map() 方法的延迟版本

    imap_unordered(func, iterable[, chunksize]): 功能类似于 imap() 方法，当该方法不能保证所生成的结果（包含多个元素）与元
                                                iterable 中的元素顺序一致

    starmap(func, iterable[, chunksize]): 功能类似于 map() 方法，但该方法要求 iterable 的元素也是 iterable 对象，程序会将每一个
                                          元素解包之后作为 func 函数的参数

    close(): 关闭进程池。在调用该方法之后，该进程池不能在接收新任务，他会把当前进程池中的所有任务执行完成后再关闭自己。

    terminate(): 立即中止进程池

    join(): 等待所有进程完成

'''


# 定义一个准备作为进程任务的函数
def action(name = '_default_'):
    print('(%s)进程正在执行， 参数为：%s' % (os.getpid(), name))
    time.sleep(3)

def action1(max):
    my_sum = 0
    for i in range(max):
        print('(%s)进程正在执行:%d' % (os.getpid(), i))
        my_sum += i
    return my_sum



if __name__ == '__main__':
    # 创建一个包含 4 个进程的进程池
    # pool = multiprocessing.Pool(processes=4)
    # pool.apply_async(action)
    # pool.apply_async(action, args=('位置参数',))
    # pool.apply_async(action, kwds={'name': '关键字参数'})
    # pool.close()
    # pool.join()

    with multiprocessing.Pool(processes=4) as pool:
        # 使用进程执行map计算
        # 后面元组有 3 个元素，因此程序启动 3 个进程来执行 action1 函数
        results = pool.map(action1, (50, 100, 150))
        print('-----------------------')
        for r in results:
            print(r)
