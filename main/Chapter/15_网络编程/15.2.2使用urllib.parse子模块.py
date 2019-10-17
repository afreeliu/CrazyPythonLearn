
from urllib.parse import *
'''
    下面介绍 urllib.parse 子模块中用于解析 URL 地址和查询字符串的函数

    urllib.parse.urlparse(urlstring, scheme='', allow_fragments=True): 该函数用于解析 URL 字符串。程序返回一个 ParseResult 对象，
            可以获取解析出来的数据。

    urllib.parse.urlunparse(parts): 该函数是一个函数的反响操作，用于将解析结果反向拼接成 URL 地址。

    urllib.parse.parse_qs(qs, keep_blank_values=False, strict_parsing=False, encoding='utf-8'): 该函数用于解析查询字符串
        (application/x-www-form-urlencodeed 类型的数据)，并以 dict 形式返回解析结果

    urllib.parse.parse_qsl(qs, keep_blank_values=False, strict_parsing=False, encoding='utf-8'): 该函数用于解析查询字符串
        (application/x-www-form-urlencodeed 类型的数据)，并以列表形式返回解析结果

    urllib.parse.urlencode(query, doseq=False, safe='', encoding=None, errors=None, quote_via=quote_plus): 将字典形式或列表
        形式的请求参数恢复成请求字符串。该函数相当于 parse_qs()、parse_qsl() 的逆函数

    urllib.parse.urljoin(base, url, allow_fragments=True): 该函数用于将一个 base URL 和另一个资源 URL 连接成代表绝对地址的 URL

'''

# 解析 URL 字符串
result = urlparse('http://www.crazyit.org:80/index.php;yeeku?name=fkit#frag')
print(result)
# 通过属性名和索引来获取 URL 的个部分
print('scheme:', result.scheme, result[0])
print('主机和端口:', result.netloc, result[1])
print('主机:', result.hostname)
print('端口:', result.port)
print('资源路径:', result.path, result[2])
print('参数:', result.params, result[3])
print('查询字符串:', result.query, result[4])
print('fragment:', result.fragment, result[5])
print(result.geturl())


originURL = urlunparse(result)
print(originURL)


# 解析查询字符串，返回 dict
result = parse_qs('name=fkit&name=lskdjfslkjjava&age=12')
print(result)
result = parse_qsl('name=fkit&name=lskdjfslkjjava&age=12')
print(result)
# 将列表形式的请求参数恢复成字符串
print(urlencode(result))

'''
    urljoin() 函数负责将两个 URL 拼接在一起，返回代表绝对地址的 URL。这里主要可能出现 3 中情况
    
    1 被拼接的 URL 只是一个相对路径的 path（不以斜线开头），那么该 URL 将会被拼接早 base 之后，如果 base 本身包含 path 部分，则用
        被拼接的 URL 替换 base 所包含的 path 部分
    
    2 被拼接的 URL 是一个根路径 path（以单斜线开头），那么该 URL 将会被拼接到 base 的域名之后
    
    3 被拼接的 URL 是一个绝对路径 path（以双斜线开头），那么该 URL 将会被拼接到 base 的 scheme 之后。

'''

# 1 被拼接的 URL 不以斜线开头
result = urljoin('http://www.crazyit.org/users/login.html', 'help.html')
print(result)
result = urljoin('http://www.crazyit.org/users/login.html', 'book/list.html')
print(result)

# 2 被拼接的 URL 以单斜线开头
result = urljoin('http://www.crazyit.org/users/login.html', '/help.html')
print(result)

# 3 被拼接的 URL 以双斜线开头
result = urljoin('http://www.crazyit.org/users/login.html', '//help.html')
print(result)



