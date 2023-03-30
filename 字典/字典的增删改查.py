# dic=dict()
# #增
# dic['jay']="周杰伦"
# dic[1]=123
# print(dic)
# #改
# dic['jay']="张杰"
# print(dic)
# dic.setdefault("tom","汤姆")#setdefault设置默认值
# #如果以前有有tom，setdefault不起任何作用、
# #删
# dic.pop("jay")#根据key去删除
# #查询
# print(dic['tom'])#如果key不存在，会报错
# print(dic.get("tom10086"))#key不存在，返回None
#

#案例
# dic={
# "赵四":"特别能歪嘴",
# "刘能":"老，老四啊...",
# "大脚":"跟这个和那个搞对象",
# "大脑袋":"瞎折腾....",
# }
# name=input("请输入我们村人的名字：")
# val=dic.get(name)
# if val is None:
#     print("我们村没这个人~~~")
# else:
#     print(val)

#循环
dic={
 "赵四":"特别能歪嘴",
 "刘能":"老，老四啊...",
 "大脚":"跟这个和那个搞对象",
 "大脑袋":"瞎折腾....",
 }
# for key in dic:
#     print(key,dic[key])

#希望把所有的key全部保存在一个列表中
#print(list(dic.keys()))

#把全部的values都放在一个列表中
#print(list(dic.values()))

#直接拿到字典中的keyhevalue
# for item in dic.items():
#     key=item[0]
#     value=item[1]
#     print(key,value)

# a,b=(1,2)#元组或列表都可以执行改操作吗，该操作称为解构（解包）

for key,value in dic.items():
    #print(item) #确定，item中只有两项元素
    print(key,value)
