"""
一个函数调用时返回一个迭代器
"""

def cash_money(amount):
    while amount > 0:
        amount -= 100
        yield 100
        print('哈哈')


atm = cash_money(500)
print(type(atm))
ret = atm.__next__()
ret = atm.__next__()
print(ret)

#用调试可以查看执行过程