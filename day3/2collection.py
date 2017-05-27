import collections

'''
obj = collections.Counter('lcpoplijjjjkkp')  #对每个字符出现的次数进行计算，并排序
print(obj)
ret = obj.most_common(4)  #取出排在前四的值
print(ret)

#Counter继承dict
for k in obj.elements():
    print(k)
for k,v in obj.items():
    print(k,v)
'''

obj = collections.Counter(['11', '22', '22', '33'])
print(obj)
obj.update(['lcp', '11'])  #增加
print(obj)  #Counter({'11': 2, '22': 2, '33': 1, 'lcp': 1})
obj.subtract(['lcp', '11'])  #删除
print(obj)  #Counter({'22': 2, '11': 1, '33': 1, 'lcp': 0})
obj.subtract(['lcp', '11'])  #删除
print(obj)  #Counter({'22': 2, '33': 1, '11': 0, 'lcp': -1})
obj.subtract(['lcp', '11'])  #删除
print(obj)  #Counter({'22': 2, '33': 1, '11': -1, 'lcp': -2})
