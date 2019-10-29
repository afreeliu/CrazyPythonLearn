
import socket
'''
    程序使用 socket 之前，必须先创建 socket 对象，可通过该类的如下构造器来创建 socket 实例。
    socket.socket(famil=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)
    上面构造器的前三个参数比较重要，其中：
    family 参数用于指定网络类型。该参数支持 socket.AF_UNIX（UNIX 网络）、socket.AF_INET（基于 IPv4 协议的网络）和 socket.AF_INET6
    （基于 IPv6 协议的网络）这三个常量
    type 参数用于指定网络 sock 类型。该参数可支持 SOCK_STREAM（默认值，创建基于 TCP 协议的 socket）、SOCK_DGRAM（创建基于 UDP 协议的
        socket）和 SOCK_RAW（创建原始 socket）。一般常用的是 SOCK_STREAM 和 SOCK_DGRAM
    proto 参数用于指定协议号，如果没有特殊要求，该参数默认为 0，并可以忽略

    创建 socket 之后，接下来需要将两个 socket 连接起来。从图 15.4 中并没有看出 TCP 协议控制的两个通信实体之间有服务器和客户端之分，这是
    因为此图是两个通信实体之间已经建立虚拟链路之后的示意图。在两个通信实体之间没有建立虚拟链路时，必须有一个通信实体先做出"主动姿态"，主动
    接收来自其他通信实体的连接请求。

    作为服务器端使用的 socket 必须被绑定到指定 IP 地址和端口，并在该 IP 地址和端口进行监听，接收来自客户端的连接。

    socket 对象提供了如下常用方法。
    socket.accept(): 作为服务器端使用的 socket 调用该方法接收来自客户端的连接
    socket.bind(address): 作为服务器端使用的 socket 使用该方法，将该 socket 绑定到指定 address，该 address 可以是一个元组，包含 IP 地址和端口
    socket.close(): 关闭连接，回收资源
    socket.connect(address): 作为客户端使用的 socket 调用该方法连接远程服务器。
    socket.connect_ex(address): 该方法与上一个方法的功能大致相同，只是当程序出错时，该方法不会抛出异常，而是返回一个错误标识
    socket.listen([backlog]): 作为服务端使用的 socket 调用该方法进行监听。
    socket.makefile(mode='r', buffering=None, *, encoding=None, errors=None, newline=None): 创建一个和该 socket 关联的文件对象。
    socket.recv(bufsize[, flags]): 接收 socket 中的数据。该方法返回 bytes 对象代表接收到的数据。
    socket.recvfrom(bufsize[, flags]): 该方法与上一个方法的功能大致相同，只是该方法的返回值是 (bytes, address) 元组
    socket.recvmsg(bufsize[, ancbufsize[, flags]]): 该方法不仅接收来自 socket 的数据，还接收来自 socket 的辅助数据，因此该方法的
        返回值是一个长度为 4 的元组———— (data, ancdata, msg_flags, address) 元组。
    socket.recvmsg_into(buffers[, ancbufsize[, flags]]): 类似于 socket.recvmsg() 方法，但该方法将接收到的数据放入 buffers 中
    socket.recvfrom_into(buffer[, nbytes[, flags]]): 类似于 socket.recvfrom() 方法，但该方法将接收到的数据放入 buffer 中。
    socket.recv_into(buffer[, nbytes[, flags]]): 类似于 socket.rec() 方法，但该方法将接收到的数据放入 buffer 中。
    socket.send(bytes[, flags]): 向 socket 发送数据，该 socket 必须与远程 socket 建立了连接。该方法通常用于在基于 TCP 协议的网络中发送数据
    socket.sendto(bytes, address): 向 socket 发送数据，该 socket 应该没有与远程 socket 建立连接。该方法通常用于在基于 UDP 协议的网络中发送数据
    socket.sendfile(file, offset=0, count=None): 将整个文件内容都发送出去，知道遇到文件的 EOF。
    socket.shutdown(how): 关闭连接，其中 how 用于设置关闭方式。

    TCP 通信的服务端编程的基本步骤：
    1 服务器端先创建一个 socket 对象
    2 服务器端 socket 将自己绑定到指定 IP 地址和端口
    3 服务器端 socket 调用 listen() 方法监听网络
    4 程序采用循环不断调用 socket 的 accept() 方法接收来自客户端的连接。
'''


# 创建 socket 对象
s = socket.socket()
# 将 socket 绑定到本机 IP 地址和端口
s.bind(('192.168.1.88', 30000))
# 服务器端开始监听来自客户端的连接
s.listen()
while True:
    # 每当接收到客户端 socket 的请求时，该方法就返回对应的 socket 和远程地址
    c, address = s.accept()