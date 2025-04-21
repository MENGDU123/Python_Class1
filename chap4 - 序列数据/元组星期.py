week = ('日','一','二','三','四','五','六') #元组也是列表的一种，但是不能被更改！
try:
    w = int(input("w="))
except ValueError:
    print("非法输入")
    exit(1)
else:
    if w < 1 or w > 7:
        print("#N/A")
        exit(1)
    elif w == 7:
        w = 0
    else:
        pass
print(week[w])