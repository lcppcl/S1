import copy

#copy.copy()  #浅拷贝
#copy.deepcopy()  #深拷贝

#字符串和数字同样   （字符串和数字赋值图）
a1 = 121212
a2 = 121212
a1 = 12
print(id(a1))  #查看在内存中的地址
print(id(a2))  #两者的内存地址相同

#字符串和数字无论深浅拷贝还是赋值，他们都是指向同一块内存单元
a1 = 121212
a2 = a1
a3 = copy.copy(a1)  #浅拷贝，地址一样
a4 = copy.deepcopy(a1)  #深拷贝，地址一样
print(id(a1))  #查看在内存中的地址
print(id(a2))  #两者的内存地址相同
print(id(a3))  #两者的内存地址相同
print(id(a4))  #两者的内存地址相同

#元组，列表，字典
n1 = {'k1': 'v1', 'k2': 123, 'k3': ['lcp', 234]}
n2 = n1  #赋值
print(id(n1))  #查看在内存中的地址
print(id(n2))  #两者的内存地址相同

n3 = copy.copy(n1)  #浅拷贝，只拷贝一层
print(id(n1))
print(id(n3))  #两者之间的内存地址不一样
print(id(n1['k1']))
print(id(n3['k1']))  #里面元素的地址相同

n4 = copy.deepcopy(n1)  #深拷贝，除了最后一层不拷贝外，都进行拷贝
print(id(n1))
print(id(n4))  #两者之间的内存地址不一样
print(id(n1['k1']))
print(id(n4['k1']))  #最后一层里面元素的地址相同
print(id(n1['k3']))
print(id(n4['k3']))   #地址不相同




#应用
dic = {
    'cpu':[80,],
    'mem':[80,],
    'disk':[80,],
}
new_dic = copy.deepcopy(dic)
new_dic['cpu'][0] = 50
print(dic)
print(new_dic)
