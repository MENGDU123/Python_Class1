'''
该文件用于演示可变参数
——一次调用进行多次运算，无需重复调用函数。
'''
def max(*args):
    print(args)
    m = args[0]
    for i in range(len(args)):
        if m < args[i]:
            m = args[i]
    return(m)
print(max(1,2))
print(max(1,2,0,3))