
# open(文件路径,mode="",encoding="")
# 文件路径：
# 1.绝对路径：D:test/xxx/test.txt
#2.相对路径：相对于当前程序的所在文件夹
#../上一层文件夹
# mode:
#     r:read 读取
#encoding="编码"
f=open("葫芦侠.txt",mode="r",encoding="utf-8")
# content=f.read()#全部读取
# print(content)
# line=f.readline()#读取一行
# print(line)
#最重要的
for line in f:
    print(line.strip())