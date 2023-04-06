a=10
def func():
    print(a)
#此时我就想在函数内部修改全局的变量a
global a # 把外面的全局变量引入到局部a = 28 # 创建一个局部变量。 并没有去改变全局变量中的afunel
print(a)


# global : 在局部，引入全局变量
# nonLocal: 在局部，引入外层的局部变量