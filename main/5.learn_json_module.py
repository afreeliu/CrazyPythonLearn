

def sum(argList, ss):
    if len(argList) < 2:
        return None
    last = len(argList)
    lastnum = argList.pop()
    listcount = len(argList)
    first = 0
    sec = 0
    tt = 0
    while listcount:
        print(listcount)
        second = argList[listcount - 1]
        print(lastnum, second, ss)
        if lastnum + second == ss:
            first = listcount - 1
            sec = last -1
            print('相同的了')
            print(first, sec)
            print('相同的了')
            tt = 1
            break
            # print('有值相等', listcount-1, last-1)
            # return [listcount-1, last-1]
        else:
            listcount-=1
    if tt:
        print('输出了')
        print(first, sec)
        return [first, sec]
    else:
        print(first, sec)
        sum(argList, ss)





if __name__ == '__main__':
    sum([2, 7, 11, 15], 9)