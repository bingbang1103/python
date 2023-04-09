from datetime import datetime
from datetime import date#掌握一个


# print(datetime.now())#现在时间
# print(datetime(2018,1,1,12,00,1))

#
# t1=datetime(2018,1,1,12,00,1)
# t2=datetime(2018,1,19,20,50,29)
# diff=t2-t1
# print(diff)
# print(diff.total_seconds())#秒


#格式化时间
# t=datetime.now()
# print(t)
# print(t.strftime("%Y年%m月%d日%H时%M分%S秒"))

# s1=input("请输入第一个时间(Y-mm-dd HH:MM:SS)：")
# s2=input("请输入第二个时间(Y-mm-dd HH:MM:SS)：")
# #把字符串转化成时间
# t1=datetime.strptime(s1, "%Y-%m-%d %H:%M:%S")
# t2=datetime.strptime(s2, "%Y-%m-%d %H:%M:%S")
# print(t2-t1)

# date
# print(date.today())今天的日期
# print(date(1988,12,3))