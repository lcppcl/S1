import re

m = re.match('abc', 'abcdef')  #match()只能从数据源的开头匹配
print(m.group())   #group()显示匹配的内容

m1 = re.match('[0-9]', '43ab6')  #[0-9]只匹配一个
if m1:
    print(m1.group())


m1 = re.match('[0-9]{0,10}', '43342532532532abdferer6')  #{0,10}最长匹配0到10个，多余10个就不匹配
if m1:
    print(m1.group())
m1 = re.match('[0-9]{10}', '43ab6')  #{10}只匹配10个数字
if m1:
    print(m1.group())

m = re.findall("[0-9]", "f9e8r7f5e56v6c43v2f3d31f0r5")  #findall()数据源的每个数据都匹配一遍
if m:
    print(m)
m = re.findall("[0-9]{1,2}", "f9e8r7f5e56v6c43v2f3d31f0r5")  #findall()数据源的每个数据都匹配一遍,
if m:
    print(m)

m = re.findall('[a-zA-Z]',"eff34vfdcv")  #匹配所有字母
if m:
    print(m)

m = re.findall('.*',"eff34vfdcv")  #匹配任意字符
if m:
    print(m)

m = re.findall('.+',"eff34vfdcv")  #匹配一个或多个
if m:
    print(m)

m = re.findall('[a-zA-Z]+',"eff3_4vfdcv")  #匹配一个或多个字符
if m:
    print(m)

m = re.search("\d+", "as56cdcf")  #找到第一个数字返回
if m:
    print(m)

m = re.sub("\d+", "=", "ade32_ded54",count=2)  #将前两个数字替换成=
if m:
    print(m)

m = re.search("^\d+$","3eds0")  #^是以什么开头，$是以什么结尾
if m:
    print(m)