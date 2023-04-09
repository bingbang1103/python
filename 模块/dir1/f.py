import hashlib
# #创建MD5对象
# obj=hashlib.md5(b'asgdjksajasjkd')  # md5(b'盐')
# #把要加密的信息传递给obj
# obj.update("1527971".encode("utf-8")) # 需要转化成字节
# #从obj中拿到密文
# mi=obj.hexdigest()
# print(mi)

#正常的默认加密过程容易撞库，十分危险。
#解决：加盐

#加密函数
def func(salt,s):
    obj=hashlib.md5(salt)
    obj.update(s.encode("utf-8"))
    return obj.hexdigest()#返回一个加密后的密文

#用户注册
# username =input("请输入用户名：")
# password=input("请输入密码：")
# #动态加盐
# mi_password=func(username.encode("utf-8"),password)
#
# f=open('user.txt',mode='w',encoding="utf-8")
#
# f.write(username)
# f.write("\n")
# f.write(mi_password)#把密文写进去


#登录
# username=input("用户名：")
# password=input("密码：")
# password=func(username.encode("utf-8"),password)
# f=open("user.txt",mode="r",encoding="utf-8")
# uname=f.readline().strip()
# upwd=f.readline().strip()
# if username==uname and password==upwd:
#     print("登陆成功！")
# else:
#     print("登录失败！")



#文件加密
obj=hashlib.md5(b'deng')
f=open("hello.txt",mode="rb")
for line in f:
    obj.update(line)
#得到加密结果
print(obj.hexdigest())
#判断文件一致性：两个相同文件的MD5的值是相同的
#上传文件时，首先计算你上传文件的MD5的值
#比对数据库中有没有相同的MD5.如果有就是上传过，已经保存了
#文件改动前：e601d9b1cbd012a8aedc5967c9b7106d
#文件改动后：4b8bcafd2f70699a20bbbc1b5e8b96ca