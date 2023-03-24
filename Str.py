name=input("请输入你的名字：")
age=int(input("请输入你的年龄："))
address=input("请输入你的地址：")
hobby=input("请输入你的爱好：")
# %s 字符串占位
#s="我叫%s，我住在%s，我今年%d岁，我喜欢%s" %s(name,address,age,hobby)
s1="我叫{}，我住在{}，我今年{}岁，我喜欢{}".format(name,address,age,hobby)
s2=f"我叫{name}，我住在{address}，我今年{age}岁，我喜欢{hobby}"
#print(s)
print(s1)
print(s2)