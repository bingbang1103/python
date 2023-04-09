import traceback
import logging
# try:
#     print(1/0)
# except:
#     print("程序出错了")
#     print(traceback.format_exc())
#
# print(666)


#准备好日志的logging

logging.basicConfig(filename='x2.txt',
                     format='%(asctime)s - %(name)s - %(levelname)s %(module)s: %(message)s',
                     datefmt='%Y-%m-%d %H:M:s',
                     level=40) #记录文件中的日志的最低等级

#正常写程序
try:
    print(1/0)
except:
    print("出错了")
    logging.error(traceback.format_exc())
