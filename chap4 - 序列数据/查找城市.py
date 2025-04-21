"""
输入城市查找城市
"""
provinces = ["江苏","四川","广州"]
cities = [["南京","无锡","苏州","常州"],["成都","内江","乐山"],["广州","深圳","惠州","珠海"]]
p = str(input("请输入要查找的省份："))
for i in range(len(provinces)):
    if provinces[i] == p:
        for j in range(len(cities[i])):
            print(cities[i][j],end="，")
        exit(0)

print("没有找到该省份。")

def secrch(c):
    for m in range(len(cities)):
        for n in cities[m]:
            if n == c:
                print(c,"在",provinces[m]+"省")
c = str(input("请输入要查找的城市："))
secrch(c)
