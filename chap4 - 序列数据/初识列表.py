from tkinter.constants import EXTENDED

list1=['a','a',1,1,4,5,1,4]
print(list1)
print(list1[2])
print(list1[2:8]) #切片
list1[0] = 'A' #列表是允许修改的,直接赋值可以更改
print(list1)
del list1[0:2] #删除元素
print(list1)
list2 = ["a","a"]
list3 = list2 + list1 #列表可以合并
print(list3)
#L[start:end:step]
list1.append("MENGDU") #末尾加入
print(list1)
print(list1.count(1))#count用于统计某个元素出现次数
list1.extend(list2) #这也是一种合并方式
print(list1)
list1.remove(1) #删除默认删除第一个该出现的该元素，不存在的元素会报错！ #不如del
print(list1)
list1.pop()#删除最后一个元素
print(list1)
list1.pop()#删除最后一个元素
print(list1)
list1.pop(0)#删除第一个元素
print(list1)
list1.reverse()#颠倒列表
print(list1)