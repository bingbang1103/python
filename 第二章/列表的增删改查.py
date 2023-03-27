#增删改查
# append()---追加
# lst=[]
# lst.append("张无忌")
# lst.append("张三丰")
# print(lst)
# #insert() 插入
# lst.insert(1,"马大哈")
# print(lst)
# #extend() 合并两个列表
# lst.extend(['武则天','嬴政','马超'])
# print(lst)
# #删除
# ret=lst.pop(1)#给出被删除的索引，返回被删除的元素
# print(lst)
# print(ret)
# lst.remove("马超")#删除某个元素，不返回
# print(lst)
# #修改
# lst[3]="项羽"
# print(lst)
# #查询
# print(lst[2])#直接用索引查询


#练习：
lst=['武则天','嬴政','马超']
for i in range(len(lst)):
    item=lst[i]
    if item.startswith("武"):
        new_name="刘"+item[1:]
        print(new_name)
        #把新名字放进列表（需要索引）
        lst[i]=new_name#修改完成

print(lst)