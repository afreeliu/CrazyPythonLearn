
import os


'''
    与目录相关的函数：
    os.getcwd(): 获取当前目录
    os.chdir(path): 改变当前目录
    os.fchdir(fd): 通过文件描述符改变当前目录。该函数与上一个函数的功能基本相似，知识该函数以文件描述符作为参数来代表目录
    
    os.chroot(path): 改变当前进程的根目录
    os.listdir(path): 返回 path 对应目录下的所有文件和子目录
    os.mkdir(path[,mode]): 创建 path 对应的目录，其中 mode 用于指定该目录的权限。该 mode 参数代表一个 UNIX 风格的权限
        比如 0o777 代表所有者可读/可写/可执行、组用户可读/可写/可执行、其他用户可读/可写/可执行
    os.makedirs(path[,mode]): 其作用类似于 mkdir()， 但该函数的功能更加强大，它可以递归创建目录。比如要创建 abc/xyz/wawa 目录，
        如果在当前目录下没有 abc 目录，那么使用 mkdir() 函数就会报错，而使用 makedirs() 函数则会先创建 abc， 然后在其中创建 xyz
        子目录，最后在 xyz 子目录下创建 wawa 子目录
        
    os.rmdir(path): 删除 path 对应的空目录。如果目录非空，则抛出一个 OSError 异常。程序可以先用 os.remove() 函数删除文件
    os.rmovedirs(path): 递归删除目录。其功能类似于 rmdir()， 但该函数可以递归删除 abc/xyz/wawa 目录，他会从 wawa 子目录
        开始删除，然后删除 xyz 子目录，最后删除 abc 目录
        
    os.rename(src, dst): 重命名文件或目录，将 src 重命名为 dst
    os.renames(old, new): 对文件或目录进行递归重命名。其功能类似于 rename()， 但该函数可以递归重命名 abc/xyz/wawa 目录，
        它会从 wawa 子目录开始重命名，然后重命名 xyz 子目录，最后重命名 abc 目录
'''


if __name__ == '__main__':
    # 获取当前目录
    print(os.getcwd())
    # # 改变当前目录
    # os.chdir('../leetcode')
    # # 再次获取当前目录
    # print(os.getcwd())

    # path = 'my_dir'
    # # 直接在当前目录下创建子目录
    # os.mkdir(path, mode=0o755)
    # path = 'abc/xyz/wawa'
    # os.makedirs(path, 0o755)

    # 以下两种删除目录的方式都需要目录是为空的前提下才能进行操作
    # rmpath = 'my_dir'
    # os.chmod(rmpath, mode=0o777)
    # if os.listdir(rmpath):
    #     for file in os.listdir(rmpath):
    #         os.remove(os.path.abspath(os.path.join(rmpath, file)))
    #     os.rmdir(rmpath)
    # else:
    #     os.rmdir(rmpath)
    # rmpath = 'abc/xyz/wawa'
    # os.removedirs(rmpath)