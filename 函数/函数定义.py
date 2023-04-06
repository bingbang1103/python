# 定义:def 函数的名字():被封装的功能或者代码块->函数体
# 调用:
# 函数的名字()
# def luru(name,age,gender="男"):
#     print(name,age,gender)
#
# luru("张三",26)#有默认值可以省略，且要放在后面
# luru("李四",28,"女")
#
#
#
# 动态传参.
# 1. *args，
# 表示接收所有的位置参数的动态传参
# def chi(*food):
#     print(food)
#
# chi("大米",'烧茄子',"蛋花汤")

# #2.**args,关键字再动态传参
# def chi(**food):
#     print(food)
#
# chi(zhu="米饭",fu="粥")
# # 顺序: 位置 > *args >默认值> **kwargs


# lst=["张三","李四","刘二"]
# def func(*args):
#     print(args)
# func(*lst)
#*在实参位置，是把列表打散成位置参数进行传递
#**在实参位置，可以把字典自动转化成关键字参数进行传递



# for i in range(65536):
#     print(chr(i)+" ",end="")#给出编码位置，展示出文字



