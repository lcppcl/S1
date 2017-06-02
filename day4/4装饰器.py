def login(func):
    def inner(*arg, **kwargs):
         print('passed user verification')
         return func(*arg, **kwargs)
    return inner

@login    #程序一执行就会执行这句话，也就执行login函数
def tv(name, password):
    print('welcome %s to home page' %name)
    return 4

@login
def mv(name):
    print('welcome %s to home page' %name)

a = tv('lcp', 123)
print(a)
mv('lcp')
# lv = login(tv)
# lv('lcp')

#加断点调试,
