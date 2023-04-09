import json
# 1.把python中的字典或者列表。转化成ison字符串
# dic={"id":1,"name":"我叫张三","usertype":0}
# s=json.dumps(dic,ensure_ascii=False)#处理中文时要加ensure_ascii=False
# print(s,type(s))

# 2.前端返回的json字符串， 想办法编程python中的字典
s='{"id":1,"name":"我叫张三","usertype":0}'
dic=json.loads(s,)
print(dic,type(dic))
print(dic['name'])#字典查询

# # 前端的json和python中的字典有什么区别
#     {"id":1,"islogin": true,"hasGiri": null}
# d = {"id":1,"islogin": True,"hasGiri": None])
# print(json.dumps(d)


# # 数据类型的写法不一样
# python        前端
#  True        true
#  False       false
#  None        null
#列表一样可以进行json转换

