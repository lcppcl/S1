name = 'lcp'
name2 = str('lcp')  #默认执行str类的__init__方法
print(type(name))
print(dir(name))  #显示类的所有成员


result = name.__contains__('er')  #包含
print(result)
result = 'er' in name  #和上面那就意思相同
print(result)


result = name.capitalize()  #首字符小写变大写
print(result)


result = name.casefold()   #首字符大写变小写
print(result)


result = name.center(20, '*')  #值居中，第一个参数是值，第二个参数是填充字符
print(result)


name = 'cdfvdfvergfvvgthyhb '
result = name.count('df')  #计算某个子序列字符出现的次数
print(result)
result = name.count('df', 0, 10)  #后面两个参数是指定起始位置
print(result)


name = '李杰'
result = name.encode('gbk')  #转换编码   内部先把utf8编码转化成Unicode，然后再把Unicode转换成gbk
print(result)


name = 'lcp'
result = name.endswith('e')  #判断字符串是不是以某个字符串结尾
result = name.endswith('e', 0, 3)  #可以指定子序列是不是以某个字符串结尾


name = 'l\tcp'
result = name.expandtabs()  #把\t默认转化成8个空格
print(result)

name = 'lcp'
result = name.find('cp')  #查找某个值，返回他的索引，没有找到返回-1
result = name.find('cp', 0, 5)  #指定查找位置
print(result)
result = name.index('cp')  #若查找的值不再，就会报错
print(result)


name = 'lcp {0} as {1} {sex}'
result = name.format('sb', '2ll', sex='男')  #拼接字符串
print(result)


li = ['s', 'b', 'lcp']
result = "".join(li)    #字符串连接
print(result)
result = "-".join(li)   #前面双引号可以指定连接格式
print(result)


# inTab = 'aeiou'
# outTab = '12345'
# trantab = maketrans(inTab, outTab)
# str = "this is string example...wow"  #将a替换成1，与此对应
# str.translate(trantab, 'xs')  #同时去掉xs


name = 'liukaiissb'
result = name.partition('is')  #按指定字符串分割
print(result)


result = name.replace('a', 'o')  #把指定字符转换成另外一个
print(result)
result = name.replace('a', 'o', 1)  #后面的数字指定转换的个数
print(result)


name = """
    aa
    bb
    cc
"""
result = name.split('\n')  #以指定字符分割
print(result)
result = name.splitlines()   #以每一行分割
print(result)




