import xml.etree.ElementTree as ET

tree = ET.parse('test.xml')

root = tree.getroot()
print(root.tag)



'''
#遍历xml文档
for child in root:
    print(child.tag, child.attrib)
    for i in child:
        print('-->', i.tag, i.text)



# 遍历某个结点
for node in root.iter('year'):
    print(node.tag, node.text)



#修改
for node in root.iter('year'):
    new_year = int(node.text) + 1
    node.text = str(new_year)  #把值修改
    node.set('xinshuxing', 'ok')
'''


#删除   不能使用
'''
for country in root.findall('country'):
   rank = int(country.find('rank').text)
   if rank > 50:
     root.remove(country)
'''
tree.write('xmltest.xml')  #写入新文件



#创建xml