#try...except来处理异常
# try:
#     print(1/0)
# except:
#     print("程序出错了，请联系管理员")
#
# try:
#     print(1/0)
#     # open("hehe",mode="r").read()
#     # lst=[]
#     # lst.__iter__().__next__()
# except ZeroDivisionError as z:
#     print("除数为0")
# except FileNotFoundError as f:
#     print("文件不存在")
# except Exception as e:
#     print("系统错误")
# finally:
#     print("收尾")#无论是否出错误，都要收尾
#
#
def func(a,b):#计算两个int类型的和
    if type(a)== int and type(b)==int:
        return  a+b
    else:       #谁调用的，谁接受该异常
        raise Exception("你给我的不是int类型，无法计算")

sum=func("hehe",2)
print(sum)

