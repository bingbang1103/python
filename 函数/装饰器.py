# 装饰器:
# ->要求记住最后的结论装饰器本质上是一个闭包
# 作用:
#   在不改变原有函数调用的情况下。给函数增加新的功能
#   直白:可以在函数前后添加新功能，但是不改原来的代码
#在用户登入的地方，日志。

# 通用装饰器的写法:
# def wrapper(fn):                          wrapper: 装饰器，fn: 目标函数
#       def inner(*args，**kwargs):          # 在目标函数执行之前.....
#           ret = fn(*args,**kwargs)        执行目标函数# 在目标函数执行之后.....
#       return ret
#   return inner
#                                            千万别加()

def guanjia(game):
    def inner(*args,**kwargs):#参数个数不限制
        print('打开外挂')
        game(*args,**kwargs)
        print('关闭外挂')
    return inner
@guanjia
def play_dnf(username,password):
    print('开始游戏！')
    print('......')
    print('游戏结束！')
#play_dnf=guanjia(play_dnf)#把游戏重新封装
play_dnf('root',20230405)

