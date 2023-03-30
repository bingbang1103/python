dic={
 "赵四":"特别能歪嘴",
 "刘能":"老，老四啊...",
 "大脚":"跟这个和那个搞对象",
 "大脑袋":"瞎折腾....",
 }
temp=[]#存放即将删除的key
for key in dic:
    if key.startswith("大"):
        temp.append(key)#将要删除的添加到temp列表

for t in temp:
    dic.pop(t)

print(dic)