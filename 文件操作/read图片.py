#
# with open("广州.png",mode="rb") as f:
#     for line in f:
#         print(line)

#非文本文件endoing不能用mode=" +b"

#图片复制:从源文件读取内容后，写入新入径
with open("广州.png",mode="rb") as f1,\
     open("../test/广州2.png",mode="wb") as f2:
     for line in f1:
         f2.write(line)
