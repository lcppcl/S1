"""
[11,22,33,44,55,66,77,88,99,....]
将所有大于66的值保存至字典的第一个key中，将小于66的值保存至第二个key的值中
即：{'k1':大于66,'k2':小于等于66}
"""
from collections import defaultdict
all_list = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90,]
dic = defaultdict(list)
for value in all_list:
    if value>66:
        dic['k1'].append(value)
    else:
        dic['k2'].append(value)
print(dic)