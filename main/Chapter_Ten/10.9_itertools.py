import itertools as it
'''
    这个主要是练习 itertools 模块的功能函数
'''

if __name__ == '__main__':
    print([e for e in dir(it) if not e.startswith('_')])

    # 使用 count(10, 3) 生成 10，13，16，...的迭代器
    for i in it.count(10, 3):
        if i > 20:
            break
        print(i)

    print('---------------')
    # cycle 用于对序列生成无限循环的迭代器
    my_count = 0
    for e in it.cycle(['Python', 'Java', 'Switf', 'C++']):
        if my_count > 5:
            break
        my_count += 1
        print(e)
    print('---------------')
    # repeat 用于生成n个元素重复的迭代器
    for e in it.repeat('Python', 3):
        print(e)
    print('---------------')
    # accumulate(p, [,func]): 默认生成根据序列p元素累加的迭代器，p0,p0+p1,p0+p1+p2,...序列，如果指定了func函数，则用func函数来计算下一个元素的值
    for e in it.accumulate([1,2,3,4,5,6]):
        print(e)
    for e in it.accumulate([1,2,3,4], lambda x,y : x*y):
        print(e)
    print('---------------')
    # chain(p,q,...): 将多个序列里的元素"链"在一起生成新的序列
    for e in it.chain([1,2,3], [2,3,4,5], [1,1,5,6,7]):
        print(e)
    print('---------------')
    # compress(data, selectors): 根据 selectors 序列的值对data序列的元素进行过滤。如果selectors[0]为真，则保留data[0]；如果selectors[1]为真，则保留data[1]...以此类推
    for e in it.compress([1,2,3,4,5,6,7,8], [1,0,1,0,1,0,0,0]):
        print(e)
    print('---------------')
    # dropwhile(pred, seq): 使用pred函数对seq序列进行过滤，从seq中第一个使用pred函数计算为False的元素开始，保留从该元素到序列结束的全部元素
    for e in it.dropwhile(lambda x: x<=0, [-1,-2,-3,-4,0,1,2,3,4]):
        print(e)
    print('---------------')
    # takewhile(pred, seq): 该函数和上一个函数恰好相反。使用pred函数对seq序列进行过滤，从seq中第一个使用pred函数计算为False的元素开始，去掉从该元素到序列结束的全部元素
    for e in it.takewhile(lambda x: x<=0, [-1,-2,-3,-4,0,1,2,3,4]):
        print(e)
    print('---------------')
    # filterfalse(pred, seq): 使用pred函数对seq序列进行过滤，保留seq中使用pred计算为True的元素。比如filterfalse(lambda x:x%2, range(10)),得到0，2，4，6，8
    for e in it.filterfalse(lambda x: x%2, [-1,-2,-3,-4,0,1,2,3,4]):
        print(e)
    print('---------------')
    # isice(seq, [start,], stop, [, step]): 其功能类似于序列的slice方法，实际上就是返回seq[start:stop:step]的结果
    for e in it.islice([-1,-2,-3,-4,0,1,2,3,4], 2, 6, 2):
        print(e)
    print('---------------')
    # starmap(func, seq): 使用func对seq序列的每个元素进行计算，将计算结果作为新的序列元素。当使用func计算序列元素时，支持序列解包
    #   比如seq序列的元素长度为3，那么func可以是一个接受三个参数的函数，该函数将会根据这三个参数来计算新序列的元素。
    for e in it.starmap(pow, [(2,3), (3,4), (4,5)]):
        print(e)
    print('---------------')
    # zip_longest(p,q,...): 将p、q等序列中的元素按索引合并成元组，这些元组将作为新序列的元素
    for e in it.zip_longest('ABCDE', 'abc', fillvalue='@'):
        print(e)