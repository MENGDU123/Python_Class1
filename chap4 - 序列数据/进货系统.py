"""
在示例代码的基础上完成下列任务：
1、添加蛋糕，价格15元。
2、将可乐涨价到3.5元。
3、棒棒糖缺货了，请从清单上删除。
4、超市倒闭了，清空列表。
"""
goods = {"方便面":5,"可乐":3,"雪碧":3,"棒棒糖":1}
print(goods["雪碧"])
for sp in goods:
    print(sp,goods[sp])

###以上为示例代码###

goods['蛋糕']=15
print(goods)

goods['可乐']=3.5
print(goods)

del goods['棒棒糖']
print(goods)

goods.clear()
print(goods)