import zipfile
#创建压缩包
# f=zipfile.ZipFile("dir2/abc.zip",mode="w")
# f.write("x2.txt")
# f.close()

#解压缩
f=zipfile.ZipFile("dir2/abc.zip",mode="r")
#直接全部进行解压缩
# f.extractall("dir2/abc")
#一个一个解压缩
for name in f.namelist():
    f.extract(name,"dir2/hehe")