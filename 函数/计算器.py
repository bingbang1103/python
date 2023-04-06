def jisuanqi(a,opt,b):
    if opt=="+":
        print(a+b)
    elif opt=="-":
        print(a-b)
    elif opt == "*":
        print(a * b)
    elif opt == "/":
        print(a/b)
    else:
        print("符号错误")

jisuanqi(99,"+",33)
jisuanqi(99,"-",33)
jisuanqi(99,"*",33)
jisuanqi(99,"/",33)
