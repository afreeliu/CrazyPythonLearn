import random
'''
    random 模块主要包含生成伪随机数的各种功能变量和函数
'''

if __name__ == '__main__':
    print(random.__all__)

    # random.seed(a=None,version=2): 指定种子来初始化伪随机数生成器
    # random.randrange(start=,stop=[,step]): 返回从start开始到stop结束、步长为step的随机数，其实就相当于choice(range(start,stop,step)
    #           的效果，只不过世纪底层并不生成区间对象。
    # random.randint(a,b): 生成一个范围为a到b（包含两者）的随机数，其等于randrange(a,b+1)的效果
    # random.choice(seq): 从seq中随机抽取一个元素，如果seq为空，则引发IndexError异常。
    # random.choices(seq,weights=None,*,cum_weights-None,k=1): 从seq序列中抽取k个元素，不可通过weights指定各元素被抽取的权重
    #       (代表被抽取的可能性高低）。
    # random.shuffle(x[,random]): 对 x 序列执行洗牌 "随机排序"操作
    puke = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54]
    print(puke)
    random.shuffle(puke)
    print(puke)
    # random.sample(population=,k): 从population序列中随机抽取k个独立的元素。
    print(random.sample(puke, 5))
    # random.random(): 生成一个从0.0（包含）到1.0（不包含）之间的伪随机浮点数
    print(random.random())
    # random.uniform(a,b): 生成一个范围为a到b（包含两者）的随机数
    print(random.uniform(1,100))

    # random.expovariate(lambd=): 生成呈指数分布的随机数。其中lambd参数（其实应该是lambda，知识lambda是Python的关键字，所以简写成lambd）
    #       为 1 除以期望平均值。如果lambd是正值，则返回的随机数是从0到正无穷大；如果lambd为负数，则返回的随机数是从负无穷到0
    print(random.expovariate(-1))