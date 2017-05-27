import collections

#创建类
MytypleClass = collections.namedtuple('MytypleClass', ['x', 'y', 'z'])
obj = MytypleClass(11,22,33)  #创建对象
print(obj.x)
print(obj.y)
print(obj.z)