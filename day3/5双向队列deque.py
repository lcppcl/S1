#单向队列：先进先出
#双向队列：出入无序

import collections

d = collections.deque()  #创建双向队列
d.append('1')  #右边添加一个元素
d.appendleft('10')  #在左边添加一个元素
d.appendleft('12')
print(d)   #deque(['12', '10', '1'])
d.count('1')  #查看1的个数
d.extend(['yy', 'uu'])  #可以右边扩展多个数据
d.extendleft(['ww', 'rr'])  #可以左边扩展多个元素
print(d)  #deque(['rr', 'ww', '12', '10', '1', 'yy', 'uu'])
d.rotate(2)  #把队尾的元素放到队首，执行两次
