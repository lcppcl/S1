'''
递归要有明确的出口
效率低，易理解
局部变量每一层的返回点都需要栈来存储，递归次数过多容易造成栈溢出

要求：
每一次在规模上都有所缩小

'''

def calc(n):
    if n/2 > 1:
        return calc(n/2)
    else:
        return 1


"""
斐波那契
"""

def func(arg1, arg2, stop):
    if arg1 == 0:
        print(arg1, arg2)
    arg3 = arg1 + arg2
    print(arg3)
    if arg3 < stop:
        func(arg2, arg3, stop)

func(0,1,30)