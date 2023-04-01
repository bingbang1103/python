import os #引入和系统有关的模块
import time
with open("人名单.txt", mode="r", encoding="utf-8") as f1,\
     open("人名单_副本.txt", mode="w", encoding="utf-8") as f2:
    for line in f1:
        line = line.strip() #去掉换行
        if line.startswith("张"):
            line = line.replace("张", "周")#替换，修改

        f2.write(line)
        f2.write("\n")
time.sleep(3)
#删除源文件
os.remove("人名单.txt")
time.sleep(3)
#把副本重命名为源文件
os.rename("人名单_副本.txt", "人名单.txt")
