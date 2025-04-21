'''
设计一个程序，可以用来查找字符串中的子串。
'''
def myFind(s,t):
    m = len(s)
    n = len(t)
    if m < n:
        return -1
    i = 0
    while i <= m - n:
        j = 0
        while j < n:
            if s[i + j]!= t[j]:
                break
            j = j + 1
        if j == n:
            return i
        i = i + 1
    return -1

s = input("请输入字符串")
t = input("请输入查找的字符串")

if myFind(s,t) == -1:
    print("找不到字符串")
else:
    print(f"找到该字符串，位置为：{myFind(s,t)}")