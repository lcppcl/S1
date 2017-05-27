li = [1, 2, 3]
li = list([1, 2, 3])
li = list((1, 2, 3))  #两种方式创建列表对象

#列表是有序的
li.append(5)  #列表的尾部添加一个元素
print(li)


li.clear()  #清除列表
print(li)

li = [1, 2, 3]
li[1] = 3  #更新列表的某个值
print(li)

del li[1]  #删除列表的某个值
print(li)

li.extend([11, 33])   #扩展列表
print(li)
li.extend((11, 33,))
print(li)


result = li.index(33)  #获取某个元素的下标，没有值就会出错
print(result)


li.insert(0, 'lcp')  #指定位置插入元素
print(li)


li = [2,3,4,5]
result = li.pop()  #默认取出最后一个值
print(result)
print(li)
result = li.pop(0)  #指定取出某个位置的值
print(result)
print(li)


li = [2,2,3,4,5]
li.remove(2)  #取走第一个指定的元素值
print(li)


li.reverse()  #反转列表
print(li)
li.sort()   #排序
print(li)