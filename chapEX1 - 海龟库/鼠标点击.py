#点击画布任意区域，海龟移动到那里
import turtle
def f(x,y):
    turtle.goto(x,y)
turtle.onscreenclick(f)
# turtle.done()      在python自带的编辑器和MU编辑器中，这行代码可以省略                      # 在pycharm编辑器中必须要使用，不然绘图结束后会闪退。