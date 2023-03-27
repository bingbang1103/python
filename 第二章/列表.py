#定义：能装东西的东西
#a=["张三丰","张无忌","张绍刚",[1,2,3,true]]
#特性：
#1.有索引和切片
#2.索引超过范围会报错
#3.可以用for循环遍历
#4.可以用len拿列表的长度
lst=["张三丰","张无忌","张绍刚","杨过"]
print(lst[0])
print(lst[1:3])
print(lst[::-1])
for item in lst:
    print(item)

print(len(lst))

