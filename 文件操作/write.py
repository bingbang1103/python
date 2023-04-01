#f=open("笔记.txt",mode="w",encoding="utf-8")
#写入文件
# w模式下，如果文件不存在，自动的创建一个文件
# w模式下。每一次open都会清空掉文件中的内容
# f.write("有一天，")
#
# lst=['张三','李四','王五']
# for item in lst:
#     f.write(item)
#     f.write("\n")
#
# #a追加写入
# A=open("笔记.txt",mode="a",encoding="utf-8")
# A.write("在河边钓鱼")
#f.close()#每次操作之后，要关闭链接

# with 自动关闭文件
with open("笔记.txt", mode="r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())