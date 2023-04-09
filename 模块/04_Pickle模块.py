import pickle
# lst=["成龙","赵本山","张三"]
# bs=pickle.dumps(lst)#转化成字节
# print(bs)
#
# bs=b'\x80\x04\x95#\x00\x00\x00\x00\x00\x00\x00]\x94(\x8c\x06\xe6\x88\x90\xe9\xbe\x99\x94\x8c\t\xe8\xb5\xb5\xe6\x9c\xac\xe5\xb1\xb1\x94\x8c\x06\xe5\xbc\xa0\xe4\xb8\x89\x94e.'
# lst=pickle.loads(bs)#把字节转化成文本
# print(lst)


# #把数据存储到文件中最合理的方案就是pickle
# dic = {"nane":"admin","password":123}
# pickle.dump(dic,open("d.data",mode="wb"))
# #读取也必须用pickle读取
# dic=pickle.load(open("d.data",mode="rb"))
# print(dic)

'''
序列化: 把对象转化成二进制字节
反序列化: 把二进制字节转化回对象
1. dumps把对象(数据)转化成字节
2. Loads把字节转化回对象(数据)
3. dunp把对象序列化成字节之后'写入'到文件是。
4. load 把文件中的字节反序列化成对象--(读取)
'''