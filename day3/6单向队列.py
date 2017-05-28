import queue
q = queue.Queue()  #创建单向队列
q.put('123')  #往单向队列里面放置元素
q.put('456')
print(q)
q.qsize()  #单向队列的大小
value = q.get()  #获取单向队列的队首元素
print(value)