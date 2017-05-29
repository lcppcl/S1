#!/usr/bin/env python
# -*- coding:utf-8 -*-

f = open('test.log', 'w', encoding='utf-8')
f.write('我123098765就斤斤计较')
f = open('test.log', 'r+', encoding='utf-8')
f.seek(3)  #设置当前指针的位置
print(f.tell())  #读取指针的位置，还未读为0
ret = f.read(2)  #read读取当前指针后面的字符
print(f.tell())  #tell按字节读，查看当前指针位置
print(ret)
f.truncate()  #读取当前指针前面的数,并放到原文件
f.close()