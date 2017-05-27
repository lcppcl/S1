import collections

dic2 = dict()  #没有顺序
dic2['k1'] = 'v1'
dic2['k2'] = 'v2'
dic2['k3'] = 'v3'
print(dic2)


dic = collections.OrderedDict()  #有序
dic['k1'] = 'v1'  #一般字典是没有顺序的
dic['k2'] = 'v2'  #一般字典是没有顺序的
dic['k3'] = 'v3'  #一般字典是没有顺序的
'''
print(dic)
dic.move_to_end('k1')  #把当前的值的键值对移到最后
print(dic)
ret = dic.popitem()  #后进先出取出值
print(dic, ret)
ret = dic.pop('k2')  #指定拿出键所对应的值
print(dic, ret)
dic['k4'] = None  #给k4设置默认值
dic.setdefault('k4','value')  #给k4设置默认值
dic.update({'k1':12, 'k10':'k10'})  #更新字典中的值
print(dic)
'''

dic = collections.defaultdict(list)   #设置默认类型
print(dic)
dic['k1'].append('lcp')
print(dic)









