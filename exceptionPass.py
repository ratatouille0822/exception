def input_password():

    pwd = input("请输入密码")
    if len(pwd) >= 8:
        return pwd

    print("抛出异常")
    ex = Exception("密码长度不够")
    raise ex


try:
    pass_word = input_password()
    print(pass_word)

except Exception as result:
    print(result)

