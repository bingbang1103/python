# lst=[224,242,11,2464,5567,32,23]
# lst.sort()# sort排序--升序
# print(lst)
# lst.sort(reverse=True)#reverse--翻转
# print(lst)


lst=[1,12,33,['你好',"你好啊",['dengzhibin']],23]
print(lst[3][2][0])
lst[3][2][0]=lst[3][2][0].upper()
print(lst)