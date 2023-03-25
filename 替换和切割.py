'''
s=" 我叫 周杰 伦 "
s1=s.strip()#去除字符串左右两端的空白符（空格 \t \n）
print(s)
print(s1)
'''
#案例
'''
username=input("请输入用户名：").strip()#去除左右两端的空格
password=input("请输入密码：").strip()
if username=="admin":
    if password=="338101":
        print("登录成功！")
    else :
        print("密码错误，登录失败！")
else:
    print("账户不存在，登录失败！")
'''
'''
#字符串替换
ch="你好啊！张三。"
ch1=ch.replace("张三","李四")
print(ch1)
a="he l lo !"
a1=a.replace(" ",'')#去除空格
print(a1)
'''
#split(用什么切) 字符串切割，用什么切，就会损失掉谁
a="python_java_c_c++_javascript"
lst=a.split("_")#切割的结果会放在列表中
print(lst)
