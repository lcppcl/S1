tu =(50,) #元祖只包含一个元素时，需要在元素后面添加逗号


#元组中的元素值是不能修改，可以对元祖进行连接组合
tu = (1, 2, 3,)
tu = tuple((1, 2, 3,))

tu = tuple([1, 2, 3, ])   #把列表转换成元祖


li = [1, 2, 3,]
tu = tuple(li)   #把列表转换成元祖
li = list(tu)   #把元祖转化成列表
