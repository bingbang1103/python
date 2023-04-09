import logging
# filename:文件名
# format: 数据的格式化输出， 最终在日志文件中的样子
# 时间-名称-级别-模块: 错误信息
# datefmt: 时间的格式
# Level: 错误的级别权重，当错误的级别权重大于等于leval的时候才会写入文件
# logging.basicConfig(filename='xl.txt',
#                     format='%(asctime)s - %(name)s - %(levelname)s %(module)s: %(message)s',
#                     datefmt='%Y-%m-%d %H:M:s',
#                     level=40) #记录文件中的日志的最低等级
#最高级别的日志信息 50
# logging.critical("今天系统炸了，请程员来调试")
# #40
# logging.error("一般指的是普通的程序错误，俗称bug")
# #30
# logging.warning("一个警告信息")
# #20
# logging.info("一个普通的消息")
# #10
# logging.debug("默认最低等级的消息")
# #0
# logging.NOTSET

import logging
#创建一个操作日志的对象Logger (依赖FileHandler)
file_handler = logging.FileHandler('l1.log','a', encoding='utf-8')
file_handler.setFormatter(logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s:%(message)s"))
logger1=logging.Logger('财务系统',level=40)
logger1.addHandler(file_handler)

#再创建一个操作日志的对象Logger (依赖FileHandLer)
file_handler2 = logging.FileHandler('l2.log','a', encoding='utf-8')
file_handler2.setFormatter(logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s: %(message)s"))
logger2=logging.Logger('会计系统',level=40)
logger2.addHandler(file_handler2)

#项目一：财务系统出错误了
logger1.error('财务系统炸了，程序员出来工作了')
#项目二
logger2.error("会计系统出错了，领导出来溜达溜达")
logger1.log(9999,"没事")