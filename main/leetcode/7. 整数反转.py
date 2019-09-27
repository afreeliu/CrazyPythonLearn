






# 自己思考的来的通过的答案
def reverse(x):
    if int(x / (10 ** 9)) > 2 or int(x / (10 ** 9)) < -2:
        # 溢出了
        return 0
    isfushu = False
    if x < 0:
        x *= -1
        isfushu = True
    result = 0
    index = 0
    tmp = {}
    while x / 10 >= 1:
        a = x % 10
        x = int(x / 10)
        tmp.update({index: a})
        index += 1
    else:
        tmp.update({index: x})
    count = len(tmp)
    if count > 10:
        return 0
    else:
        for key, value in tmp.items():
            result += 10 ** (count-1-key) * value
        if isfushu:
            result *= -1
            if result < -2**31:
                return 0
            return result
        else:
            if result > 2**31-1:
                return 0
            return result



if __name__ == '__main__':
    print(reverse(10))