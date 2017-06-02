import time
def consumer(name):
    print("%s准备吃包子" % name)
    while True:
        food = yield
        print('包子[%s]来了,被[%s]吃了' %(food, name))

def producer(name):
     c = consumer('A')
     c2 = consumer('B')
     c.__next__()
     c2.__next__()
     print('准备做包子')
     for i in range(10):
         time.sleep(1)
         print('做了2个包子')
         c.send(i)  #把i传给yield，
         c2.send(i)


producer('lcp')