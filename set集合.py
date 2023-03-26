#set集合是无序的,无法索引
# s={1,'hhd',2,3}
# print(s)

# s = {1, 'hhd', 2, 3,}#TypeError: unhashable type: 'list'
# print(s)
#不可哈希：python中的set集合进行数据存储的时候，需要对数据进行哈希计算，
#根据哈希计算的值进行存储数据
#set集合要求存储的数据必须是可以进行哈希计算的
#  可变的数据类型，list,dict,set
#可哈希：不可变的数据类型，int，str ,tuple,bool

s1={1,2,"haha",(1,2,3)}
print(s1)
#想要修改先删除
s1.remove("haha")
print(s1)
s1.add("马云")
print(s1)
#查询
for item in s1:
    print(item)