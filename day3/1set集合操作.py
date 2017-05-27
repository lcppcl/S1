#set是一个无序且不重复的元素集合
#访问速度快，天生解决重复问题
s1 = set()
s1.add('alex')
print(s1)
s1.add('alex')   #set集合中不允许有重复元素
print(s1)


s2 = set(['lcp', 'lop', 'lcp', 'alex'])  #创建set时，自动去掉重复元素
"""s3 = s2.difference(['lcp'])   #不改变原来的集合，会生成一个新的集合,s2集合和['lcp']不同的元素的集合
print(s3)
s2.difference_update('lop')  #改变原来的集合，不会生成新的集合，去掉一个相同的值
print(s2)
value = s2.pop()  #s2里面拿走一个值，并赋给另外一个变量
print(s2)"""
s2.remove('alex')  #制定拿走一个元素，但是没有返回值
print(s2)


old_dict = {
    "k1":{'host':'host','name':'name'},
    "k2":{'host2':'host2','name2':'name2'},
    "k3":{'host3':'host3','name3':'name3'},
}
new_dict = {
    "k1":{'host':'host','name':'name'},
    "k3":{'host2':'host2','name2':'name2'},
    "k4":{'host3':'host3','name3':'name3'},
}
old_dict.keys()  #得到key的列表[]
old = set(old_dict.keys())  #把列表转换成集合
new = set(new_dict.keys())
#交集：需要更新的数据   1set集合操作.jpg
update_set = old.intersection(new)  #交集
delete_set = old.symmetric_difference(update_set)  #差集
add_set = new.symmetric_difference(update_set)



s1 = set([11, 22, 33, ])
s2 = set([44, 22, ])
ret1 = s1.difference(s2)  #[11, 33]s1中，不包含s2的所有元素
ret2 = s1.symmetric_difference(s2)  #[11,33,44]s1和s2不同时包含的元素
