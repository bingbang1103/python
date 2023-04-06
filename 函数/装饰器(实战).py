login_flag=False
def login_verify(fn):
    def inner(*args,**kwargs):
        #完成登录校验
        global login_flag
        if login_flag==False:
            print("未登录！")
            while 1:
                username=input("用户名>>>")
                password=input("密码>>>")
                if username=="admin" and password=="123":
                    print("登录成功！")
                    login_flag=True
                    break
                else:
                    print("登录失败！用户名或密码错误！")
        ret=fn(*args,**kwargs)#后续程序执行
        return ret
    return inner
@login_verify
def add():
    print("添加员工信息")
@login_verify
def delete():
    print("删除员工信息")
@login_verify
def upd():
    print("修改员工信息")
@login_verify
def search():
    print("查询员信息")
add()
delete()
upd()
search()