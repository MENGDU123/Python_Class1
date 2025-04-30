def fun(x,y=2,*args,**kargs):
    print(x,y)
    print(args)
    print(kargs)

fun(1,2,3,4)
fun(1,2,3,4,z=5,d='demo')
fun(1,2,3,w=4) #建值参数不能写在未知参数前面