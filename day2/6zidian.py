dic = {'k1': 'v2'}
dic = dict(k1='v2', k2='v2')
dic.fromkeys(['k1'], 'v2')



dic = {'k1':'v1','k2':'v2'}
v1 = dic['k1']  #获取键位k1的值
print(v1)
v1 = dic.get('k1')  #获取键位k1的值
print(v1)
v3 = dic.get('k3', 'lcp')  #没有key时，可以自己设置返回值,默认为None。有key就不会替换
print(v3)


dic.keys()    #获取到所有的keys
dic.values()   #获取到所有的values
dic.items()   #获取到所有的键值对
for k in dic.keys():  #输出所有的key
    print(k)
for v in dic.values():  #输出所有的value
    print(v)
for k, v in dic.items():  #输出所有的键值对
    print(k, v)

dic = {'k1':'v1','k2':'v2'}
v = dic.pop('k1')   #字典是无序的，拿走值时必须指定拿走哪一个值，指定的key不在，就会出错
print(v)
print(dic)
dic.popitem()   #随机拿走一个值


dic = {'k1':'v1','k2':'v2'}
dic.update({'k3':123})
dic['k4'] = 1234
print(dic)