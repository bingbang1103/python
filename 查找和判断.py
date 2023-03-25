#查找
'''
s="你好，我叫周润发"
ret=s.find("周润发")
print(ret)
ret1=s.find("张三")
print(ret1)#找不到会返回-1！
#ret2=s.index("张三")#找不到会报错！
print("周润发" in s)#true/false --in做条件上的判断
print("周润发" not in s)#not in 判断是否不存在
'''
#判断

#判断字符串是否以XXX开头或结尾
#startswith()
#endswith()
# name=input("请输入你的名字：")
# if name.startswith("张"): #判断字符串是否以XXX开头
#     print("你姓张")
# else:
#     print("你不姓张")

#isdigit()判断是否为整数
money=input("请输入你兜里的钱：")
if money.isdigit():
    money=int(money)
    print("可以花钱了")
else:
    print("对不起，你输入有误....")




