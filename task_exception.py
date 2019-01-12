try:
    num = int(input("请输入一个整数\n"))
    print("-" * 50)

    result = 8/num

    print(result)

except NameError:
    print("输入值错误")

except ZeroDivisionError:
    print("分母是零")

except ValueError:
    print("输入值错误")

except Exception as result:
    print("未知错误 %s" % result)
else:
    print("尝试成功")
finally:
    print("无论尝试成功与否都会执行")

print("*" * 50)













