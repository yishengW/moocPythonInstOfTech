TempStr=input("请输入带单位的温度：")
if TempStr[-1] in ['f','F']:
    C=(eval(TempStr[0:-1])-32)/1.8
    print("转换后的温度{:.2f}C".format(C))
elif TempStr[-1] in ['c','C']:
    F=(eval(TempStr[0:-1])*1.8)+32
    print("转换后的温度{:.2f}F".format(F))
else:
    print("输入格式错误！")
