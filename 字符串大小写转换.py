s="I have a dream!"
s1=s.title()#单词的首字母大写
print(s1)
Y="I HAVA A DREAM!"
y1=Y.lower()#大写变小写
print(y1)
X="i have a dream!"
x1=X.upper()
print(x1)
verify_code="xAd1"
user_input=input(f"请输入验证码（{verify_code}）：")
if verify_code.upper()==user_input.upper():
    print("验证码正确！")
else:
    print("验证码错误！")
