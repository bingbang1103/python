import time

#
# print("你好！")
# time.sleep(5)#暂停5秒
# print("你也好！")

# while True:
#     print("抓取百度的信息")
#     time.sleep(1)


#print(time.time())#时间戳 1970-01-01 00:00:00


#计算时间差
start=time.time()
for i in range(1000000):
    print(i)
end=time.time()
print(end-start)