# 点击屏幕事件_魔法星空# 魔法星空的效果：如拥有魔法棒一般，用鼠标左键在屏幕的任意位置单击，单击在哪，哪里就会出现星星。
# 程序初始化操作
import turtle                   # 导入 turtle 库
import random                   # 导入 random 随机库
turtle.shape("turtle")          # 将海龟的真身召唤出来。海龟默认的形状是黑色小箭头。
turtle.pensize(1)               # 设置海龟绘图时画笔的粗细。
turtle.speed(0)                 # 设置海龟移动的速度也就是海龟绘图的速度为0。参数为0时速度最快，参数为1时最慢。
turtle.delay(0)                 # 设置海龟两次移动的间隔时间为0。数值越大延迟越长，绘图速度越慢。
turtle.colormode(255)           # 将默认的颜色模式切换为RGB模式
turtle.bgcolor(0,0,15)          # 设置背景颜色为（0,0,15），纯黑色为(0,0,0)  RGB(red,green,blue)
# 自定义函数star，画一个五角星
def star(length):               # 自定义函数star（有参函数，参数为length） length是五角星的边长
    r=random.randint(0,255)     # 随机生成一个[0,255]范围内的整数，并赋值给变量r
    g=random.randint(0,255)     # 随机生成一个[0,255]范围内的整数，并赋值给变量g
    b=random.randint(0,255)     # 随机生成一个[0,255]范围内的整数，并赋值给变量b
    turtle.color(r,g,b)         # 同时设置画笔颜色pencolor和填充颜色fillcolor为颜色(r,g,b）
    
    turtle.begin_fill()         # 开始填充颜色
    i=1
    while i<=5:
        turtle.forward(length)  # 海龟前进length像素，length是五角星的边长
        turtle.left(144)        # 海龟向左旋转144度
        i=i+1
    turtle.end_fill()           # 结束填充颜色
# 自定义函数f，画一个五角星
def f(x,y):
    turtle.penup()                # 画笔抬起（海龟抬起脚）
    turtle.goto(x,y)              # 海龟移动到坐标(x,y),x和y的值是由onscreenclick()指令产生的。
    turtle.pendown()              # 画笔落下（海龟落下脚）
    length=random.randint(10,50)  # 随机生成一个[10,50]范围内的整数，并赋值给五角星的边长length
    star(length)                  # 调用自定义函数star
# 用鼠标左键在画布任意位置单击，onscreenclick()指令就会把该位置的坐标(x,y)传递给自定义函数f。
turtle.onscreenclick(f)     
turtle.hideturtle()               # 隐藏海龟