lst=["张三丰","张无忌","张绍刚","杨过"]
temp=[]#准备一个临时列表，负责存储删除的内容
for item in lst:
    if item.startswith("张"):
        temp.append(item)#把要删除的内容记入到temp

for item in temp:
    lst.remove(item)
print(lst)

