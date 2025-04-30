#print(5%3,5%-3,-5%-3)
# from email.quoprimime import body_check

# ask = str(input("你想要和谁打招呼?"))
# print("你好",ask,end="")
# print("再见",ask)
# while True:
#     try:
#         n = int(input("n="))
#     except ValueError:
#         pass
#     else:
#         break
#
# i = 1
# s = 1
#
# while i < n:
#     i = i + 1
#     s = s + i
#
# print(f"1+2+……+{n}={s}")
# for i in [1,0]:
#     print(i+1)
# y = 0
#
# for i in range(0, 10, 2):
#
#     y += i
#
# print(y)

# def fun(x,y):
#     print("In fun:",x,y)
#     x = 1
#     y = 2 #局部函数x，y仅仅在函数中有x，y
#     return x
#     return y
#
# x = 100
# y = 200
# fun(x,y)
# print(x,y) #这里输出的是主程序的x，y

# print("baka",9,sep="-")
# print(1,2,end="*")
# print()
# print(2025,"03",31,sep=":",end=" ")
# print(13,51,10,sep=":")

# import time
#
# # 获取当前时间的时间戳
# current_timestamp = time.time()
#
# # 将时间戳转换为本地时间
# local_time = time.localtime(current_timestamp)
#
# # 格式化时间
# formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', local_time)
#
# print(formatted_time) # 输出例如：'2021-08-17 15:47:58'

a = {"a":5,"b":6}

a.clear()

print(a)
