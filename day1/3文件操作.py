#!/usr/bin/env python
# -*- coding:utf-8 -*-

f = open("test.log", "w") #写文件

f.write("this is file")

f = open("test.log", "r") #读文件

for line in f:
    print(line)
f.close()


f = open("test.log", "r") #追加
f.write("this is 2 file")

