dict = {'name':"张三","age":20}
print(dict)
print(dict['name'])
print(dict['age'])

dict1 = {'省份':'江苏',
            '城市':['南京','无锡']}

print(dict1['城市'][0])
for i in range(len(dict1['城市'])):
    print(dict1["城市"][1],end="")

for i in dict1['城市']:
    print(i,end='')

print()

dict['age']="21" #修改字典值
print(dict['age'])
dict['school']="苏信" #如果字典里没有该键，则为新建
print(dict)

del dict['age'] #删除字典条目
print(dict)

print(len(dict1)) #列出字典长度

dict.clear() #清空字典
print(len(dict))