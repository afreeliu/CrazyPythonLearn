'''
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

示例 1:

输入: "Let's take LeetCode contest"
输出: "s'teL ekat edoCteeL tsetnoc" 
注意：在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。

'''

'''
执行用时 :
132 ms
, 在所有 Python3 提交中击败了
11.21%
的用户
内存消耗 :
14.6 MB
, 在所有 Python3 提交中击败了
5.04%
的用户
'''
def reverseWords(s):
    if len(s) == 0:
        return s
    else:
        currentS = list(s)
        stack = []
        result = ''
        for c in currentS:
            if c == ' ':
                while len(stack):
                    result = result + stack.pop()
                else:
                    result = result + ' '
            else:
                stack.append(c)
        while len(stack):
            result = result + stack.pop()
        return result

'''
执行用时 :
88 ms
, 在所有 Python3 提交中击败了
22.91%
的用户
内存消耗 :
14.1 MB
, 在所有 Python3 提交中击败了
5.04%
的用户
'''
def areverseWords(s):
    if not len(s):
        return s
    else:
        b = ''
        r = ''
        for ss in str(s):
            if len(ss):
                if ss == ' ':
                    r = r + b + ss
                    b = ''
                else:
                    b = ss + b
        return r + b

def breverseWords(s):
    return " ".join([i[::-1] for i in s.split()])



'''
    首先，假设有一个元组或者列表

    a = (1, 2, 3, 4)
    b = [1, 2, 3, 4]
    则a[::-1]
    和b[::-1]
    的含义是将元组或列表的内容翻转

    a[::-1]   # 结果为(4,3,2,1)
    b[::-1]   # 结果为[4,3,2,1]
    返回结果是4321，那么问题就来了[::-1]
    表示的是从头到尾，步长为 - 1
    Sequence[start:end:step]
    b = a[i:j:s]
    这种格式呢，i, j与上面的一样，但s表示步进，缺省为1.
    所以a[i:j:1]
    相当于a[i:j]。当s < 0
    时，i缺省时，默认为 - 1.
    j缺省时，默认为 - len(a) - 1
'''



a = breverseWords('aada gweg sdfwe')
print(a)
